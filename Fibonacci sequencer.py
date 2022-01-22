#Fibonacci sequencer
#I was playing a coding clash on codingame.com and it was a reversing challenge for the Fibonacci sequence
#But I ran out of time because I got tripped up on the 0 1 part of the sequence, but since I code becuase I enjoy it and enjoy learning I made this
#Made by KillerKat on Github, Checkout my blog! CyberKatCafe.com

firstNumber = 1
secondNumber = 0
init = True
print("Fibonacci Sequencer")
print("This Program calculates the Fibonacci sequence to whatever length is specified by the user.")
n = input("Calculate how many digits? : > ")
print(0) 
for i in range(int(n) - 1):
    newNumber = (firstNumber + secondNumber)
    firstNumber = secondNumber
    secondNumber = newNumber
    print(newNumber)