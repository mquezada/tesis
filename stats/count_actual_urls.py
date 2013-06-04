#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""cuenta la cantidad de urls basado en la cantidad
de urls incluidas en los tweets (mensajes), no en
los archivos de urls, y lo compara con triples_urls.txt"""

import files
import re


url_tw_count = 0
url_pattern = re.compile('(http:\/\/.*?/[a-zA-Z0-9]*)')


def process_file(f, day):
    global url_tw_count
    for line in f:
        tweet = line.split('\t')[-1][:-1]
        urls = url_pattern.findall(tweet)
        for url in urls:
            url_tw_count += 1


url_files_count = 0


def process_file2(f, day):
    global url_files_count
    for line in f:
        tokens = line.split('\t')
        if len(tokens) > 3:
            url_files_count += 1


def main():
    files.read('tweets', process_file)
    files.read('urls', process_file2)

    triples = 0
    with open('./data/triples_urls.txt', 'r') as f:
        for line in f:
            triples += 1

    print 'cantidad de urls en los tweets', url_tw_count
    print 'cantidad de urls en archivos de urls', url_files_count
    print 'cantidad de urls en triples', triples


if __name__ == '__main__':
    main()
