#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statscollector
from nltk import pos_tag
from words import *

np_freqs = []


def init(counters):
    global np_freqs
    np_freqs = counters


def process_file(f, day):
    for line in f:
        line = line.split('\t')[-1]
        word_list = clean_and_tokenize(line[:-1])
        pos = pos_tag(word_list)
        for word, typ in pos:
            if typ == 'NNP':
                np_freqs[day - 16][word.lower()] += 1


def main():
    from_what = 'tweets'
    summary_name = 'noun_pos_freqs'
    statscollector.collect_stats(init, from_what, process_file, summary_name)


if __name__ == '__main__':
    main()
