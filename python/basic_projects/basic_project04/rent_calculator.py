#inputs we need from the user
#total rent
#total food ordered for snacks
#electricity units spent
#charge per unit
#persons living in room
# #output
# total amount you have to pay is

rent = int(input("Enter your rent : "))
food = int(input("Enter the amunt of food ordered : "))
electricity = int(input("enter the electricity spent : "))
charge_per_unit = int(input("enter the charge per unit : "))
persons = int(input("enter the number of persons living in room : "))
total_e_bill = electricity*charge_per_unit
output = (food + rent + total_e_bill) / persons
print(f"each person will pay {output}")
