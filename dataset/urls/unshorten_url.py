#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def unshorten_url(url, timeout=5):
    try:
        return requests.request('HEAD', url, timeout=timeout).url
    except:
        return url
