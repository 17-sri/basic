# Write a program to print third, fifth and seventh element in the list using enumerate function
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, item in enumerate(l):
    if(i == 2 or i ==4 or i==6):
        print(item)

