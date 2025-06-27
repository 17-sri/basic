# Define a class named Number
class Number:
    # Constructor method to initialize the instance with a number
    def __init__(self, n):
        self.n = n

    # Overloading the + operator to define custom behavior for addition
    def __add__(self, num):
        # Return the sum of the internal values of two Number instances
        return self.n + num.n

# Create two instances of the Number class with values 1 and 2
n = Number(1)
m = Number(2)

# Add the two instances using the overloaded + operator and print the result
print(n + m)  # Output: 3
