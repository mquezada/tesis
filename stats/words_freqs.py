#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statscollector
from words import *

words_frequencies = []


def process_file(f, day):
    for line in f:
        line = line.split('\t')[-1]
        word_list = clean_and_tokenize(line[:-1])
        for word in word_list:
            words_frequencies[day - 16][word] += 1


def init(counters):
    global words_frequencies
    words_frequencies = counters


def main():
    from_what = 'tweets'
    summary_name = 'word_freqs'
    statscollector.collect_stats(init, from_what, process_file, summary_name)


if __name__ == '__main__':
    main()
