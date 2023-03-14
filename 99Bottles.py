#Made by KillerKat on Github
#Just a funny idea I had so I wanted to write a quick script, I doubt any other human will ever read this script.
import random

def Bottles(x,y):
    bottles = x
    contents = y
    for i in range(bottles):
        chance = random.randrange(0,(bottles+1),1) #Gets a random number with the upper bound of the current number of bottles so the chance increases as the amount of bottles decreases.
        if chance == bottles:
            print("You get alcohol poisioning from all the " + contents + " and pass out.")
            return
        print( str(bottles) + " bottles of " + str(contents) + " on the wall " + str(bottles) + " of " + str(contents) + " take one down pass it around " + str((bottles -1)) + "  bottles of " + str(contents) + " on the wall!")
        bottles -= 1

Bottles(99, "beer")

