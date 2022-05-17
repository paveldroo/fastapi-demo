from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, oauth2
from app.database import get_db
from app.repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request, db)


@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get(user_id, db)
