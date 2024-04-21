from pydantic import BaseModel
from typing import  Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    address: str
    phone: str

class add_patient(BaseModel):
    name: str
    age: int
    sex: str
    address: str
    phone: str

class update_patient(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

Patients: dict[str, Patient] = {}