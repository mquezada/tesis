# -*- coding: utf-8 -*-

"""
    returns TwSb objects
    dates in format "YYYY-MM-DD HH:MM:SS"
"""


def select_rows(init_date, end_date, limit=100):
    import model
    session = model.Session()
    limit_str = "limit " + str(limit)
    if limit == 0:
        limit_str = ""
    rows = session.query(model.TwSb).from_statement("""
        select * from tw20130203_sb
        where
            to_timestamp(tw_timestamp, 'YYYYMMDD HH24:MI:SS') < :end_date
            and
            to_timestamp(tw_timestamp, 'YYYYMMDD HH24:MI:SS') > :init_date
        order by tw_timestamp
        %s;
    """ % limit_str).params(init_date=init_date, end_date=end_date).all()
    return rows
