# __init__() is a special method which is first run as soon as the object is created
# is is known as constructor
# it can take 'self' argument and can also takes further arguments

class Employee:
    language = "Python" # This is the class attribute
    salary = 120000 # This is the class attribute

    def __init__(self): # dunder method, which is automatically called 
        print("I'm creating an object") # this will print before everything

    def getInfo(self):
        print(f"The salary is {self.salary} and language is {self.language}")
        # prints 1200000  and Javascript
    
    # Sometimes we need  function that does not use the self-parameter. We can define a method like this
    @staticmethod
    def greet():
        print("Good Morning ........")

harry = Employee()
harry.name = ("Harry")
print(harry.name, harry.salary)

rohan = Employee() # here also dudnder method will automatically called

