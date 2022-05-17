from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app import models, schemas, oauth2
from app.database import get_db
from app.repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get('/{blog_id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(blog_id, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {blog_id} is not available')
    return blog


@router.delete('/{blog_id}')
def delete_blog(blog_id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(blog_id, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(request, blog_id, db)
