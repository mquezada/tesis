#!/usr/bin/env python
# -*- coding: utf-8 -*-

from files import *

from collections import Counter
from operator import itemgetter
import os


counters = [
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
    Counter(),
]


def write_file(summary_name, day, counter):
    filename = summary_name + str(day + 16) + '.txt'
    print "Writing file %s" % filename
    PATH = '/Users/mquezada/Tesis/stats/data'
    os.chdir(PATH)

    freqs = sorted(counter.items(), key=itemgetter(1), reverse=True)
    with open(filename, 'w') as f:
        for word, freq in freqs:
            print >>f, word + '\t' + str(freq)


def collect_stats(init, from_what, process_file, summary_name, end=lambda: None, other_path=''):
    init(counters)

    read(from_what, process_file, other_path)

    for day in range(7):
        write_file(summary_name, day, counters[day])

    total = sum(counters, Counter())
    write_file(summary_name + "_total", -16, total)

    end()
