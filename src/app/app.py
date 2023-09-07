from fastapi import FastAPI
from src.app.routes.users import users_router


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(title="placeholder")
    return _register_routes(app)
    
def _register_routes(app: FastAPI) -> FastAPI:
    app.include_router(router=users_router.router, prefix="/users")
    # app.include_router(router=, prefix=)
    # app.include_router(router=, prefix=)
    # app.include_router(router=, prefix=)
    return app
