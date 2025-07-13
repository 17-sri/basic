import random

# Mapping:
# 1 for Snake
# -1 for Water 
# 0 for Gun

# Computer randomly selects one of the three choices
computer = random.choice([-1, 0, 1])

# Ask the user for their choice
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Dictionary to map user input to numerical values
youDict = {"s": 1, "w": -1, "g": 0}

# Reverse dictionary to convert numeric values back to string for display
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the numeric value of the user's choice
you = youDict[youstr]

# Display choices made by the user and the computer
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Determine the result
if computer == you:
    print("It's a draw")  # Same choice results in a draw

# All winning and losing conditions
else:
    if computer == -1 and you == 1:  # Snake drinks water
        print("You win!")

    elif computer == -1 and you == 0:  # Gun sinks in water
        print("You Lose!")

    elif computer == 1 and you == -1:  # Snake drinks water
        print("You lose!")

    elif computer == 1 and you == 0:  # Gun kills snake
        print("You Win!")

    elif computer == 0 and you == -1:  # Water sinks gun
        print("You Win!")

    elif computer == 0 and you == 1:  # Gun kills snake
        print("You Lose!")

    else:
        print("Something went wrong!")  # Fallback for unexpected cases
