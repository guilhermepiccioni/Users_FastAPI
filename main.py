import uvicorn

from app.routers.user import router
from app.db.database import ENGINE
from app.db.models import Base
from fastapi import FastAPI


def create_database():
    Base.metadata.create_all(bind=ENGINE)


create_database()


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
