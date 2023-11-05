from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int

    model_config = ConfigDict(from_attributes=True)
    
class UserResponse(UserBase):
    pass
    
class  UserListResponse(BaseModel):
    user_list: list[UserResponse]