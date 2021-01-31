#Project Draugr Variable ROT encoder made by Killer-Kat on github 1/31/2021
#Takes text and ROT value as arguments and encodes the text to the rotation value.
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

