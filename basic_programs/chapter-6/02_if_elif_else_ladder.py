# if elif else ladder
a = int(input("enter your age : "))
if(a>=18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
    print("you're entering invalid negetive age")
elif(a==0):
    print("you're entering 0, which is invalid age")
else:
    print("you are below the age of consent")
print("end of program")
