# Add a static method in problem 2, to greet the user with 'Hello'
class Calculator:
    def __init__(self, n):
        self.n = n

    def sqaure(self):
        print(f"Square is {self.n*self.n}")
    
    def cube(self):
        print(f"Cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"Squareroot is {self.n**0.5}")
    @staticmethod
    def greet():
        print("Hello there !")

number = int(input("Enter a number : "))
a = Calculator(number)
a.greet()
a.sqaure()
a.cube()
a.squareroot()

