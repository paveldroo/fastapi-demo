from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import blog, user, login

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)
