from datetime import datetime

from sqlalchemy import Column, String, DateTime, LargeBinary
from sqlalchemy import Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mptt.mixins import *

engine = create_engine('postgresql://postgres:Ugesh@1995@localhost:5432/BNY')
Base = declarative_base()
id_seq = Sequence('user_settings_id_seq')


class UserSettings(Base):
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    user_settings_type = Column(String, nullable=False)
    content = Column(LargeBinary, nullable=False)
    file_name = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_time = Column(DateTime, nullable=True)

    def __init__(self, user_id, user_settings_type, content, file_name, created_time='', updated_time = ''):
        self.user_id = user_id
        self.user_settings_type = user_settings_type
        self.content = content
        self.file_name = file_name

    def __str__(self):
        return "(%s, %s, %s, %s, %s, %s)" % (
            self.user_id, self.user_settings_type, self.content, self.file_name,
            self.created_time, self.updated_time)

    def __repr__(self):
        return "(%s, %s, %s, %s, %s, %s)" % (
            self.user_id, self.user_settings_type, self.content, self.file_name,
            self.created_time, self.updated_time)


Base.metadata.create_all(engine)
