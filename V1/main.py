from fastapi import FastAPI
import models
from database import engine
from routers import question

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz FastAPI",
    description="API for managing Quiz Questions",
    version="1"
)

app.include_router(question.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)