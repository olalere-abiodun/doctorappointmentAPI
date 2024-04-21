from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from datetime import datetime

from schema.patient import Patient,Patients,add_patient, update_patient
from schema.doctor import Doctor,Doctors, add_doctor, update_doctor
from schema.appointment import Appointment,Appointments


router = APIRouter()

appointment_id = 1

@router.get("/appointments", status_code=status.HTTP_200_OK)
def get_appointments():
    return Appointments

@router.post("/book_appointments", status_code=status.HTTP_201_CREATED)
async def create_appointment(patient_id: int, date: str):
    global appointment_id
    if str(patient_id) not in Patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    
     # Check if the provided date is in the future and in format Y-M-D
    appointment_date = datetime.strptime(date, "%Y-%m-%d")
    if appointment_date < datetime.now():
        raise HTTPException(status_code=400, detail="Appointment date must be in the future")

    for doctor_id, doctor in Doctors.items():
        if doctor.is_available:
            doctor.is_available = False
            appointment = Appointment(
                id=appointment_id,
                patient_id=patient_id,
                patient = Patients[str(patient_id)].name,
                doctor_id=doctor_id,
                doctor = Doctors[str(doctor_id)].name,
                date=date
            )
            Appointments[appointment_id] = appointment
            appointment_id += 1
            
            return {"message": "Appointment booked successfully", "Serial Number": appointment.id, "doctor_name": Doctors[str(doctor_id)].name, "patient_name": Patients[str(patient_id)].name, "date": date}
           
    raise HTTPException(status_code=404, detail="No available doctors")

#complete appointment
@router.put("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
async def complete_appointment(appointment_id: int):
    appointment = Appointments.get(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    doc = str(appointment.doctor_id)
    doctor = Doctors.get(doc)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor.is_available = True
    del Appointments[appointment_id]
    return {"message": "Appointment completed successfully"}

#cancel the appointment

@router.delete("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
async def cancel_appointment(appointment_id: int):
    appointment = Appointments.get(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    doc = str(appointment.doctor_id)
    doctor = Doctors.get(doc)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor.is_available = True
    del Appointments[appointment_id]
    return {"message": "Appointment cancelled successfully"}
