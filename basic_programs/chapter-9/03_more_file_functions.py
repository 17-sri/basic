f = open("file.txt")
'''
lines = f.readlines()  # readlines()
print(lines, type(lines)) # It returns 'list'
'''

line = f.readline()    # readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close