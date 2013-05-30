#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
import re
from nltk.corpus import stopwords
from StringIO import StringIO

english_sw = stopwords.words('english')
spanish_sw = stopwords.words('spanish')


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


def clean_and_tokenize(sentence):
    """
    - removes diacritics
    - removes urls
    - removes stopwords
    """
    sentence = remove_diacritic(sentence)
    words = sentence.split()
    new_words = StringIO()
    for word in words:
        if len(word) < 3:
            continue
        if not word.startswith('http') and not is_stopword2(word):
            new_words.write(word + ' ')
    return re.findall(r'\w+', new_words.getvalue(), flags=re.UNICODE | re.LOCALE)
