from pydantic import BaseModel
from datetime import datetime, date


class hourly_schemas(BaseModel):
    date: datetime


class daily_schemas(BaseModel):
    date: dateclass daily_input_schemas(BaseModel):
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
