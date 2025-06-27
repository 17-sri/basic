# super() method is used to access the methods of a super class in the derived class

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
class Manager(Programmer): # This is multilevel inheritance
    def __init__(self):
        super().__init__() # This will access the super class methods i,e 'Programmer' methods
        print("Constructor of Manager")
    c = 3
o = Employee()
print(o.a)
o = Programmer()
print(o.a, o.b)
o = Manager()
print(o.a, o.b, o.c)