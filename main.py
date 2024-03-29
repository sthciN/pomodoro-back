from fastapi import Body, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app import app
from database import (db, todo_items_collection, todo_lists_collection,
                      users_collection)
from model.models import TodoItem, TodoList, User

from beanie import init_beanie
from utils.auth import auth_backend
from model.users import current_active_user, fastapi_users
from model.schemas import UserRead, UserCreate, UserUpdate

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.on_event("startup")
async def on_startup():
    await init_beanie(
        database=db,  
        document_models=[
            User,  
        ],
    )

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

@app.post('/user')
async def create_user(user: User = Body(...)):
    user = jsonable_encoder(user)
    print('user', user)
    result = users_collection.insert_one(user)
    
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'id': str(result.inserted_id)})


@app.get('/user/{user_id}')
async def get_user(user_id: str):
    user = users_collection.find_one({'_id': user_id})
    
    if user:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)
    
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f'User {user_id} not found.')


@app.post('/todo-list')
async def create_todo_list(todo_list: TodoList = Body(...)):
    todo_list = jsonable_encoder(todo_list)
    result = todo_lists_collection.insert_one(todo_list)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'id': str(result.inserted_id)})


@app.get('/todo-list/{list_id}')
async def get_todo_list(list_id: str):
    todo_list = todo_lists_collection.find_one({'_id': list_id})

    if todo_list:
        return JSONResponse(status_code=status.HTTP_200_OK, content=todo_list)
    
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f'Todo list {list_id} not found.')


@app.post('/todo-item')
async def create_todo_item(todo_item: TodoItem = Body(...)):
    todo_item = jsonable_encoder(todo_item)
    result = todo_items_collection.insert_one(todo_item)
    
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'id': str(result.inserted_id)})


@app.get('/todo-item/{item_id}')
async def get_todo_item(item_id: str):
    todo_item = todo_items_collection.find_one({'_id': item_id})
    
    if todo_item:
        return JSONResponse(status_code=status.HTTP_200_OK, content=todo_item)

    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f'Todo item {item_id} not found.')
    