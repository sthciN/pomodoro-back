from app import app
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

class InvalidPasswordException(StarletteHTTPException):
    pass


@app.exception_handler(StarletteHTTPException)
def handle_exception(e):
    return PlainTextResponse(str(e.detail), status_code = e.status_code)
