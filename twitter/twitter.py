#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1
import settings as k
import time


auth = OAuth1(k.OAUTH_API_KEY, k.OAUTH_API_SECRET, k.USER_OAUTH_TOKEN, k.USER_OAUTH_TOKEN_SECRET)


def get_tweet(id=None):
    url = 'https://api.twitter.com/1.1/statuses/show.json?id=' + id
    response = requests.get(url, auth=auth)

    return response


def yield_tweets(ids_list):
    for id in ids_list:
        yield get_tweet(id)
        time.sleep(5)
