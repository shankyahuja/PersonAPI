#Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Create a database URL for SQLAlchemy. the SQlite database file will be stored as app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"

#create a SQLAlchemy "engine"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#each instance of the below SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create Base class for database models
Base = declarative_base()