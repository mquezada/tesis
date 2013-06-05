# -*- coding: utf-8 -*-
import os
import re
import unicodedata
from StringIO import StringIO
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def is_mention(w):
    return w[0] == '@'


def is_hashtag(w):
    return w[0] == '#'


def is_stopword(word, lang='english'):
    return word.lower() in stopwords.words(lang)


def is_stopword2(word):
    w = word.lower()
    return w in stopwords.words('english') or w in stopwords.words('spanish')


def is_url(w):
    return w.startswith('http://')


def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')


stemmer = SnowballStemmer('english')


def stem(word, lang='english'):
    return stemmer.stem(word)

filter_words = ['i m', 'you re', 'don t', 'haven t', 'didn t']
filter_words += ['hadn t', 'he s', 'she s', 'it s', 'they re']
filter_words += ['we re', 'who s', 'what s', 'how s', 'why s']
filter_words += ['i am', 'cannot', 'cant']


def filter_cont(sentence):
    """
    - removes diacritics
    - removes expressions like 'i am' or 'you re'
    - removes mentions, urls
    - removes # from hashtags
    - removes stopwords
    - stem words
    """
    #sentence = sentence.lower()
    sentence = remove_diacritic(sentence)
    for word in filter_words:
        if word in sentence:
            sentence = sentence.replace(word, '')
    words = sentence.split()
    new_words = StringIO()
    for word in words:
        if not word[0] == '@' and not word.startswith('http') and len(word) > 1:
            if not is_stopword2(word):
                if word[0] == '#':
                    new_words.write(stemmer.stem(word[1:]) + ' ')
                else:
                    new_words.write(stemmer.stem(word) + ' ')
    ans = ' '.join(re.findall(r'\w+', new_words.getvalue(), flags=re.UNICODE | re.LOCALE))
    return ans

ROOT = '/Users/mquezada/Tesis'

"""open urls.txt and generates dictionary of urls"""
PATH = ROOT + '/summarizer2'

furl = open(PATH + '/urls.txt', 'r')
expanded_urls = {}
for line in furl:
    tok = line.split()
    short_link = tok[0]
    if len(tok) > 1:
        expanded = tok[1]
        expanded_urls[short_link] = expanded
furl.close()

"""generate url..=(id1,..,idn) based on filtered tweets and days"""
init = 16
#end = 23
end = 17  # 1 dia

docs = {}

kw = ['boston', 'bomb', 'attack', 'terrorist', 'terrorists']
kw += ['bombs', 'marathon', 'attacks']

PATH = ROOT + '/Boston Dataset'
for day in range(init, end):
    folder = PATH + '/201304' + str(day) + '/Tweets/'
    tweets = {}
    for filename in os.listdir(folder):
        if filename == '.DS_Store':
            continue
        with open(folder + filename, 'r') as f:
            print filename
            for line in f:
                for word in kw:
                    line2 = line.lower()
                    if word in line2:
                        try:
                            tokens = line2.split('\t')
                            m = tokens[7]
                            twid = tokens[1]
                            t = filter_cont(unicode(m, 'UTF-8'))
                            tweets[twid] = t
                        except:
                            print tokens
    print

    folder = PATH + '/201304' + str(day) + '/E_URLs/'
    for filename in os.listdir(folder):
        with open(folder + filename, 'r') as f:
            print filename
            for line in f:
                tokens = line.split('\t')
                if len(tokens) > 3:
                    possibly_short_url = tokens[-1][:-1]
                    if tokens[0] == '[-URL ]':
                        twid = tokens[2]
                    else:
                        twid = tokens[1]
                    try:
                        if int(twid) < 100000000:
                            continue
                        """si la url del archivo fue expandida, usar esa"""
                        if possibly_short_url in expanded_urls:
                            url = expanded_urls[possibly_short_url]
                        else:
                            url = possibly_short_url

                        """si la key url tiene tweets, añadir el actual"""
                        if url in docs:
                            docs[url].append(twid)
                        else:
                            docs[url] = [twid]
                    except:
                        continue

"""como lista de palabras
event_docs = {}
words = []
for url, ids in docs.items():
    utweets = []
    for id in ids:
        if id in tweets:
            utweets.extend(tweets[id].split())
            words.extend(tweets[id].split())
    if len(utweets) > 0:
        event_docs[url] = utweets

words = list(set(words))
"""

"""como texto"""
event_docs = {}
for url, ids in docs.items():
    utweets = ''
    for id in ids:
        if id in tweets:
            utweets = utweets + ' ' + tweets[id]
    if len(utweets) > 0:
        event_docs[url] = utweets

import operator
from sklearn import cluster
from sklearn.feature_extraction.text import TfidfVectorizer


event_items = event_docs.items()
texts = map(operator.itemgetter(1), event_items)

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(texts)

n_clusters = 5

kmeans = cluster.KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, verbose=1)
kmeans.fit(matrix)

# asignar labels
clust_data = zip(map(operator.itemgetter(0), event_items), kmeans.labels_)

clusters = [[]] * n_clusters
for data in clust_data:
    clusters[data[1]].append(data[0])

"""clusters[] contiene las URLs"""
