from pydantic import BaseModel

class Salary(BaseModel):
    salary: float
    required_hours: int

    def displaySalary(self):
        print("Salary: ", self.salary,  ", Required Hours: ", self.required_hours)
    