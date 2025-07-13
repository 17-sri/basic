# write a pyhton program to print the contents of a directory using the os module, search online for the function which does that

#print's all the file and directorys
import os

# Specify the directory path
directory_path = '/' # / means drive where OS is installed

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
