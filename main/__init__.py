from fastapi import FastAPI

app = FastAPI()

from .main_view import main_view
from routers.v1 import v1

app.include_router(v1, tags=['v1'], prefix='/v1')
