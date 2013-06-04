#!/usr/bin/env python
# -*- coding: utf-8 -*-
PATH = '/Users/mquezada/Tesis/dataset/'

import sys
sys.path.append(PATH)

import files

keywords = [
    'boston',
    'marathon'
]

count = 0


def process_file(f, day):
    global count
    out = open('./tmp/tweets_filtered.txt', 'a')
    for line in f:
        tweet = line.split('\t')[-1]
        for kw in keywords:
            if kw in tweet.lower():
                count += 1
                out.write(line)
    out.close()


def main():
    files.read('tweets', process_file)
    print 'total lines:', count


if __name__ == '__main__':
    main()
