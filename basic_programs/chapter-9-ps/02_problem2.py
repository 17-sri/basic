# The game() function in a program lets a user to play a game and returns an integer. You need to read a file 'Hi-sore.txt' which is either blank or contains the previous Hi-score. You need to write a program to update te Hi-score whenever the game() function braks the Hi-score

import random
def game():
    print("You are palying the game... ")
    score = random.randint(2, 77)
    # fetch the hiscore 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score
game()        

