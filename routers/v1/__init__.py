from fastapi import APIRouter

v1 = APIRouter()

from .v1_main_view import v1_main_view
from .hourly import hourly
