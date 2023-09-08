from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int
    
class  UserListResponse(BaseModel):
    user_list: list[UserResponse]