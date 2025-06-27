# Write a list comprehension to print a list which contains the multiplication table of user entered a number

n = int(input("Enter a number : "))
table = [n*i for i in range(1, 11)]
print(table)