# Tic Tac Toe without GUI

# Helper function to sum three values (used for checking winning conditions)
def sum(a, b, c):
    return a + b + c

# Function to print the current game board
def printBoard(xState, zState):
    # Determine what to print for each cell (X, O, or cell index if empty)
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    # Print the formatted board
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

# Function to check if there's a winner
def checkWin(xState, zState):
    # All possible winning combinations (rows, columns, diagonals)
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    # Check each win condition
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0

    # If no one has won yet
    return -1

# Main execution block
if __name__ == "__main__":
    # Initialize the game state: 0 means the cell is empty
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Player X
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Player O

    turn = 1  # 1 for X's turn, 0 for O's turn

    print("Welcome to Tic Tac Toe")

    # Main game loop
    while(True):
        printBoard(xState, zState)  # Display the board

        # Take input depending on whose turn it is
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1

        # Check for a winner after the move
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Match over")
            break
        
        # Switch turns
        turn = 1 - turn
