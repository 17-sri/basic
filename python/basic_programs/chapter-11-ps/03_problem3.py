class Employee:
    salary = 234             # Class variable: base salary
    increment = 20           # Class variable: percentage increment

    @property
    def salaryAfterIncrement(self):
        # Calculates the salary after applying the increment
        return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        # Sets the increment percentage based on the new target salary
        # Formula rearranged from: new_salary = salary + salary * (increment / 100)
        self.increment = ((salary / self.salary) - 1) * 100

e = Employee()
e.salaryAfterIncrement = 280.8  # Sets increment so that salaryAfterIncrement becomes 280.8
print(e.increment)              # Prints the calculated increment (should be 20.0)
