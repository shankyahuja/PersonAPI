from sqlalchemy.orm import Session
from sqlalchemy import update


from . import models, schemas

# read person details based on ID
def get_person(db: Session, id: int):

    return db.query(models.Person).filter(models.Person.id == id).first()

# insert a new person if it doesn't exist already
def create_person(db: Session, person: schemas.Person):
    #create a model instance for the data
    db_person = models.Person(id=person.id, first_name=person.first_name, last_name=person.last_name, email=person.email, gender=person.gender, ip_address=person.ip_address, country_code=person.country_code)
    #add the instance object to database session
    db.add(db_person)
    #commit the changes to the database
    db.commit()
    #refresh the instance so that it contains the new data from database
    db.refresh(db_person)
    return db_person    

#update person details if the person already exists    
def update_person(db: Session, person: schemas.Person):
    db.query(models.Person).filter(models.Person.id == person.id).update(dict(first_name=person.first_name, last_name=person.last_name, email=person.email, gender=person.gender, ip_address=person.ip_address, country_code=person.country_code),synchronize_session="fetch")
    db.commit()
    return person

# delete a person based on ID    
def delete_person(db: Session, id: int):
    x = db.query(models.Person).filter_by(id = id).first()
    print(x)
    db.delete(x)
    db.commit()
    return x
