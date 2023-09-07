from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from src.app.models.users.responses import User


def create_user(db:Session, first_name, last_name, age):
    """
    function to create a user model object
    """
    # create user instance 
    new_user = User(first_name=first_name, last_name=last_name, age=age)
    #place object in the database session
    db.add(new_user)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_user)
    return new_user

def get_user(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_user = db.query(User).filter(User.id==id).first()
    return db_user

def list_users(db:Session):
    """
    Return a list of all existing User records
    """
    all_users = db.query(User).all()
    return all_users


def update_user(db:Session, id:int, first_name: str, last_name: str, age:int):
    """
    Update a User object's attributes
    """
    db_user = get_user(db=db, id=id)
    db_user.first_name = first_name
    db_user.last_name = last_name
    db_user.age = age

    db.commit()
    db.refresh(db_user) #refresh the attribute of the given instance
    return db_user

def delete_user(db:Session, id:int):
    """
    Delete a User object
    """
    db_user = get_user(db=db, id=id)
    db.delete(db_user)
    db.commit() #save changes to db