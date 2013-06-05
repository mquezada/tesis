#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


english_sw = stopwords.words('english')
spanish_sw = stopwords.words('spanish')

stemmers = {
    'en': SnowballStemmer('porter'),
    'es': SnowballStemmer('spanish'),
    'pt': SnowballStemmer('portuguese'),
    'it': SnowballStemmer('italian'),
    'fr': SnowballStemmer('french'),
    'de': SnowballStemmer('german'),
}

tco_urls_pattern = re.compile("(https?:\/\/.*?/[a-zA-Z0-9]*)")


def is_stopword2(word):
    w = word.lower()
    return w in english_sw or w in spanish_sw


def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    try:
        return unicodedata.normalize('NFKD', unicode(input, 'utf-8')).encode('ASCII', 'ignore')
    except:
        return ''


def clean_and_tokenize(sentence, stem_words=False, lang='en'):
    """
    - removes diacritics
    - removes urls
    - removes stopwords
    - removes punctuation
    - tokenizes sentence
    - stems words
    """
    sentence = remove_diacritic(sentence)  # removes accents
    sentence = tco_urls_pattern.sub('', sentence)  # removes urls
    words = re.findall(r'\w+', sentence, flags=re.UNICODE | re.LOCALE)  # tokenize, removes punctuation
    if stem_words:
        loc_stem = lambda w: stem(w, lang=lang)
    else:
        loc_stem = lambda x: x
    return [loc_stem(w.lower()) for w in words if not len(w) < 3 and not is_stopword2(w)]  # filters short words and stop words


def stem(word, lang='en'):
    return stemmers.get(lang, stemmers['en']).stem(word)


def main():
    sents = [
        'RT @KevinHart2ReaI: If you tweeted #prayforboston actually pray because God doesn t answer tweets',
        'Nope & I still ain t RT @itsJADEhun: When the lakers were playing the celtics was y all "team boston" then?',
        'RT.like follow.me ánimo IF ME',
        'RT @analisaspina: the 8 year old girl that died 😭💔 #prayforboston 🙏 http://t.co/AUMWHofsA5'
    ]

    print sents
    print
    for s in sents:
        print clean_and_tokenize(s)

if __name__ == '__main__':
    main()
