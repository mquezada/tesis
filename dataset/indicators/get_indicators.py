#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import twitter
import simplejson as json


def get_social_indicators(ids_list):
    indicators_list = []
    raw_tweets = []
    for resp in twitter.yield_tweets(ids_list):
        if resp.ok:
            data = resp.json()
            indicators = (
                data['id_str'],
                data['favorite_count'],
                data['retweet_count'],
                data['truncated'],
                data['user']['name'],
                data['user']['geo_enabled'],
                data['user']['url'],
                data['user']['verified'],
            )
            indicators_list.append(indicators)
            raw_tweets.append(data)
    return indicators_list, raw_tweets


def save_to_file(indicators_list, raw_tweets):
    with open('./tmp/raw_tweets.txt', 'w') as f:
        f.write(json.dumps(raw_tweets))

    with open('./tmp/indicators.txt', 'w') as f:
        for ind in indicators_list:
            for item in ind[:-1]:
                to_write = str(item).replace('\t', ' ')
                f.write(to_write + '\t')
            f.write(str(ind[-1]) + '\n')


def main():
    ids = [
        '324699556963041281',
        '324699573736054784',
        '342062866821689344',
        '342038519339950080',
        '342061259396628480',
        '342064437362049024'
    ]
    indicators_list, raw_tweets = get_social_indicators(ids)
    save_to_file(indicators_list, raw_tweets)


if __name__ == '__main__':
    main()
