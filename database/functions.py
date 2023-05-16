from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Boolean, MetaData
from models.student import Student

from config.hosts import *

class ORM:
    def __init__(self):
        self.engine = create_engine(DBSTRING)  
        
        self.meta = MetaData(self.engine)  

    def CreateTable(self):
        self.table = Table('users', self.meta, 
                       Column('telegram_id', String),
                       Column('group', String),
                       Column('is_set_group',Boolean)) 
        
        self.meta.create_all(self.engine)
        
    def GetSession(self):
        Session = sessionmaker(self.engine)
        return Session()
    
    def AddStudent(self, telegram_id_, group_):
        session = self.GetSession()
        session.add(Student(telegram_id=telegram_id_, group=group_))
        session.commit()

    def GetStudent(self, telegram_id_):
        session = self.GetSession()
        return session.scalars(select(Student).filter_by(telegram_id=telegram_id_)).first()
    
        
    def UpdateStudentGroup(self, telegram_id_, group_):
        session = self.GetSession()
        session.query(Student).filter(Student.telegram_id==telegram_id_).update({'group': group_})
        session.commit()

        
    def UpdateIsSetGroup(self, telegram_id_, is_set_group_):
        session = self.GetSession()
        session.query(Student).filter(Student.telegram_id==telegram_id_).update({'is_set_group': is_set_group_})
        session.commit()