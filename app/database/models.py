from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MobileBarRequest(Base):
    __tablename__ = "mobile_bar_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(60), nullable=False)
    guests_teens = Column(Integer, nullable=False)
    guests_adults = Column(Integer, nullable=False)
    location = Column(String(255), nullable=False)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=False)
    service_duration = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<MobileBarRequest(id={self.id}, name='{self.email}')>"