# container to store a set of values of any data type
# List is mutable

friends = ["Apple", "Pineapple", 17, 1997.9, "Cat", False]
print(friends[0]) # returns 'Apple'
friends[0] = "Grapes"  # unlike strings , lists are mutable
print(friends[0]) # returns 'Grapes'
# lists can be indexed like a string
friends[4]   # returns 'Cat'
#friends[6]   # returns error
print(friends[1:5:2]) #sliced list like string, returns 'Pineapple', '1997.9'