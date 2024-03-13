from schema.schema import Employee, EmployeeCreate
from model.model import EmployeeModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import List


# Repository class for database operations
class EmployeeRepository:
    def __init__(self):
        engine = create_engine('sqlite:///employee.db')
        Base.metadata.create_all(engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Method for creating a new employee
    def create_employee(self, employee_data: EmployeeCreate, working_year: int) -> Employee:
        # Create EmployeeModel instance
        db_employee = EmployeeModel(name=employee_data.name, date_of_joining=employee_data.date_of_joining,
                                    working_year=working_year)
        db = self.SessionLocal()
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        db.close()
        return db_employee

    # Method for retrieving all employees
    def get_all_employee(self) -> List[Employee]:
        db = self.SessionLocal()
        employees = db.query(EmployeeModel).all()
        db.close()
        return employees
