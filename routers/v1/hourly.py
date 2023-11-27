from . import v1
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends
from .v1_schemas import hourly_schemas


@v1.get('/hourly')
def hourly(body: hourly_schemas, db: Session = Depends(get_db)):
    return "hourly"
