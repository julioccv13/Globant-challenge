from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HiredEmployee(Base):
    __tablename__ = 'hired_employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer)
    job_id = Column(Integer)

class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    department = Column(String)

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    job = Column(String)
