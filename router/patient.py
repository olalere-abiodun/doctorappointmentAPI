# CRUD endpoints for Patients
from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from schema.patient import Patient,Patients,add_patient, update_patient
from schema.doctor import Doctor,Doctors, add_doctor, update_doctor, update_availability

router = APIRouter()

# Get all patient information
@router.get("/patients", status_code=status.HTTP_200_OK)
def get_patient():
    return Patients
#Create a new Patient
@router.post("/patients", status_code=status.HTTP_201_CREATED)
def create_patient(patient: add_patient):
    new_patient = Patient(
        id=int(UUID(int=len(Patients) + 1)),
        name=patient.name,
        age=patient.age,
        sex=patient.sex,
        address=patient.address,
        phone=patient.phone
    )
    Patients[str(new_patient.id)] = new_patient
    return new_patient

#get patient by ID
@router.get("/patients/{patient_id}", status_code=status.HTTP_200_OK)
def get_patient_by_id(patient_id: int):
    try:
        return Patients[str(patient_id)]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} not found"
        )

#update patient
@router.put("/patients/{patient_id}", status_code=status.HTTP_200_OK)
def update_patient(patient_id: int, patient: update_patient):
    try:
        Patients[str(patient_id)].age = patient.age
        Patients[str(patient_id)].sex = patient.sex
        Patients[str(patient_id)].address = patient.address
        Patients[str(patient_id)].phone = patient.phone

        return patient

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with the ID {patient_id} not found"
        )

#delete patient
@router.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    try:
        
        del Patients[str(patient_id)]
             
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with the ID {patient_id} not found"
        )