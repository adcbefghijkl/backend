from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from app.user import schema, crud

router = APIRouter(
    prefix="/api/users",
)


@router.get("/", response_model=list[schema.User])
def user_list(db: Session = Depends(get_db)):
    _user_list = crud.get_user_list(db)
    return _user_list


@router.get("/{user_id}", response_model=schema.User)
def user_detail(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    return user


@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: schema.UserCreate, db: Session = Depends(get_db)):
    crud.create_user(db, _user_create)


@router.put("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def user_modify(user_id: int, _user_modify: schema.UserModify, db: Session = Depends(get_db)):
    crud.modify_user(db, user_id=user_id, user_modify=_user_modify)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def user_delete(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id=user_id)