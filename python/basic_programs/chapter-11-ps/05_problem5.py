# Write a class vector representing a vector of 'n' dimensions. Overload the '+' and '*' operator which calculates the sum and the dot(.) product of them

class Vector:
    def __init__(self, x, y, z):
        # Constructor initializes the vector with x, y, z components
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Overloads the '+' operator to perform vector addition
        # (a1, b1, c1) + (a2, b2, c2) = (a1+a2, b1+b2, c1+c2)
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        # Overloads the '*' operator to compute the dot product of two vectors
        # (a1, b1, c1) · (a2, b2, c2) = a1*a2 + b1*b2 + c1*c2
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        # String representation of the vector for readable output
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Another 3D vector for testing

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32 (dot product)

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50 (dot product)
