# Write a program to find out whether a file is identical & matches the content of another file
with open("this.txt") as f:
    content1 = f.read()
with open("this_copy.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes, These files are identical ")
else:
    print("These files are not identical ")