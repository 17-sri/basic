a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if(b == 0):
    raise ZeroDivisionError("Hey your program is not meant to devide numbers by zero")
else:
    print(f"the division of a/b ia {a/b}")