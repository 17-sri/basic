try:
    a = int(input("Enter a number"))
    print(a)

except Exception as e:
    print(e)

else:
    print("I'm inside else") # This will excute only when try block is successful