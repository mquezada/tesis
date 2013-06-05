#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Abre el archivo de URLs del dataset de tweets
y extrae las urls "extendidas" por twitter, se reextienden
y se guardan en la carpeta ./urls
finalmente se juntan todas las urls en un solo archivo ./urls.txt
el formato del archivo generado es
<url-original> <url-extendida>\n
"""
import os
import threading
import Queue
from urls import unshorten_url
import time

PATH = '/Users/mquezada/Tesis/Boston Dataset'
init = 16
end = 23

url_list = Queue.Queue()
url_dict = {}

i = 0
for day in range(init, end):
    folder = PATH + '/201304' + str(day) + '/E_URLs/'
    for filename in os.listdir(folder):
        with open(folder + filename, 'r') as f:
            for line in f:
                tokens = line.split('\t')
                if len(tokens) > 3:
                    url = tokens[-1][:-1]
                    url_list.put(url)
                    i += 1

dat = open('data.txt', 'w')
print '%s links' % str(i)
ti = time.time()
print ti
dat.write(str(ti) + '\n')

class Writer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.f = open('urls/urls%s.txt' % str(name), 'w')

    def run(self):
        while True:
            url = self.queue.get()
            if url in url_dict:
                unshort = url_dict[url]
            else:
                unshort = unshorten_url(url)
                url_dict[url] = unshort
            if unshort is None:
                self.f.write(url + '\n')
            else:
                self.f.write('%s %s\n' % (url, unshort))
            self.queue.task_done()
    
    def join(self, timeout=None):
        threading.Thread.join(timeout)
        self.f.close()
        

for i in range(256):
    thr = Writer(url_list, i+1)
    thr.daemon = True
    thr.start()

url_list.join()

dt = time.time() - ti
print dt
dat.write(str(dt) + '\n')

outfile = open('urls.txt', 'w')
folder = '/Users/mquezada/Tesis/summarizer2/urls/'
for filename in os.listdir(folder):
    f = open(filename, 'r')
    for line in f:
        outfile.write(line)
    f.close()

outfile.close()
