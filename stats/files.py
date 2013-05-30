#!/usr/bin/env python
# -*- coding: utf-8 -*-


PATH = '/Users/mquezada/Tesis/Boston Dataset'
entities = {
    'tweets': '/Tweets',
    'hashtags': '/E_Hashtags',
    'urls': '/E_URLs',
    'mentions': '/E_UserRefs',
    'users': '/Users',
    'index': '/Index'
}


def read(entity, process_file):
    for day in range(16, 23):
        path = PATH + '/201304' + str(day) + entities[entity]
        read_files_in(path, process_file, day)


def read_files_in(folder, process_file, day):
    import os
    for filename in os.listdir(folder):
        if filename == '.DS_Store':
            continue
        abs_file = folder + '/' + filename
        print 'Processing file: ' + abs_file
        with open(abs_file, 'r') as f:
            process_file(f, day)
