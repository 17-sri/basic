# Create a class 'Programmer' for storing information of few programmers working at Microsoft

class Programmer:
    company  = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Harry", "122000", "560066")
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", "130000", "560055")
print(r.name, r.salary, r.pin, r.company)
