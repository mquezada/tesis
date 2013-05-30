#!/usr/bin/env python
# -*- coding: utf-8 -*-

from files import *

from urlparse import urlparse
from collections import Counter
from operator import itemgetter
import os


urls = {}
domain_freqs = [
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
]


def process_file(f, day):
    for line in f:
        tokens = line.split('\t')
        if len(tokens) > 3:
            pos_short = tokens[-1][:-1]
            url = pos_short
            if pos_short in urls:
                url = urls[pos_short]
            domain = urlparse(url).hostname
            domain_freqs[day - 16][domain] += 1


def init():
    with open('urls.txt', 'r') as f:
        for line in f:
            pair = line.split()
            if len(pair) < 2:
                continue
            short = pair[0]
            expanded = pair[1]

            urls[short] = expanded


def main():
    end = lambda: None
    from_what = 'urls'
    summary_name = 'domain_freqs'

if __name__ == '__main__':
    main()
