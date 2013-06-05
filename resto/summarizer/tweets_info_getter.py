""" Obtiene la info de los tweets dados de Twitter, en formato json """
import model
import twitter
import time


def get_tweets_from_rows(rows):
    session = model.Session()
    print str(len(rows)), 'rows'
    for row in rows:
        id = row.tw_id
        text = row.tw_message
        print "Obtaining info from tweet", id, repr(text)
        data = twitter.get_tweet_json(id)
        time.sleep(5)
        if data is None:
            continue
        twdata = model.TwData(id, str(data))
        session.add(twdata)
    session.commit()
