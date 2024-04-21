from pydantic import BaseModel
from typing import  Optional

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class add_doctor(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class update_availability(BaseModel):
    is_available: Optional[bool] = None

class update_doctor(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    # is_available: Optional[bool] = None

class update_availability(BaseModel):
    is_available: Optional[bool] = None

Doctors: dict[str, Doctor] = {}