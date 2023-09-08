
from sqlalchemy.orm import Session
from src.app.schemas.user import UserResponse, UserListResponse
from src.app.queries.user_queries import UserQueries


class UserService:
    def __init__(self, queries: UserQueries) -> None:
        self._queries = queries
        
    async def get_users(self, db: Session) -> UserListResponse:
        db_users = await self._queries.get_all_users(db=db)
        fetched_users = []
        for user in db_users:
            fetched_users.append(UserResponse.validate_model(user))
        return UserListResponse(user_list=fetched_users)
    

