# check that a tuple type cannot be changed in python
a = (23, 45, 12, "srikanth")
a[2] = "hello" # returns TYpeError
               # 'tuple' object does not support item assignment, tuple is immutable 