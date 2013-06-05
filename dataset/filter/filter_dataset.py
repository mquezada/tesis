#!/usr/bin/env python
# -*- coding: utf-8 -*-

from files import files

kws = [
    'boston',
    'marathon'
]

tweets = []


def process_file(f, day):
    for line in f:
        tokens = line.split('\t')
        if len(tokens) < 3:
            continue
        tweet = tokens[-1]
        id = tokens[1]
        lang = tokens[-3]
        for kw in kws:
            if kw in tweet.lower():
                tweets.append((id, lang, tweet))


def filter_by_keywords(keywords=kws):
    files.read('tweets', process_file)
    return tweets


def main():
    files.read('tweets', process_file)


if __name__ == '__main__':
    main()
