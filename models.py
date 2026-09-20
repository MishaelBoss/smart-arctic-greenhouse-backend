from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Device(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    api_key: str = Field(index=True, unique=True)
    connection_type: str = Field(default="wifi")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_seen: Optional[datetime] = None


class Telemetry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="device.id", index=True)

    # Датчик 1 (почва)
    sensor1_raw: int = 0
    sensor1_moisture: float = 0.0

    # Датчик 2 (почва)
    sensor2_raw: int = 0
    sensor2_moisture: float = 0.0

    # Температура/влажность воздуха #1 и #2
    temperature1: Optional[float] = None
    humidity1:    Optional[float] = None
    temperature2: Optional[float] = None
    humidity2:    Optional[float] = None

    # Освещённость #1 и #2
    light1: Optional[int] = None
    light2: Optional[int] = None

    timestamp: datetime = Field(default_factory=datetime.utcnow, index=True)