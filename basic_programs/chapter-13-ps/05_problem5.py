# Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
l = [2, 5, 90, 65, 32, 99, 900, 555, 775, 12, 76]
def greater(a, b):
    if(a>b):
        return a
    return b 
print(reduce(greater, l))




