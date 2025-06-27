d= {}  # empty dictionary 

marks = {"rohan": 78,
         "shubham": 98,
         "harry": 99
}
print(marks.items()) # returns a list of (key,value) tuple
print(marks.keys()) # returns a list containing dictionary's keys
print(marks.values()) # returns a list containing dictionary's values
marks.update({"harry": 97, "roxxy": 95}) # dictionary is mutable
print(marks)
print(marks.get("maxxy")) # returns 'None'
print(marks["maxxy"]) # returns an error
print(marks.get("harry")) # returns 97

