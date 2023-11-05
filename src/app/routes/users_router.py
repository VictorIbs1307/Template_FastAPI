
from src.app.db_models.user import User
from src.app.schemas.user import UserListResponse, UserBase
from src.app.queries.user_queries import UserQueries
from fastapi import APIRouter


class UserRouter(APIRouter):
    def __init__(self, queries: UserQueries):
        super().__init__()
        
        self._queries = queries
        self.get("", response_model=UserListResponse)(self.get_all_users)
        
    async def get_all_users(self) -> UserListResponse:
        db_users: list[User] = await self._queries.get_all_users()
        return UserListResponse(user_list=[UserBase.model_validate(db_user) for db_user in db_users])
