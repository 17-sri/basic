# Import the tkinter module for GUI creation
import tkinter as tk

# Import the strftime function from the time module to format time strings
from time import strftime

# Create the main window of the application
root = tk.Tk()

# Set the title of the window
root.title("Digital Clock")

# Define a function to update the time every second
def time():
    # Get the current time formatted as hours:minutes:seconds AM/PM and date (MM/DD/YY)
    String = strftime('%H:%M:%S %p \n %D')
    
    # Update the label's text with the current time and date
    label.config(text=String)
    
    # Schedule this function to be called again after 1000 milliseconds (1 second)
    label.after(1000, time)

# Create a label widget to display the time
# Set the font to Calibri, size 175, bold style
# Set background color to black and text color to red
label = tk.Label(root, font=('calibri', 175, 'bold'), background='black', foreground='red')

# Pack the label widget into the window and center it
label.pack(anchor='center')

# Call the time function to start the clock updates
time()

# Start the Tkinter event loop to keep the window open
root.mainloop()
