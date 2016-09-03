#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, contains_eager
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department
    # onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        #lazy='joined',
                        cascade='delete,all'))


from sqlalchemy import create_engine
engine = create_engine('sqlite:///tutorial6.db')
engine.echo = True

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

d = Department(name="IT")
emp1 = Employee(name="John", department=d)
s = session()
#s.add(d)
#s.add(emp1)
#s.commit()

emps = s.query(Employee).filter(Department.name == 'IT')
for emp in emps:
    print(emp.name, emp.department.name)
    print(emp.name, emp.department.name)
    print(emp.name, emp.department.name)