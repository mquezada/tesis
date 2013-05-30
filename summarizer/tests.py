from sqlalchemy import *
from nltk.stem import SnowballStemmer
import text_utils
from ttp import ttp

twitter_parser = ttp.Parser()
stemmer = SnowballStemmer('english')
engine = create_engine('postgresql://postgres:password@localhost:5432/bursts')
db = engine.connect()

results = db.execute('select * from tw20130203_sb limit 100')

# (u'298276595150499841', u'239211968', u'200', u'20130204 03:47:36 +0000', u'<<<text>>>')

rows = {}
for row in results:
    text = row['tw_message']
    id = row['tw_id']
    text = text_utils.strip_accents(text)
    text = text_utils.remove_stopwords(text)
    text = ' '.join([stemmer.stem(token) for token in text.split()])
    rows.update({id: text})

# eg. u'298276221832282112': u'raaaaaven superbowl2013'
print rows



def get_tweets(rows):
    pass

def save_data(data):
    pass


# bug de ttp
"""
>>> s = 'RT @waxkun: hola @cuerti http://t.co/asdsad?qwe=1&asd=2&ddsa#das @uiop'
>>> r = p.parse(s)
>>> r.urls
[('http://t.co/asdsad?qwe=1&asd=2&ddsa#das', (25, 64))]
>>> r.urls
[('http://t.co/asdsad?qwe=1&asd=2&ddsa#das', (25, 64))]
>>> r.users
[('waxkun', (3, 10)), ('cuerti', (17, 24)), ('uiop', (115, 120))]
>>> len(s)
70
>>> s = 'RT @waxkun: hola @cuerti http://t.co/asdsad @uiop'
>>> r = p.parse(s)
>>> r.urls
[('http://t.co/asdsad', (25, 43))]
>>> r.users
[('waxkun', (3, 10)), ('cuerti', (17, 24)), ('uiop', (77, 82))]
"""
from ttp import ttp
def clean(text):
    p = ttp.Parser(include_spans=True)
    r = p.parse(text)
    result = text
    for user in r.users:
        init = user[1][0]
        end = user[1][1]
        result = result.replace(result[init:end], ' ' * (end-init))
    print result


"""
estrategia:
hacer una pasada por los tweets deseados
-- obtener su info de twitter (5s)
-- limpiar, obtener datos deseados, guardar en tabla en db
-- profit

con esto, *solo bastaria* sacar los datos de la db
y hacer el resumen a partir de estos

datos deseados:
- texto (limpio)
- # retweets
- # favs
- usuario verificado
- etc.. (ver indicadores sociales)

luego, otra pasada sobre un evento (=filas de la nueva tabla)
para generar vectores tf-idf (guardar en db?)
-- generar resumen
"""
