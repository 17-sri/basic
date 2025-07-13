class Employee:
    language = "Python" # This is the class attribute
    salary = 120000 # This is the class attribute

harry = Employee()
harry.language = "Javascript" # This is an instance attribute
print(harry.salary, harry.language) # prints 1200000 Javascript

# Instance attribute take preference over class attribute during assignment and retrieval
