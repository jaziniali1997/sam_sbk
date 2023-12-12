from pydantic import BaseModel
from datetime import datetime, date
from typing import List


class hourly_input_schemas(BaseModel):
    date: datetime


class daily_input_schemas(BaseModel):
    date: date


class daily_data_schemas(BaseModel):
    loc_id: int
    date: datetime
    t2m_dm: float
    t2m_dmax: float
    t2m_dmin: float
    d2m_dm: float
    tp_dsum: float
    ssrd_dsum: float
    e_dsum: float
    sd_dsum: float
    sde_dsum: float
    rh2m_dmax: int
    rh2m_dm: int
    rh2m_dmin: int
    sshn_dsum: float


class daily_output_schemas(BaseModel):
    date: date
    result: List[daily_data_schemas]


class hourly_data_schemas(BaseModel):
    loc_id: int
    date: datetime
    local_date: datetime
    sunrise_local: datetime
    sunset_local: datetime
    day_duration: float
    dd_10m: int
    ff_10m: float
    tcc: int
    t2m: float
    d2m: float
    tp: float
    e: float
    fg10: float
    pev: float
    sd: float
    sde: float
    sf: float
    skt: float
    smlt: float
    snowc: int
    ssr: float
    ssrd: float
    rh2m: int
    ws: str
    sshn: float


class hourly_output_schemas(BaseModel):
    date: datetime
    date_shamsi: str
    result: List[hourly_data_schemas]