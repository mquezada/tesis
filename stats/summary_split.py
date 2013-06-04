#!/usr/bin/env python
# -*- coding: utf-8 -*-

PATH = '/Users/mquezada/Tesis/stats/data'

keys = ['hashtags', 'mentions', 'tweets', 'urls', 'users']

days = [
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
    dict.fromkeys(keys, 0),
]

with open(PATH + '/summary.txt', 'r') as f:
    for line in f:
        if '#' in line:
            continue
        tokens = line.split('\t')
        date = tokens[0].split('_')
        day = int(date[0][-2:])

        hashtags = int(tokens[1])
        mentions = int(tokens[2])
        tweets = int(tokens[3])
        urls = int(tokens[4])
        users = int(tokens[5])

        days[day - 16]['hashtags'] += hashtags
        days[day - 16]['mentions'] += mentions
        days[day - 16]['tweets'] += tweets
        days[day - 16]['urls'] += urls
        days[day - 16]['users'] += users

with open(PATH + '/summary_by_day.txt', 'w') as f:
    print >> f, '#day\thashtags\tmentions\ttweets\turls\tusers'
    d = 16
    for data in days:
        f.write(str(d))
        for _, num in sorted(data.items(), key=lambda x: x[0]):
            f.write('\t' + str(num))
        f.write('\n')
        d += 1
