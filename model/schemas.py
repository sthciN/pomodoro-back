from beanie import PydanticObjectId
from fastapi_users import schemas
from pydantic import EmailStr
from typing import Union

class UserRead(schemas.BaseUser[PydanticObjectId]):
    name: str
    username: str
    email: EmailStr
    avatar: Union[str, None] = None


class UserCreate(schemas.BaseUserCreate):
    name: str
    username: str
    email: EmailStr
    avatar: Union[str, None] = None


class UserUpdate(schemas.BaseUserUpdate):
    name: str
    username: str
    email: EmailStr
    avatar: Union[str, None] = None