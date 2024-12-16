from typing import List
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from models import Question
from schemas import Question_Request, db_dependency, Question_Response, get_db

# Initialize the router with a prefix and tags
router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.get("/", response_model=List[Question_Response])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return questions

@router.get("/{question_id}", response_model=Question_Response)
def get_question_by_id(db: Session = Depends(get_db), question_id: int = 0):
    question = db.query(Question).get(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

# API to add a new question
@router.post("/", response_model=Question_Response, status_code=status.HTTP_201_CREATED)
def add_question(db: Session = Depends(get_db), question: Question_Request = ...):
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

# API to update an existing question by ID
@router.put("/{question_id}", response_model=Question_Response, status_code=status.HTTP_200_OK)
def update_question(question_id: int, db: Session = Depends(get_db), question: Question_Request = ...):
    db_question = db.query(Question).filter(Question.question_id == question_id).first()
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

# API to delete a question by ID
@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    db_question = db.query(Question).filter(Question.question_id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(db_question)
    db.commit()
    return  # No content for 204
