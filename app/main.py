from typing import List
import json
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKey

from sqlalchemy.orm import Session

from starlette.status import HTTP_403_FORBIDDEN

from . import crud, models, schemas
from .database import SessionLocal, engine

# api key for authentication through header
API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)    

# Dependency
def get_api_key(
    api_key_header: str = Security(api_key_header)
):

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#each request gets its own database connection session in a dependency
# Dependency
def get_db():
    db = SessionLocal()
    try:
        # yield to do something like closing the db session after sending the response
        yield db
    finally:
        db.close()

# path operation to load the full data for the first time
@app.put("/load_data/")
def load_data(db: Session = Depends(get_db), api_key: APIKey = Depends(get_api_key)):
    # drope and recreate the database table
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)

    with open("/app/data.json", "r") as f:
        person_dict = json.load(f)
    
    for row in person_dict:
        db_person = models.Person(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            gender=row["gender"],
            ip_address=row["ip_address"],
            country_code=row["country_code"]
        )
        db.add(db_person)

    db.commit()
    print("rows added successfully:")
    print(len(person_dict))

    db.close()

# to add person if it doesn't exists and update if it already exists
@app.post("/person/", response_model=schemas.Person, tags=["test"])
def add_update_person(person: schemas.Person, db: Session = Depends(get_db), api_key: APIKey = Depends(get_api_key)):

    db_person = crud.get_person(db, id=person.id)
    if db_person:
        return crud.update_person(db=db, person=person)
    return crud.create_person(db=db, person=person)

# GET method to read a person based on ID in query param
@app.get("/person/{id}", response_model=schemas.Person)

def read_person(id: int, db: Session = Depends(get_db), api_key: APIKey = Depends(get_api_key)):

    db_person = crud.get_person(db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

# delete a person based on ID    
@app.delete("/person/{id}", response_model=schemas.Person)

def delete_person(id: int, db: Session = Depends(get_db), api_key: APIKey = Depends(get_api_key)):

    db_person = crud.get_person(db, id=id)
    if db_person is None:
        raise HTTPException(status_code=400, detail="Person doesn't exists already")
    return crud.delete_person(db=db, id=id)


