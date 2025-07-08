import random

'''
1 for Snake
-1 for Water 
0 for Gun
'''

# Computer randomly picks one of the three options
computer = random.choice([-1, 0, 1])

# User input: 's' for snake, 'w' for water, 'g' for gun
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Dictionary to convert user input string to numeric value
youDict = {"s": 1, "w": -1, "g": 0}

# Dictionary to convert numeric values back to text for display
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Convert user input to its numeric representation
you = youDict[youstr]

# Display both choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Check for a draw
if computer == you:
    print("It's a draw")

else:
    '''
    Explanation of outcomes using (computer - you):
    - (computer - you) == -1  → you lose
    - (computer - you) == 2   → you lose
    - All other cases         → you win

    Why?
    -----------------------------
    S (1) beats W (-1) → 1 - (-1) = 2
    W (-1) beats G (0) → -1 - 0 = -1
    G (0) beats S (1)  → 0 - 1 = -1

    So, losing cases: computer - you = -1 or 2
    '''

    if (computer - you) == -1 or (computer - you) == 2:
        print("You lose!")
    else:
        print("You win!")
