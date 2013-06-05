#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tokenizer import words
from dataset.filter import filter_dataset
from files import files

from collections import Counter

import settings

# shorcuts
cl = words.clean_and_tokenize
url_finder = words.tco_urls_pattern

# containers
docs = {}  # {url : [id_1, id_2, ..., id_d]}
tweets = {}  # {id : tokens_ti}
docs_str_freq = {}  # {url: [(tweet_str, freq), ...]}
u_index = {}  # {'t.co/asdf' : 'http://www.example.com/foo.html?bar='}

# settings
keywords = ['boston', 'marathon']

#########################################################################

print "=== Filtering tweets from dataset ==="
tweets_data = filter_dataset.filter_by_keywords(keywords)
print "=== tweets_data created ==="

#########################################################################

print "=== creating urls dicts ==="


def process_file(f, day):
    for line in f:
        short, exp = line.split()
        u_index[short] = exp

files.read('other', process_file, other_path=settings.URLS_EXPANDED_DIR)
print "=== u_index created ==="

#########################################################################

print "=== clean tweets and build docs data ==="
print "processing", len(tweets_data), "tweets"
for id, lang, tweet in tweets_data:
    tweets[id] = cl(tweet, stem_words=True, lang=lang)
    for url in url_finder.findall(tweet):
        if url not in docs:
            docs[url] = []
        docs[url].append(id)
print "=== docs created ==="
#########################################################################

print "=== unsplit tweets and reduce by number of occurrences(?) ==="
for url, ids_list in docs.iteritems():
    tweet_tokens_list = map(lambda id: tweets[id], ids_list)
    tweet_list = map(lambda tokens: ' '.join(tokens), tweet_tokens_list)
    tweets_count = Counter(tweet_list)

    docs_str_freq[url] = tweets_count.items()
print "=== docs_str_freq created ==="
