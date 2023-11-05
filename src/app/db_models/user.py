
from sqlalchemy import Column, Integer, String
from src.app.core.base import Base

# model/table
class User(Base):
    __tablename__ = "user"

    # fields 
    id = Column(Integer,primary_key=True, index=True)
    email = Column(String(20))
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    