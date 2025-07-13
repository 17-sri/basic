class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
e = Employee()
e.a = 45
e.show() # the absence of @classmethod, this will print 45 instead of 1