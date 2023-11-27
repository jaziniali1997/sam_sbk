from pydantic import BaseModel
from datetime import datetime


class hourly_schemas(BaseModel):
    date: datetime
