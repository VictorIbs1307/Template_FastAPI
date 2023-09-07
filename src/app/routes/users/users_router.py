import fastapi
# from fastapi import Depends
# from src.app.queries import crud
# from sqlalchemy.orm import Session
# from src.app.app import app, get_db
from src.app.models.users.responses import UserListResponse
from src.app.services.users.user_service import UserService
from src.app.core import service_container


router = fastapi.APIRouter()
USER_SERVICE = fastapi.Depends(service_container.user_service)

@router.get(path="/", response_model=UserListResponse)
async def get_user(service: UserService = USER_SERVICE) -> UserListResponse:
    return await service.get_users()
    # return crud.get_user(db=db, id=id)

# #define endpoint
# @app.post("/create_user")
# def create_user(first_name:str, last_name:str, age:int, db:Session = Depends(get_db)):
#     user = crud.create_user(db=db, first_name=first_name, last_name=last_name, age=age)
# ##return object created
#     return {"user": user}

# #get/retrieve user 
# @app.get("/get_user/{id}/") #id is a path parameter


# #get/retrieve user 
# @app.get("/get_user/{id}/") #id is a path parameter
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = crud.get_user(db=db, id=id)
#     return user

# @app.put("/update_user/{id}/") #id is a path parameter
# def update_user(id:int, first_name:str, last_name:str, age:int, db:Session=Depends(get_db)):
#     db_user = crud.get_user(db=db, id=id)
#     if db_user:
#         updated_user = crud.update_user(db=db, id=id, first_name=first_name, last_name=last_name, age=age)
#         return updated_user
#     else:
#         return {"error": f"User with id {id} does not exist"}
    
# @app.delete("/delete_user/{id}/") #id is a path parameter
# def delete_user(id:int, db:Session=Depends(get_db)):
#     db_user = crud.get_user(db=db, id=id)
#     if db_user:
#         return crud.delete_user(db=db, id=id)
#     else:
#         return {"error": f"User with id {id} does not exist"}