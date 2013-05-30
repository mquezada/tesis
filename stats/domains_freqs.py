#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statscollector

from tldextract import extract


urls = {}
domain_freqs = []


def process_file(f, day):
    for line in f:
        tokens = line.split('\t')
        if len(tokens) > 3:
            pos_short = tokens[-1][:-1]
            url = pos_short
            if pos_short in urls:
                url = urls[pos_short]
            ex = extract(url)
            domain = ex.domain + '.' + ex.tld
            domain_freqs[day - 16][domain] += 1


def init(counters):
    global domain_freqs
    domain_freqs = counters
    with open('urls.txt', 'r') as f:
        for line in f:
            pair = line.split()
            if len(pair) < 2:
                continue
            short = pair[0]
            expanded = pair[1]

            urls[short] = expanded


def main():
    from_what = 'urls'
    summary_name = 'domain_freqs'

    statscollector.collect_stats(init, from_what, process_file, summary_name)


if __name__ == '__main__':
    main()
