#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
genera un triple
acortada-twitter expandida-por-twitter expandida

a partir de la lista de
expandida-por-twitter expandida

usando los archivos de URLs"""

PATH = '/Users/mquezada/Tesis/stats/'

import sys
sys.path.append(PATH)

import files
import os

urls = {}
PATH = '/Users/mquezada/Tesis/stats/data/'
os.chdir(PATH)


def process_file(f, day):
    out = open(PATH + 'triples_urls.txt', 'a')
    for line in f:
        tokens = line.split('\t')
        if len(tokens) > 3:
            url_tw_exp = tokens[-1][:-1]
            url_orig = tokens[-2]
            url_exp = urls.get(url_tw_exp, url_tw_exp)
            out.write(url_orig)
            out.write(' ')
            out.write(url_tw_exp)
            out.write(' ')
            out.write(url_exp)
            out.write('\n')
    out.close()


def main():
    PATH = '/Users/mquezada/Tesis/stats/'
    with open(PATH + 'urls.txt', 'r') as urls_file:
        for line in urls_file:
            pair = line.split()
            short = pair[0]

            if len(pair) > 1:
                expanded = pair[1]
            else:
                expanded = pair[0]

            urls[short] = expanded
    files.read('urls', process_file)


if __name__ == '__main__':
    main()
