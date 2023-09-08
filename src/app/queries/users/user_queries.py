from fastapi import Depends
from sqlalchemy.orm import Session

from src.app.models.users.user import User

class UserQueries:
    async def get_all_users(self, db:Session):
        return db.query(User).all()