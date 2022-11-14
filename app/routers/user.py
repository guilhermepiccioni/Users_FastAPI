from app.routers.schemas import User
from app.db.database import get_db
from app.db import models

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


users_all = []


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    db.query(models.User).all()
    # print(data)
    return users_all


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
        address=users["address"],
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "Successful"


@router.post("/id/{user_id}")
def get_user_id(user_id: int, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not res_user:
        return "User not found !"
    return {"Response:": res_user}


@router.post("/name/{user_name}")
def get_user_name(user_name: str, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.name == user_name).first()
    if not res_user:
        return "User not found !"
    return {"Response:": res_user}


@router.post("/name/{user_username}")
def get_user_username(user_username: str, db: Session = Depends(get_db)):
    res_user = db.query(models.User).filter(models.User.username == user_username).first()
    if not res_user:
        return "User not found !"
    return {"Response:": res_user}


@router.delete("/delete/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_all):
        if user.id == user_id:
            users_all.pop(index)
            return user, {
                "Response": "User deleted successful."
            }
    return {"Response": "User not found."}


@router.put("/update/{user_id}")
def update_user(user_id: int, updateUser: User):
    for index, user in enumerate(users_all):
        if user.id == user_id:
            users_all[index].id = updateUser.dict()["id"]
            users_all[index].name = updateUser.dict()["name"]
            users_all[index].surname = updateUser.dict()["surname"]
            users_all[index].age = updateUser.dict()["age"]
            users_all[index].tel = updateUser.dict()["tel"]
            users_all[index].address = updateUser.dict()["address"]
            return user, {
                "Response": "User updating successful."
            }
    return {"Response": "User not found."}