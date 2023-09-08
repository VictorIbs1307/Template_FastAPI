from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int

class UserResponse(UserBase):
    pass
    
class  UserListResponse(BaseModel):
    user_list: list[UserResponse]