from pydantic import BaseModel

#create Pydantic model (schema) for pydantic to orm (database) model mapping
class Person(BaseModel):
    id: int
    first_name: str = None
    last_name: str = None
    email: str = None
    gender: str
    ip_address: str = None
    country_code: str
    
    class Config:
        # config to make it compatible with orm model
        orm_mode = True
