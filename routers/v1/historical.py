from . import v1
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends
from .v1_schemas import hourly_schemas, daily_schemas
from sqlalchemy import text


@v1.post('/hourly')
def hourly(body: hourly_schemas, db: Session = Depends(get_db)):
    a = db.execute(text("Select * from  hd_hourly_sbk")).fetchall()
    b = db.execute(text("Select * from  devices LIMIT 10")).fetchall()
    print(body.date)
    return "hourly"


@v1.post('/daily')
def daily(body: daily_schemas, db: Session = Depends(get_db)):
    a = db.execute(text("Select * from  hd_hourly_sbk")).fetchall()
    b = db.execute(text("Select * from  devices LIMIT 10")).fetchall()
    print(body.date)

    return "hourly"
