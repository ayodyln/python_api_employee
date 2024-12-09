from classes.employee import Employee

class Backend(Employee):
    skill: str

    def displayFrontend(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)