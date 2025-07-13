# Create a class with a class attribute a; create an object from it and set 'a' directly using 'object.a=0' .Does this change the class attribute

class Demo:
    a = 4

obj = Demo()
print(obj.a)  # Prints class attribute because instance attribute is not present
obj.a = 0     # Instance attribute is set
print(obj.a)  # Prints instance attribute because instance attribute is present
print(Demo.a) # Prints class attribute