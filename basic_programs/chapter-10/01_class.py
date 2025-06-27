class Employee:
    language = "py" # This is the class attribute
    salary = 120000 # This is the class attribute

harry = Employee()
harry.name = "Harry" # This is an instance attribute
print(harry.name, harry.salary, harry.language)

rohan = Employee()
rohan.name = "Rohan Ro" # This is an instance attribute
print(rohan.name, rohan.language, rohan.salary)

# Here name is the instance attribute and salary, language is the class attributes as they directly belongs to the class