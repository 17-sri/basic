a = (3, 5, 9, 3, "hello", True, 2.2, "who")
print(a)
no = a.count(3)
print(no) # returns 2, bcz 3 occurs two times in the tuple
i = a.index(3)
print(i) # returns 0,  the index of 3 in first occurance
print("s" in a) # returns False, bcz 's' is  not in the tuple
b = (4, 6, 8, 3)
concatinated_tuple = a + b
print(concatinated_tuple)
print(len(concatinated_tuple)) # returns 12, length of the tuple
sliced_tuple = concatinated_tuple[1:11:2] # tuple slicing
print(sliced_tuple)