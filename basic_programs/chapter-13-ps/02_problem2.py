# write  program to input name marks and phone number of a studentand format it using the format function like below:
'''
The name of the student is Harry, his mmarks are 77 and phone number is 234567456
'''

name  = input("Enter name : ")
marks = int(input("Enter marks : "))
phone = int(input("Enter phone number : "))
s = "The name of the student is {}, his mmarks are {} and phone number is 2{}".format(name, marks, phone)
print(s)