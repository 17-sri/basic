# Define a function named 'myFunc'
def myFunc():
    # Print a greeting message
    print("Hello world")

# This block runs only if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # This message will be printed if the script is run directly (not imported)
    print("We are directly running this code")
    
    # Call the function 'myFunc'
    myFunc()
    
    # Print the special __name__ variable, which should be "__main__" here
    print(__name__)
