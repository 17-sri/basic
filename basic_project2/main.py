# We are going to write a program thst generate a random number and asks the user to guess it
# If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "Higher number please". When the user guesses the correct number, the program displays thenumber of guesses the player used to arrive at the number.
# Hint : Use the random module
 
import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number : "))
    if(a>n):
        print("Enter lower number please")
        guesses +=1
    elif(a<n):
        print("Enter higher number please")
        guesses +=1
print(f"You guessed the number {n} correctly in {guesses} attempts ")  