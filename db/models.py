from db.database import Base
from sqlalchemy import Column, Float, Integer, DateTime, String


class hd_hourly_sbk(Base):
    __tablename__ = 'hd_hourly_sbk'

    pkid = Column(Integer, primary_key=True)

    loc_id = Column(Integer)
    date = Column(DateTime)
    local_date = Column(DateTime)
    sunrise_local = Column(DateTime)
    sunset_local = Column(DateTime)
    day_duration = Column(Float)
    dd_10m = Column(Integer)
    ff_10m = Column(Float)
    tcc = Column(Integer)
    t2m = Column(Float)
    d2m = Column(Float)
    tp = Column(Float)
    e = Column(Float)
    fg10 = Column(Float)
    pev = Column(Float)
    sd = Column(Float)
    sde = Column(Float)
    sf = Column(Float)
    skt = Column(Float)
    smlt = Column(Float)
    snowc = Column(Integer)
    ssr = Column(Float)
    ssrd = Column(Float)
    rh2m = Column(Integer)
    ws = Column(String)
    sshn = Column(Float)


class hd_daily_sbk(Base):
    __tablename__ = 'hd_daily_sbk'

    pkid = Column(Integer, primary_key=True)

    loc_id = Column(Integer)
    date = Column(DateTime)
    t2m_dm = Column(Float)
    t2m_dmax = Column(Float)
    t2m_dmin = Column(Float)
    d2m_dm = Column(Float)
    tp_dsum = Column(Float)
    ssrd_dsum = Column(Float)
    e_dsum = Column(Float)
    sd_dsum = Column(Float)
    sde_dsum = Column(Float)
    rh2m_dmax = Column(Integer)
    rh2m_dm = Column(Integer)
    rh2m_dmin = Column(Integer)
    sshn_dsum = Column(Integer)
