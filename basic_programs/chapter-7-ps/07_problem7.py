# Write program to print the following star pattern
'''
  *
 ***
*****
for n = 3
'''
n = int(input(" Enter a number : "))
for i in range(1, n+1):
    print(" "*(n-i), end = "")   # it is for spaces
    print("x"*(2*i-1), end = "") # it is for stars
    print("")
# end="" it will stop new line 