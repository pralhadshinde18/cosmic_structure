from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# SQLAlchemy model for the employee table
class EmployeeModel(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_joining = Column(Date)
    working_year = Column(Integer)
