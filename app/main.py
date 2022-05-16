from fastapi import FastAPI

from app import schemas, models
from app.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/blog')
def create(blog: schemas.Blog):
    return {'title': blog.title, 'body': blog.body}
