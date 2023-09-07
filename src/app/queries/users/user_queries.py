from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List, Type, Union, Any
from src.app.core.db import get_db
from src.app.models.users.responses import User


class UserQueries:
    def __init__(self, db:Session = Depends(get_db)) -> None:
        self.db = db
            
    async def get_all_users(self) -> Any:
        test = self.db.query(User).all()
        print(test)
        return test