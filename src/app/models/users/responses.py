from sqlalchemy import Column, Integer, String
from src.app.core.db import Base
from pydantic import BaseModel


# model/table
class User(Base):
    __tablename__ = "user"

    # fields 
    id = Column(Integer,primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    
class  UserListResponse(BaseModel):
    user_list: list[UserResponse]