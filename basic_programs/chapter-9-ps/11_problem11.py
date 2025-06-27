with open("new.txt") as f:
    content = f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(content)
# create a new file and copy the contents