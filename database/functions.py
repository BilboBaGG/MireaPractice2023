from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from config.hosts import *

class Student:
    pass

class ORM:
    def __init__(self): # Creating database
        self.db = create_engine(DBSTRING)  
        '''self.db.execute("CREATE TABLE IF NOT EXISTS tg (telegramID integer,Group text) ")

        session = self.getSession()

        session.add(Student(id="19239", group="БИСО-01-22"))
        session.commit()

        print(session.scalars(select(Student).filter_by(id="19239").first()).group)
'''
        
    def getSession(self):
        return sessionmaker(self.db)