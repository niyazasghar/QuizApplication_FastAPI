from fastapi import FastAPI
import models
from database import engine
from routers import question, auth, users, admin

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QuizApplication using FastAPI",
    description="API for managing Quiz Questions , Authentication",
    version="3"
)

app.include_router(question.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)