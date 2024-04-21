from pydantic import BaseModel
from typing import  Optional
from uuid import UUID

# Appointment: id, patient, doctor, date

class Appointment(BaseModel):
    id: int
    patient_id: int
    patient: str
    doctor_id: int
    doctor: str
    date: str

Appointments: dict[str, Appointment] = {}

