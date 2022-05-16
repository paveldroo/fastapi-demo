from fastapi import FastAPI

from app import schemas

app = FastAPI()


@app.post('/blog')
def create(blog: schemas.Blog):
    return {'title': blog.title, 'body': blog.body}
