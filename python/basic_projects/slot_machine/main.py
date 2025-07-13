import random

# Constants defining limits
MAX_LINES = 3          # Maximum number of lines the user can bet on
MAX_BET = 100          # Maximum bet amount per line
MIN_BET = 1            # Minimum bet amount per line

# Slot machine dimensions
ROWS = 3               # Number of rows in the slot machine
COLS = 3               # Number of columns in the slot machine

# Dictionary of symbols and how many times each symbol appears in the pool
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary of symbol values used for calculating winnings
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check which lines won and calculate total winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Check each line up to the number the user is betting on
    for line in range(lines):
        symbol = columns[0][line]  # Take the symbol from the first column for the line
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:  # If any symbol in the line doesn't match, break
                break
        else:
            # If all symbols match (loop didn't break), it's a win
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Store the winning line (1-based index)

    return winnings, winning_lines

# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Create a list containing each symbol repeated by its count
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    # Generate each column randomly
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Make a copy of all symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Remove to avoid duplicate in same column
            column.append(value)
        columns.append(column)

    return columns

# Function to print the slot machine in a readable format
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbol with separator
            else:
                print(column[row], end="")     # Last column without separator
        print()  # Newline after each row

# Function to handle user deposit input
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function to get the number of lines user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Function to get the bet amount per line from user
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# Function to handle a single spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        # Check if user has enough balance
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    # Generate and display slot machine result
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # Calculate winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    # Return the net gain/loss
    return winnings - total_bet

# Main function that runs the game loop
def main():
    balance = deposit()  # Get initial deposit from user
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)  # Update balance with result of spin

    print(f"You left with ${balance}")

# Run the main function to start the game
main()
