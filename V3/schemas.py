from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel
from database import SessionLocal
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]



class Question_Request(BaseModel):
    question_text: str
    correct_answer: str
    option_1: str
    option_2: str
    option_3: str
    option_4: str
    subject: str

    class Config:
        orm_mode = True

class Question_Response(BaseModel):
    question_id: int
    question_text: str
    correct_answer: str
    option_1: str
    option_2: str
    option_3: str
    option_4: str
    subject: str

    class Config:
        orm_mode = True

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

    class Config:
        orm_mode = True








