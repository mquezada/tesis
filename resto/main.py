
def count_lines(filename):
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            total += 1
    return total


def read_files_in(folder, f):
    import os
    os.chdir(folder)

    for filename in os.listdir(folder):
        f(filename)


def save_counts(day, key):
    def process_file(filename):
        if filename == '.DS_Store':
            return
        print filename
        c = count_lines(filename)

        identifier = '_'.join(filename.split('_')[2:4])
        if identifier not in totals:
            totals[identifier] = dict.fromkeys(keys)
        totals[identifier][key] = c

    return process_file

import operator

PATH = '/Users/mquezada/Tesis/Boston Dataset'
tweets, urls, hashtags, users, mentions = 'tweets', 'urls', 'hashtags', 'users', 'mentions'
keys = [tweets, urls, hashtags, users, mentions]
totals = {}


for day in range(16, 23):
    folder = PATH + '/201304' + str(day) + '/Tweets'
    read_files_in(folder, save_counts(day, tweets))

    folder = PATH + '/201304' + str(day) + '/E_Hashtags'
    read_files_in(folder, save_counts(day, hashtags))

    folder = PATH + '/201304' + str(day) + '/E_URLs'
    read_files_in(folder, save_counts(day, urls))

    folder = PATH + '/201304' + str(day) + '/E_UserRefs'
    read_files_in(folder, save_counts(day, mentions))

    folder = PATH + '/201304' + str(day) + '/Users'
    read_files_in(folder, save_counts(day, users))

totals = sorted(totals.items(), key=operator.itemgetter(0))
with open(PATH + '/summary.txt', 'w') as f:
    f.write('#window\thashtags\tmentions\ttweets\turls\tusers\n')
    for win, data in totals:
        f.write(win)
        meds = sorted(data.items(), key=operator.itemgetter(0))
        for _, num in meds:
            f.write('\t' + str(num))
        f.write('\n')
