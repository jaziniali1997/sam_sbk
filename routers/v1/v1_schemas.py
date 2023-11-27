from pydantic import BaseModel
from datetime import datetime, date


class hourly_schemas(BaseModel):
    date: datetime


class daily_schemas(BaseModel):
    date: date