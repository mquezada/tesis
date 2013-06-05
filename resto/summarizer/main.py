from select_rows import select_rows
from select_random_rows import select_random_rows
from tweets_info_getter import get_tweets_from_rows


def main():
    #init = input('Init date: ')  # 2013-02-04 1:00
    #end = input('End date: ')  # 2013-02-04 2:00
    init = '2013-02-04 1:00'
    end = '2013-02-04 2:00'
    n = 0
    m = 4000
    rows = select_rows(init, end, limit=n)

    # select 4000 rows randomly
    nrows = select_random_rows(rows, n=m)
    get_tweets_from_rows(nrows)


if __name__ == '__main__':
    main()
