# Write a program using functions to find greatest of three numbers

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = int(input("Enter a : "))
b = int(input("Enter b : "))  
c = int(input("Enter c : "))
print(f"greatest of three numbers is {greatest(a, b, c)}")