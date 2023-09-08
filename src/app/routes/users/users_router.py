import fastapi
# from fastapi import Depends
# from src.app.queries import crud
# from sqlalchemy.orm import Session
# from src.app.app import app, get_db
from src.app.schemas.users.responses import UserListResponse
from src.app.services.users.user_service import UserService
from src.app.core import service_container
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.core.db import get_db


router = fastapi.APIRouter()
USER_SERVICE = fastapi.Depends(service_container.user_service)

@router.get(path="/", response_model=UserListResponse)
async def get_user(service: UserService = USER_SERVICE, db:Session = Depends(get_db)) -> UserListResponse:
    return await service.get_users(db=db)




