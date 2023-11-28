from fastapi import Depends, Body, HTTPException, status
from datetime import datetime
from main.config import START_DATE, END_DATE

start_date = START_DATE
end_date = END_DATE


def date_range_checker():
    def decorator(func):
        async def wrapper(date: datetime = Body(...)):
            if start_date <= date <= end_date:
                return await func(date)
            else:
                raise HTTPException(detail="date is not in the allowed range", status_code=status.HTTP_400_BAD_REQUEST)

        return wrapper

    return decorator
