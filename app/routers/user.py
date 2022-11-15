from app.routers.schemas import User, UpdateUser
from app.db.database import get_db
from app.db import models

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/")
def create_users(user: User, db: Session = Depends(get_db)):
    users = user.dict()
    new_user = models.User(
        username=users["username"],
        password=users["password"],
        name=users["name"],
        surname=users["surname"],
        age=users["age"],
        tel=users["tel"],
        email=users["email"],
        address=users["address"],
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "Successful"


@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    res_user = db.query(models.User).all()
    return res_user


@router.post("/id/{user_id}")
def get_user_id(user_id: int, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not res_user:
        return "User not found !"
    return {"Response:": res_user}


@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.id == user_id)
    if not res_user.first():
        return "User not found !"
    res_user.delete(synchronize_session=False)
    db.commit()
    return {"Response:": "User deleted successful"}


@router.patch("/update/{user_id}")
def update_user(user_id: int, updateUser: UpdateUser, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.id == user_id)
    if not res_user:
        return {"Response": "User not found."}
    res_user.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {
        "Response": "User updating successful.",
    }
