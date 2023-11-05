from fastapi import FastAPI
from src.app.core.db import DB
from src.app.queries.user_queries import UserQueries

from src.app.routes.users_router import UserRouter


class BaseApi:
    def __init__(self, title: str, version: str) -> None:
        self._app: FastAPI = FastAPI(title=title, version=version)
        self._register_user_routes()
        self._init_DB()

    def _register_user_routes(self) -> None:
        userQuries = UserQueries()
        userRouter = UserRouter(queries=userQuries) 
        self._app.include_router(router=userRouter, prefix="/users")
    
    def get_app(self) -> FastAPI:
        return self._app

    def _init_DB(self) -> None:         
	    DB.init_app(app=self._app)
     