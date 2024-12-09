from fastapi import FastAPI
from classes.frontend import Frontend
from classes.backend import Backend
from classes.salary import Salary

# Create an instance of FastAPI

app = FastAPI()

employee_list = [
    Frontend(
        id=0, 
        name="John Doe", 
        salary=Salary(salary=1000, required_hours=8),
        skill="frontend",
        framework="Svelte"
    )
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employee")
def read_employee():
    return employee_list

@app.post("/employee")
def create_employee(request: Frontend | Backend):
    employee = Frontend(
        id=len(employee_list), 
        name=request.name, 
        salary=request.salary, 
        skill=request.skill,
        framework=request.framework
    )
    employee_list.append(employee)
    return employee_list