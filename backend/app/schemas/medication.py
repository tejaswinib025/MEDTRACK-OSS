from pydantic import BaseModel
from typing import Optional, List

class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    instructions: Optional[str] = None

class MedicationCreate(MedicationBase):
    pass

class MedicationUpdate(MedicationBase):
    name: Optional[str] = None
    dosage: Optional[str] = None

class Medication(MedicationBase):
    id: str
    owner_id: str
