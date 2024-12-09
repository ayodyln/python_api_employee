from fastapi import FastAPI
from classes.frontend import Frontend
from classes.backend import Backend

app = FastAPI()

employee_list = []


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