# Write a class 'Train' which has methods to book a ticket, get status(number of seats) and get fare information of train running under Indian Railways
from random import randint
 
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fromm, to):
        print(f"Ticket is booked in Train number : {self.trainNo} from {fromm} to {to}")

    def getStatus(self):
        print(f"Train number : {self.trainNo} is running on time")

    def getFare(self, fromm, to):
        print(f"Ticket fair in Train number : {self.trainNo} from {fromm} to {to} is {randint(222, 4444)} rupees")

t = Train(4562)
t.book("Bengaluru", "Delhi")
t.getStatus()
t.getFare("Bengaluru", "Delhi")




