#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statscollector
import words
import string

words_frequencies = []


def process_file(f, day):
    for line in f:
        line = line.split('\t')[-1]
        word_list = words.clean_and_tokenize(line[:-1])
        word_list = map(string.lower, word_list)
        for word in word_list:
            words_frequencies[day][word] += 1


def init(counters):
    global words_frequencies
    words_frequencies = counters


def main():
    from_what = 'other'
    path = '/Users/mquezada/Tesis/filter/files/'
    summary_name = 'word_freqs_boston'
    statscollector.collect_stats(init, from_what, process_file, summary_name, other_path=path)


if __name__ == '__main__':
    main()
