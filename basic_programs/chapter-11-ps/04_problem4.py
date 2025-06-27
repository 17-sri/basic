# Write a class 'Complex' to represent complex numbers, along with overloaded operators    '+' and '*' which adds and multiplies them

class Complex:
    def __init__(self, r, i):
        # Constructor initializes the real and imaginary parts of the complex number
        self.r = r
        self.i = i

    def __add__(self, c2):
        # Overloads the '+' operator to add two complex numbers
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        # Overloads the '*' operator to multiply two complex numbers
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        # Returns the string representation of the complex number
        return f"{self.r} + {self.i}i"
        
# Create two Complex number instances
c1 = Complex(1, 2)
c2 = Complex(3, 4)

# Print the result of addition and multiplication
print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 10i
