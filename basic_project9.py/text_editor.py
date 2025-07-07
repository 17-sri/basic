# Import tkinter modules for GUI, file dialog, and message boxes
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create a new file (clears the text area)
def new_file():
    text.delete(1.0, tk.END)

# Function to open an existing file and load its contents into the text area
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Function to save the current text to a file
def save_file():
    file_path = filedialog.asksaveasfilename(  # Changed from `askopenfilename` to `asksaveasfilename`
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File Saved Successfully")

# Create the main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

# Add commands to the File menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a text area for editing
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="red")
text.pack(expand=tk.YES, fill=tk.BOTH)

# Start the Tkinter event loop (fix: call the function with parentheses)
root.mainloop()
