from fastapi import FastAPI
from src.app.core.base import Base
from src.app.routes import users_router
from src.app.core.db import engine


def _register_routes(app: FastAPI) -> FastAPI:
    app.include_router(router=users_router.router, prefix="/users")
    return app


def create_tables():         
	Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(title="my_application",version="v1.0.0")
    create_tables()
    return _register_routes(app)
    

