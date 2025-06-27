# Write a class "Calculate" capable of finding square, cube and square root of a number
class Calculator:
    def __init__(self, n):
        self.n = n

    def sqaure(self):
        print(f"Square is {self.n*self.n}")
    
    def cube(self):
        print(f"Cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"Squareroot is {self.n**0.5}")

number = int(input("Enter a number : "))
a = Calculator(number)
a.sqaure()
a.cube()
a.squareroot()
