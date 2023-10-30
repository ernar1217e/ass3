from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
import database
from database import User
from fastapi import FastAPI

from retrieve import *

Session = sessionmaker(bind=database.engine)
session = Session()

app = FastAPI()

@app.get('/users')
async def read_users():
    return read_all_users()

@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return read_one_user(user_id)

# @app.post('/users')
# async def create_user(user: User):
#     return user
