from fastapi import FastAPI
from src.app.queries.user_queries import UserQueries
from src.app.core.base import Base
from src.app.routes.users_router import UserRouter
from src.app.core.db import engine

class BaseApi:
    def __init__(self, title: str, version: str) -> None:
        self._app: FastAPI = FastAPI(title=title, version=version)
        self._register_user_routes()

    def _register_user_routes(self) -> None:
        userQuries = UserQueries()
        userRouter = UserRouter(queries=userQuries) 
        self._app.include_router(router=userRouter, prefix="/users")

    def get_app(self) -> FastAPI:
        self._create_tables()
        return self._app
    
    def _create_tables(self) -> None:         
	    Base.metadata.create_all(bind=engine)