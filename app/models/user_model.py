# app/models/user_model.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(32), unique=True, index=True)
    name = Column(String(32))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    create_datetime = Column(DateTime, default=datetime.now(timezone.utc))
    update_datetime = Column(DateTime, default=datetime.now(timezone.utc))
    active = Column(Boolean)