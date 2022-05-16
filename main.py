from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'First {limit} published blog records from db'}
    else:
        return {'data': f'First {limit} blog records from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog records'}


@app.get('/blog/{blog_id}')
def about(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int, limit=10):
    return {'data': ['1', '2']}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title {blog.title}'}
