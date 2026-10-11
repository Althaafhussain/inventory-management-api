import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

#DATABASE_URL = "sqlite:///./inventory.db"
DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("POSTGRESQL_DATABASE_URL is not set in .env")

engine = create_engine(
    DATABASE_URL
)

SessionLocal =  sessionmaker(
    autocommit=False, 
    autoflush = False, 
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()