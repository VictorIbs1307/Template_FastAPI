
from src.app.schemas.user import UserListResponse, UserBase
from src.app.queries.user_queries import UserQueries
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.core.db import get_db



class UserRouter(APIRouter):
    def __init__(self, queries: UserQueries):
        super().__init__()
        
        self._queries = queries
        self.get("", response_model=UserListResponse)(self.get_all_users)
        
    async def get_all_users(self, db:Session = Depends(get_db)) -> UserListResponse:
        db_users = await self._queries.get_all_users(db=db)
        fetched_users = []
        for user in db_users:
            fetched_users.append(UserBase.validate_model(user))
        return UserListResponse(user_list=fetched_users)
