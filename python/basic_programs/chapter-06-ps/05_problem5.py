# Write program which find out whether a given name is present in a list or not
l = ["Harry", "Roshan", "Shubham", "Maxxy"]
name = input("Enter your name : ")
if(name in l):
    print(f"Your name {name} is in the list")
else:
    print(f"Your name {name} is not in the list")