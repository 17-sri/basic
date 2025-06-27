class Employee:
    language = "Python" # This is the class attribute
    salary = 120000 # This is the class attribute

    def getInfo(self):
        print(f"The salary is {self.salary} and language is {self.language}")
        # prints 1200000  and Javascript
    
    # Sometimes we need  function that does not use the self-parameter. We can define a method like this
    @staticmethod
    def greet():
        print("Good Morning ........")

harry = Employee()
harry.language = "Javascript" # This is an instance attribute
harry.greet()
#harry.getInfo()             # both are same
Employee.getInfo(harry)      # both are same