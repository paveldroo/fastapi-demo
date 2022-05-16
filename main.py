from typing import Optional

from fastapi import FastAPI

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
