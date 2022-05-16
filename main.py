from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog records'}


@app.get('/blog/{blog_id}')
def about(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int):
    return {'data': ['1', '2']}
