from pydantic import BaseModel
from datetime import date


# Pydantic models for employee data
class EmployeeBase(BaseModel):
    name: str
    date_of_joining: date


class EmployeeCreate(EmployeeBase):
    pass


# employee model inheriate from employeebase and include additional field like id & working year
class Employee(EmployeeBase):
    id: int
    working_year: int

    # using sqlalchemy models directly in pydantic model
    class Config:
        orm_mode = True
