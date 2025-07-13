name = "srikanth"           #single qouted : valid 
myname = 'srikanth'         #double quoted : valid
name_is = '''srikanth'''    #triple quoted : valid
# string are immutable, onv=ce defined we cannot change the value


nameshort  = name[0:3] #start from index 0 all the way till 3, excluding 3 (it returns 'sri')
print(nameshort)
print(name[:4]) # starts with 0 ends with 4 , (returns 'srik')
print(name[3:]) # starts with 3 ends with len(string) , (returns 'kanth')