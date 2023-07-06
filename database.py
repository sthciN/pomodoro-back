import os

import motor.motor_asyncio

monogdb_user = os.environ['ADMIN_MONGODB_USER']
mongodb_pass = os.environ['ADMIN_MONGODB_PASSWORD']

DATABASE_URL = "mongodb+srv://{}:{}@cluster-pomo.e9dzoyj.mongodb.net/?retryWrites=true&w=majority"\
                     .format(monogdb_user, mongodb_pass)
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["pomodoro-tm"]

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
users_collection = db["user"]
todo_lists_collection = db["todo_list"]
todo_items_collection = db["todo_item"]
