# Rock Paper Scissor
import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move : Rock, Paper, Scissor\n")
computer_choice = random.choice(item_list)
print(f"user choice : {user_choice}\ncompter choice : {computer_choice}")
if user_choice == computer_choice:
    print("Both chooses same : Match ties")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock : Computer wins")
    else:
        print("Rock smashes Scissors : You win")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts the Paper : Computer wins")
    else:
        print("Paper covers Rock : You win")
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock smashes Scissor : Computer wins ")
    else:
        print("Scissor cuts Paper : You win")
