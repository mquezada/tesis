# -*- coding: utf-8 -*-
import unicodedata, string
s = unicode('á è ì k ñ', 'UTF-8')


def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()





print repr(s)
print remove_accents(s)