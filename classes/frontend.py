from classes.employee import Employee

class Frontend(Employee):
    skill: str
    framework: str
    
    def displayFrontend(self):
        print(f"Name: {self.name}, Salary: {self.salary}")