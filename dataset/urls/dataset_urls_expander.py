#!/usr/bin/env python
# -*- coding: utf-8 -*-

PATH = '/Users/mquezada/Tesis/dataset'
import sys
sys.path.append(PATH)

import files
import re
import threading
import Queue
from unshorten_url import unshorten_url

to_expand = Queue.Queue()  # urls por expandir
to_exp_count = 0
url_dict = {}  # para guardar las urls expandidas por threads
result_file = 'expanded_urls.txt'  # archivo con los resultados

url_pattern = re.compile('(http:\/\/.*?/[a-zA-Z0-9]*)')
tw_se = {}  # dict twitter t.co -> semi_expanded_url
se_ex = {}  # dict semi_expanded_url -> expandend_url | semi_expanded_url (in case of failure)


def expand():
    while True:
        url = to_expand.get()
        if url not in url_dict:
            unshort = unshorten_url(url)
            url_dict[url] = unshort
        to_expand.task_done()


def generate_urls_dicts():
    with open('urls_triples.txt', 'r') as f:
        for line in f:
            tw, se, ex = line.split()
            tw_se[tw] = se
            se_ex[se] = ex


def process_file(f, day):
    expanded_urls = open('./tmp/' + result_file, 'a')
    for line in f:
        tweet = line.split('\t')[-1][:-1]
        urls = url_pattern.findall(tweet)
        for url in urls:
            if url not in tw_se:
                global to_exp_count
                to_expand.put(url)
                to_exp_count += 1
            else:
                expanded_urls.write(url)
                expanded_urls.write(' ')
                expanded_urls.write(se_ex[tw_se[url]])
                expanded_urls.write('\n')
    expanded_urls.close()


def main():
    generate_urls_dicts()  # dicts for already unshortened urls
    files.read('tweets', process_file)  # get list of shortened urls

    print 'To expand', to_exp_count, 'urls'
    for t in range(8):  # threads
        thr = threading.Thread(target=expand)
        thr.daemon = True
        thr.start()

    to_expand.join()

    with open('./tmp/' + result_file, 'a') as f:
        for (short, expanded) in url_dict.iteritems():
            f.write('%s %s\n' % (short, expanded))


if __name__ == '__main__':
    main()
