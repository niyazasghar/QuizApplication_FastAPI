from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Question
from database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/view_question", status_code=status.HTTP_200_OK)
async def view_all_Question(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Question).all()


@router.delete("/question/{ques_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_Question(user: user_dependency, db: db_dependency, ques_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(Question).filter(Question.question_id == ques_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Question not found.')
    db.query(Question).filter(Question.question_id == ques_id).delete()
    db.commit()



