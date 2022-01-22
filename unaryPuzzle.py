#Made by KillerKat on Github 1/22/2022 Check out my blog! https://cyberkatcafe.com/
#Code to solve Unary puzzle on codeingame.com https://www.codingame.com/training/easy/unary
import sys
import math

message = input()
message = str(bin(ord(message)))[2:]
charlist = []
charlist.append(message[0])
listCounter = 0
firstTime = True
outputString = ""
print(message, file=sys.stderr, flush=True)
print(charlist, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#This will seperate the input into groups of 1 or 0
for i in message:
    if firstTime == True:
        firstTime = False
    elif i == charlist[listCounter][0]:
        charlist[listCounter] = charlist[listCounter] + i
    else: 
        listCounter += 1
        charlist.append(i)
for parts in charlist:
    if parts[0] == str(1):
        outputString = outputString + " 0 "
    else: outputString = outputString + " 00 "
    for i in parts:
        outputString = outputString + str(0)
print(charlist, file=sys.stderr, flush=True)
print(outputString, file=sys.stderr, flush=True)
print(outputString[1:])
