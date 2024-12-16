from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from models import Question
from routers.auth import get_current_user
from schemas import Question_Request, db_dependency, Question_Response, get_db


router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", response_model=List[Question_Response])
def get_questions(user: user_dependency,db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    questions = db.query(Question).filter(Question.owner_id == user.get('id')).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return questions

@router.get("/{question_id}", response_model=Question_Response)
def get_question_by_id(user: user_dependency,db: Session = Depends(get_db), question_id: int = 0):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    question = db.query(Question).get(question_id).filter(Question.owner_id == user.get('id'))
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.post("/", response_model=Question_Response, status_code=status.HTTP_201_CREATED)
def add_question(user: user_dependency,db: Session = Depends(get_db), question: Question_Request = ...):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    db_question = Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


@router.put("/{question_id}", response_model=Question_Response, status_code=status.HTTP_200_OK)
def update_question(user: user_dependency,question_id: int, db: Session = Depends(get_db), question: Question_Request = ...):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    db_question = db.query(Question).filter(Question.question_id == question_id).filter(Question.owner_id == user.get('id')).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Update fields
    db_question.question_text = question.question_text
    db_question.correct_answer = question.correct_answer
    db_question.option_1 = question.option_1
    db_question.option_2 = question.option_2
    db_question.option_3 = question.option_3
    db_question.option_4 = question.option_4
    db_question.subject = question.subject

    db.commit()
    db.refresh(db_question)
    return db_question


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(user: user_dependency, question_id: int, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    db_question = db.query(Question).filter(Question.question_id == question_id).filter(Question.owner_id == user.get('id')).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(db_question)
    db.commit()
    return