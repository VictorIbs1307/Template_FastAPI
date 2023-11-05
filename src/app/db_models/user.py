from src.app.core.db import DB

class User(DB.Model):
    __tablename__ = "users"

    # fields 
    id = DB.Column(DB.Integer(), primary_key=True, index=True)
    email = DB.Column(DB.String(20))
    first_name = DB.Column(DB.String(20))
    last_name = DB.Column(DB.String(20))
    age = DB.Column(DB.Integer())
    