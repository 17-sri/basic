a = 89
def fun():
    global a
    a = 3
    print(a)  # both prints a = 3 only
fun()
print(a)