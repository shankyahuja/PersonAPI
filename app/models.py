from sqlalchemy import Column, Integer, String

from .database import Base

class Person(Base):
    #name of the table to use in the database
    __tablename__ = "persons"

    #create model class attributes
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(String)
    ip_address = Column(String)
    country_code = Column(String)