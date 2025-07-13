class Employee:
    company = "ABC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")
    
class Coder():
    language = "Python"
    def printLanguage(self):
        print(f"Out of all laanguages , here is your language {self.language}")

    
class Programmer(Employee, Coder): # this is  multiple inheritance
    company = "XYZ"
    def showLanguage(self):
        print(f"The name is {self.company} and language is {self.language}")
    
a = Employee()
b = Programmer()
b.show()
b.printLanguage()
b.showLanguage()

print(a.company, b.company)