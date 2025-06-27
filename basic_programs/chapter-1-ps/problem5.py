#label the problem4 with comments

#print's all the file and directorys
import os #import OS module

# Specify the directory path
directory_path = '/' # / means drive where OS is installed

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
