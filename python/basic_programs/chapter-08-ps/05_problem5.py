# Write a python function to print first n lines of the following pattern
'''
***
**
*
for n = 3
'''
n = int(input("Enter a number : "))
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    return pattern(n-1)
pattern(n)

