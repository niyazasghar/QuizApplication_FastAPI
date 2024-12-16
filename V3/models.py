from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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
    owner_id = Column(Integer, ForeignKey("users.id"))


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    role = Column(String(255))

