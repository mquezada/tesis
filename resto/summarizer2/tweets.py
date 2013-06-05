#!/usr/bin/env python
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

filter_words = ['i m', 'you re', 'don t', 'haven t', 'didn t']
filter_words += ['hadn t', 'he s', 'she s', 'it s', 'they re']
filter_words += ['we re', 'who s', 'what s', 'how s', 'why s']
filter_words += ['i am', 'cannot', 'cant']


def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')


def stem(word, lang='english'):
    stemmer = SnowballStemmer(lang)
    return stemmer.stem(word)


def filter_cont(sentence):
    """
    - removes diacritics
    - removes expressions like 'i am' or 'you re'
    - removes mentions, urls
    - removes # from hashtags
    - removes stopwords
    - stem words
    """
    sentence = sentence.lower()
    sentence = remove_diacritic(sentence)
    for word in filter_words:
        if word in sentence:
            sentence = sentence.replace(word, '')
    words = sentence.split()
    new_words = StringIO()
    for word in words:
        if not is_mention(word) and not is_url(word) and len(word) > 1:
            if not is_stopword2(word):
                if is_hashtag(word):
                    new_words.write(stem(word[1:]) + ' ')
                else:
                    new_words.write(stem(word) + ' ')
    return ' '.join(re.findall(r'\w+', new_words.getvalue(), flags=re.UNICODE | re.LOCALE))


PATH = '/Users/mquezada/Tesis/Boston Dataset'
days = (16, 22)

fw = ['boston', 'bomb', 'attack', 'terrorist', 'terrorists']
fw += ['bombs', 'marathon', 'attacks']


boston = []
for day in range(days[0], days[1] + 1):
    folder = PATH + '/201304' + str(day) + '/Tweets/'
    for filename in os.listdir(folder):
        with open(folder + filename, 'r') as f:
            print filename
            for line in f:
#                for word in fw:
#                    if word in line.lower():
                try:
                    m = line.split('\t')[7]
                    t = filter_cont(unicode(m, 'UTF-8'))
                    boston.append(t)
                except:
                    print m
#                finally:
#                    continue
#    break

#import nltk

#tc = nltk.TextCollection(map(nltk.wordpunct_tokenize, boston))
#tc.vocab().plot(50)
from collections import Counter
from operator import itemgetter

c = Counter()
for sent in boston:
    words = re.findall(r'\w+', sent, flags=re.UNICODE | re.LOCALE)
    for word in words:
        c[word] += 1


res =  sorted(c.items(), key=itemgetter(1), reverse=True)
