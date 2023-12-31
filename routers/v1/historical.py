import jdatetime

from . import v1
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends, HTTPException, status
from .v1_schemas import hourly_input_schemas, daily_input_schemas, hourly_output_schemas, daily_output_schemas
from db.models import hd_daily_sbk, hd_hourly_sbk
from main.config import START_DATE, END_DATE
from sqlalchemy.orm import Session
from datetime import timedelta


@v1.post('/hourly', response_model=hourly_output_schemas)
def hourly(body: hourly_input_schemas, db: Session = Depends(get_db)):
    try:
        if not (START_DATE <= body.date < END_DATE):
            raise HTTPException(detail="date is not in the allowed range", status_code=status.HTTP_400_BAD_REQUEST)
        result = db.query(hd_hourly_sbk).filter(hd_hourly_sbk.date == body.date).all()
        return {"date": str(body.date),
                "date_shamsi": str(
                    jdatetime.datetime.fromgregorian(datetime=body.date + timedelta(hours=3, minutes=30))),
                "result": result
                }
    except TypeError:
        raise HTTPException(detail="invalid date", status_code=status.HTTP_400_BAD_REQUEST)


@v1.post('/daily', response_model=daily_output_schemas)
def daily(body: daily_input_schemas, db: Session = Depends(get_db)):
    if not (START_DATE.date() <= body.date < END_DATE.date()):
        raise HTTPException(detail="date is not in the allowed range", status_code=status.HTTP_400_BAD_REQUEST)
    result = db.query(hd_daily_sbk).filter(hd_daily_sbk.date == body.date).all()
    return {"date": str(body.date),
            "result": result
            }
