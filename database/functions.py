from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, MetaData
import time
from models.student import Student

from config.hosts import *

class ORM:
    def __init__(self): # Creating database
        time.sleep(3)
        self.engine = create_engine(DBSTRING)  
        
        self.meta = MetaData(self.engine)  

        self.table = Table('users', self.meta, 
                       Column('id', String),
                       Column('group', String)) # Create table class
        
        self.meta.create_all(self.engine)


        session = self.getSession()

        session.add(Student(id="19123", group="БИСО-03-22"))
        session.commit()

        print(session.scalars(select(Student).filter_by(id="19123")).first().group)

        
    def getSession(self):
        Session = sessionmaker(self.engine)
        return Session()