#!/usr/bin/env python3
#Project Draugr Variable ROT encoder made by Killer-Kat on github 1/31/2021
#Takes text and ROT value as arguments and encodes the text to the rotation value.
#The name comes from the Scandinavian Undead, as undead are rotten and thats what I always think about when I hear ROT.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Text", help="The text to convert to rotated text, use quotes to encapsulate text with spaces")
parser.add_argument("-r", "-Rotation", help="Rotation is The amount of spaces you want to rotate the text by the default is 13", type=int, default=13, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26])
parser.add_argument("-a", "-all", help="Run all possible rotation values for the text", action="store_true", default=False)
args = parser.parse_args()

def Main(Text_Input,Rotation):
    Output_String = ""
    Is_Caps = False
    Letter_Value = {
     "A": 1,
     "B": 2,
     "C": 3,
     "D": 4,
     "E": 5,
     "F": 6,
     "G": 7,
     "H": 8,
     "I": 9,
     "J": 10,
     "K": 11,
     "L": 12,
     "M": 13,
     "N": 14,
     "O": 15,
     "P": 16,
     "Q": 17,
     "R": 18,
     "S": 19,
     "T": 20,
     "U": 21,
     "V": 22,
     "W": 23,
     "X": 24,
     "Y": 25,
     "Z": 26,
    }
    Place_Value = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
    5 : "E",
    6 : "F",
    7 : "G",
    8 : "H",
    9 : "I",
    10 : "J",
    11 : "K",
    12 : "L",
    13 : "M",
    14 : "N",
    15 : "O",
    16 : "P",
    17 : "Q",
    18 : "R",
    19 : "S",
    20 : "T",
    21 : "U",
    22 : "V",
    23 : "W",
    24 : "X",
    25 : "Y",
    26 : "Z",
    }
    for i in Text_Input:
        x = Letter_Value.get(i.upper(), "&") #The & here is just a placeholder for something not in the dictionary
        if type(x) == int:
            if i.upper() == i:
                Is_Caps = True
            else : Is_Caps = False    
            x = x + Rotation
            if x > 26 :
                x = x -26
            if Is_Caps == True:
                Output_String = Output_String + Place_Value[x]
            else: 
                Output_String = Output_String + Place_Value[x].lower()
        else:
            Output_String = Output_String + i
    print(Output_String)
if args.a == True:
	for i in range(26):
		Main(args.Text,i)
else: Main(args.Text,args.r)
