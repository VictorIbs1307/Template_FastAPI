from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int
