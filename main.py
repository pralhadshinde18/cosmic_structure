from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import List
from service.service import EmployeeService

# create instance of fastapi
app = FastAPI()
# initialize employee service instance
employee_service = EmployeeService()


# create model of employee using pydantic
class EmployeeCreate(BaseModel):
    name: str
    date_of_joining: date


class Employee(BaseModel):
    id: int
    name: str
    working_year: int


# endpoint for create new employee
@app.post("/employee/", response_model=Employee)
def create_employee(employee_data: EmployeeCreate):
    employee = employee_service.create_employee(employee_data)
    return employee


# endpoint for get all employee
@app.get("/employee/", response_model=List[Employee])
def get_employee():
    return employee_service.get_all_employee()
