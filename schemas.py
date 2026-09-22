from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DeviceCreate(BaseModel):
    name: str
    connection_type: str = "wifi"


class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    connection_type: Optional[str] = None


class DeviceOut(BaseModel):
    id: int
    name: str
    api_key: str
    last_seen: Optional[datetime] = None
    connection_type: str 
    class Config:
        from_attributes = True


class TelemetryIn(BaseModel):
    soil1_raw: int
    soil1_moisture: float
    soil2_raw: int
    soil2_moisture: float
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    temperature2: Optional[float] = None
    humidity2: Optional[float] = None
    light1: Optional[int] = None
    light2: Optional[int] = None
    pump: Optional[bool] = None
    light: Optional[bool] = None
    roof: Optional[bool] = None
    ev: Optional[list[str]] = None


class TelemetryOut(BaseModel):
    soil1_raw: int
    soil1_moisture: float
    soil2_raw: int
    soil2_moisture: float
    temperature: Optional[float]
    humidity: Optional[float]
    temperature2: Optional[float] = None
    humidity2: Optional[float] = None
    light1: Optional[int] = None
    light2: Optional[int] = None
    pump: Optional[bool] = None
    light: Optional[bool] = None
    roof: Optional[bool] = None
    timestamp: datetime
    is_fresh: bool = True 
    age_seconds: float = 0.0 
    class Config:
        from_attributes = True


class CommandIn(BaseModel):
    action: str