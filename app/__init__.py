from fastapi import FastAPI
from dotenv import find_dotenv, load_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
app = FastAPI()
