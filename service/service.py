from domain.domain import EmployeeDomain
from schema.schema import Employee, EmployeeCreate
from repo.repository import EmployeeRepository
from typing import List


# business logic for employee opration
class EmployeeService:
    def __init__(self):
        self.repo = EmployeeRepository()  # Initialize Employee repositry instance

    # method for creating new emplooyee
    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        # create employee domain  instance and calculate working yeaar
        employee_domain = EmployeeDomain(name=employee_data.name, date_of_joining=employee_data.date_of_joining)
        working_year = employee_domain.calculate_time_period()
        return self.repo.create_employee(employee_data, working_year)

    # methoad for retriving all employee
    def get_all_employee(self) -> List[Employee]:
        return self.repo.get_all_employee()  # retrivr all emp in repositry
