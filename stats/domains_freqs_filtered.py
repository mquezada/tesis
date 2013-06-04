#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statscollector

from tldextract import extract

import re

urls_tw_sexp = {}
urls_sexp_exp = {}
domain_freqs = []

url_pattern = re.compile('(http:\/\/.*?/[a-zA-Z0-9]*)')

keywords = [
    'boston',
    'marathon'
]


def process_file(f, day):
    for line in f:
        tweet = line.split('\t')[-1][:-1]
        for kw in keywords:
            if kw in tweet.lower():
                urls = url_pattern.findall(tweet)
                print urls
                for url in urls:
                    semi_exp = urls_tw_sexp[url]
                    exp_or_semi = urls_sexp_exp[semi_exp]
                    ex = extract(exp_or_semi)
                    domain = ex.domain + '.' + ex.tld
                    domain_freqs[day - 16][domain] += 1


def init(counters):
    global domain_freqs
    domain_freqs = counters
    with open('./data/triples_urls.txt', 'r') as f:
        for line in f:
            triple = line.split()
            short = triple[0]
            expanded_by_tw = triple[1]
            expanded = triple[2]

            urls_tw_sexp[short] = expanded_by_tw
            urls_sexp_exp[expanded_by_tw] = expanded


def main():
    from_what = 'tweets'
    summary_name = 'domain_freqs_filtered'

    statscollector.collect_stats(init, from_what, process_file, summary_name)


if __name__ == '__main__':
    main()
