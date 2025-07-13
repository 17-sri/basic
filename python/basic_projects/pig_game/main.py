import random  # Importing the random module to simulate dice rolls

# Function to simulate rolling a six-sided die
def roll():
    return random.randint(1, 6)

# Ask the user to enter the number of players (between 2 and 4)
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():  # Check if input is a number
        players = int(players)
        if 2 <= players <= 4:  # Check if number is within valid range
            break
        else:
            print("Invalid input. Must be between 2 and 4 players.")
    else:
        print("Invalid input. Please enter a number.")

# Initialize game settings
max_score = 50  # Score needed to win the game
player_score = [0 for _ in range(players)]  # List to track each player's total score

# Main game loop: continues until a player reaches max_score
while max(player_score) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn:")
        print(f"Current total score: {player_score[player_idx]}")
        current_score = 0  # Reset turn score at the start of each turn

        # Turn loop: player chooses to roll or hold
        while True:
            should_roll = input("Would you like to roll? (y to roll, anything else to hold): ").lower()
            if should_roll != 'y':  # If player chooses to hold
                break

            value = roll()  # Simulate a dice roll
            print(f"You rolled a {value}.")

            if value == 1:
                # Rolling a 1 ends the turn and forfeits turn points
                print("Oops! Rolled a 1. Turn over, no points added.")
                current_score = 0
                break
            else:
                # Add roll value to current turn score
                current_score += value
                print(f"Current turn score: {current_score}")

        # After turn ends, add turn score to player's total
        player_score[player_idx] += current_score
        print(f"Total score for Player {player_idx + 1}: {player_score[player_idx]}")

        # Break outer loop if a player reaches the winning score
        if player_score[player_idx] >= max_score:
            break

# Game is over: determine and announce the winner
winning_score = max(player_score)
winner = player_score.index(winning_score) + 1
print(f"\nPlayer {winner} wins with a score of {winning_score}! ")
