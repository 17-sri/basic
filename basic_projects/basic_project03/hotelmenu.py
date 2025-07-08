# menu
menu = {
    'pizza' : 40,
    'pasta' : 45,
    'burger' : 50,
    'salad' : 65,
    'coffee' : 75,
}
# great
print("Welcome to ABC restaurant ")
print("pizza : 40\npasta : 45\nburger : 50\nsalad : 65\ncoffee : 75")
order_total = 0
item_1 = input("Enter the item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been ordered successfully")
else:
    print(f"ordered item {item_1} is not available yet")
another_order = input("do you want ot order another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been ordered successfully")
    else:
        print(f"ordered item {item_2} is not available yet")

print(f"the total amount of items to pay is {order_total}")
