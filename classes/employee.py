from pydantic import BaseModel
from typing import Optional
from classes.salary import Salary

class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    salary: Salary

    def displayEmployee(self):
        print("Name : ", self.name,)