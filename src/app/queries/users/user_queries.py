from sqlalchemy.orm import Session

from typing import List, Type, Union
from src.app.models.users.responses import User


class UserQueries:
    def __init__(self, db:Session) -> None:
        self.db = db
            
    async def get_all_users(self,) -> List[User]:
        return await self.db.query(User).all()