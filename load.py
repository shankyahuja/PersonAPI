import json
from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

with open("data.json", "r") as f:
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