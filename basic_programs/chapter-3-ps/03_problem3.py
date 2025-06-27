#write a program to detect double space in a string
string1 = "I'm not bad"
print(string1.find("  ")) #returns -1, bcz no double space in the string
string2 = "who are  you"
print(string2.find("  ")) #returns 7, idex of the double space