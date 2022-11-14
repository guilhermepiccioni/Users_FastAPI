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
    address: Optional[str]
    create_user = datetime.now()
