# CRUD endpoints for Doctors
from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from schema.patient import Patient,Patients,add_patient, update_patient
from schema.doctor import Doctor,Doctors, add_doctor, update_doctor, update_availability

router = APIRouter()

# get all doctors information
@router.get("/doctor", status_code=status.HTTP_200_OK)
def get_doctor():
    return Doctors

# Add a new doctor
@router.post("/doctor", status_code=status.HTTP_201_CREATED)
def add_doctor(doctor: add_doctor):
    new_doctor = Doctor(
    id=int(UUID(int=len(Doctors) + 1)),
    name=doctor.name,
    specialization=doctor.specialization,
    phone=doctor.phone,
    is_available=doctor.is_available
    )
    Doctors[str(new_doctor.id)] = new_doctor
    return new_doctor

# get doctor information by ID
@router.get("/doctor/{doctor_id}", status_code=status.HTTP_200_OK)
def get_doctor_by_id(doctor_id: int):
    if str(doctor_id) in Doctors:
        return Doctors[str(doctor_id)]
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")

# set doctor availabiltiy
@router.put("/doctor/{doctor_id}", status_code=status.HTTP_200_OK)
def update_doctor_availability(doctor_id: int, doctor: update_availability):
    if str(doctor_id) in Doctors:
        Doctors[str(doctor_id)].is_available = doctor.is_available
        return Doctors[str(doctor_id)]
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")

# Update doctors information
@router.put("/doctors/{doctor_id}", status_code=status.HTTP_200_OK)
def update_doctor(doctor_id: int, doctor: update_doctor):
    if str(doctor_id) in Doctors:
        Doctors[str(doctor_id)].name = doctor.name
        Doctors[str(doctor_id)].specialization = doctor.specialization
        Doctors[str(doctor_id)].phone = doctor.phone
        return Doctors[str(doctor_id)]
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")

# delete a doctor
@router.delete("/doctor/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int):
    if str(doctor_id) in Doctors:
        del Doctors[str(doctor_id)]
        return
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")
    

