from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
# from sqlalchemy.schema import ForeignKey
# from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    tel = Column(String)
    email = Column(String)
    address = Column(String)
    create_user = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # offer = relationship("Offer", backref="user", cascade="delete, merge")


# class Offer(Base):
#     __tablename__ = "offers"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
#     offer = Column(Integer)
#     products_offer = Column(Integer)
