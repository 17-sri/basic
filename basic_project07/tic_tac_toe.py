# Tic Tac Toe with GUI (Improved)

import tkinter as tk
from tkinter import messagebox

# Function to check if any player has won the game
def check_winner():
    global winner
    # List of winning combinations (by button indices)
    for combo in [[0,1,2], [3,4,5], [6,7,8],
                  [0,3,6], [1,4,7], [2,5,8],
                  [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight the winning combination
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True  # Set winner flag
            # Announce winner and offer to restart
            result = messagebox.askyesno("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!\nDo you want to play again?")
            if result:
                restart_game()
            else:
                root.quit()
            return

    # Check for draw: all buttons are filled and no winner
    if all(button["text"] != "" for button in buttons) and not winner:
        winner = True
        result = messagebox.askyesno("Tic Tac Toe", "It's a draw!\nDo you want to play again?")
        if result:
            restart_game()
        else:
            root.quit()

# Function to handle button click events
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# Switch the current player and update the label
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Restart the game by resetting all button texts and colors
def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state=tk.NORMAL)
    label.config(text=f"Player {current_player}'s turn")

# --- GUI Setup ---
root = tk.Tk()
root.title("Tic Tac Toe")

# Create 9 buttons and assign their commands
buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2,
              command=lambda i=i: button_click(i))
    for i in range(9)
]

# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

# Game state variables
current_player = "X"
winner = False

# Label to display the current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()