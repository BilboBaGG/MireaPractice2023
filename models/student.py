from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
   __tablename__ = 'users'
   
   telegram_id = Column(String, primary_key=True)
   group = Column(String)
   is_set_gruop = Column(Boolean)