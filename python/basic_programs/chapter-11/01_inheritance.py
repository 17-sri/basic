class Employee:
    company = "ABC"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")
    
class Programmer(Employee): # this is inheritance
    company = "XYZ"
    def showLanguage(self):
        print(f"The name is {self.company} and salary is {self.salary}")
    
a = Employee()
b = Programmer()


print(a.company, b.company)