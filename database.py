from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import os


monogdb_user = os.environ['ADMIN_MONGODB_USER']
mongodb_pass = os.environ['ADMIN_MONGODB_PASSWORD']
client = MongoClient("mongodb+srv://{}:{}@cluster-pomo.e9dzoyj.mongodb.net/?retryWrites=true&w=majority"\
                     .format(monogdb_user, mongodb_pass))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client["pomodoro-tm"]
users_collection = db["user"]
todo_lists_collection = db["todo_list"]
todo_items_collection = db["todo_item"]
