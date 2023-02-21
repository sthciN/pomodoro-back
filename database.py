from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["pomodorotest"]

users_collection = db["user"]
todo_lists_collection = db["todo_list"]
todo_items_collection = db["todo_item"]
