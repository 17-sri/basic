# Write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [2, 5, 90, 65, 32, 99, 900, 555, 775, 1213, 76]
f = list(filter(divisible5, a))
print(f)