from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TwData(Base):
    __tablename__ = 'tw20130203_sb_data'

    id = Column(Integer, primary_key=True)
    tw_id = Column(String)
    tw_json = Column(String)

    def __init__(self, tw_id, tw_json):
        self.tw_id = tw_id
        self.tw_json = tw_json

    def __repr__(self):
        return "<TwData('%s','%s')>" % (self.tw_id, self.tw_json)


class TwSb(Base):
    __tablename__ = 'tw20130203_sb'

    tw_id = Column(String, primary_key=True)
    tw_user = Column(String)
    tw_code = Column(String)
    tw_timestamp = Column(String)
    tw_message = Column(String)

    def __init__(self):
        pass

    def __repr__(self):
        return "<TwSb('%s','%s','%s','%s','%s')>" % (self.tw_id, self.tw_user, self.tw_code, self.tw_timestamp, self.tw_message)


db = create_engine('postgresql://postgres:password@localhost:5432/bursts')
Session = sessionmaker(db)
