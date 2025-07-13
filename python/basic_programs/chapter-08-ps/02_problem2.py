# Write a program using functions to convert Celsius to Fahrenheit
# c/5 = (f-32)/9
# c = 5*(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in °F : "))
c = f_to_c(f)
print(f"Temperature in Celsius is {round(c, 2)}°C")

# round(c,2) : this round figures to two digits