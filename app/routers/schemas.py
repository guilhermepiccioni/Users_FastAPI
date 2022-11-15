from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    age: int
    tel: str
    email: str
    address: Optional[str]
    create_user = datetime.now()


class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    name: str = None
    surname: str = None
    age: int = None
    tel: str = None
    email: str = None
    address: Optional[str] = None
