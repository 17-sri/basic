# Write a program to print the multiplication table of 'n' using for loops in reverse order
n = int(input("Enter a number : "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")

