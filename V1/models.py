from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String(800))
    correct_answer = Column(String(255))
    option_1 = Column(String(255))
    option_2 = Column(String(255))
    option_3 = Column(String(255))
    option_4 = Column(String(255))
    subject = Column(String(255))

class user(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    hashed_password = Column(String(255))
    firstname = Column(String(255))
    lastname = Column(String(255))
    role = Column(String(255))
    isActive = Column(Boolean , default=True)
