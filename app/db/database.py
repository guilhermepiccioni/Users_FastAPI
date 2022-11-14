from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@postgresql_db:5432/fast_db"
ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
