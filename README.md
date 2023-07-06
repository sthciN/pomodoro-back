# PomoDo

This is a project providing the APIs for a TO-DO application with a focus on the Pomodoro technique.

The code is written in Python language, FastAPI framework and the database is MongoDB on atlas cloud.
You can easily run the project by installing the requirements by ```pip install -r requirements```.

I have utilized fastapi-users for user registration and user authentication.

## Start
```uvicorn main:app --reload```


```
├── README.md
├── app
│   ├── __init__.py
├── database.py
├── main.py
├── model
│   ├── models.py
│   ├── schemas.py
│   └── users.py
├── requirements.txt
└── utils
    ├── auth.py
    ├── email.py
    └── exceptions.py

```


## Routes

Auth router: /login and /logout 
Register router: /register 
Reset password router: /forgot-password and /reset-password
Verify router: /request-verify-token and /verify (User can login only after verification)
