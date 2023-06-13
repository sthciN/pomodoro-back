from typing import Union

from beanie import PydanticObjectId
from bson import ObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from pydantic import BaseModel, EmailStr, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BeanieBaseUser[PydanticObjectId]):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str = Field(min_length=3, max_length=300)
    username: str = Field(min_length=3, max_length=256)
    email: EmailStr
    avatar: Union[str, None] = None
    
    class Config:
        arbitrary_types_allowed: False
        json_encoders = {ObjectId: str}

async def get_user_db():
    yield BeanieUserDatabase(User)

class TodoList(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    user_id: str
    list_name: str = Field(min_length=1, max_length=600)

    class Config:
        arbitrary_types_allowed: False
        json_encoders = {ObjectId: str}

class TodoItem(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    todolist_id: str
    user_id: str
    item_name: str = Field(min_length=1, max_length=600)
    due_date: str
    is_completed: bool

    class Config:
        arbitrary_types_allowed: False
        json_encoders = {ObjectId: str}
