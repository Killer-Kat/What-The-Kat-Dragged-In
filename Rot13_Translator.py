
#I thought it might be fun to code a ROT13 translator so here we are
#Made by Killer-Kat on Github on 1/27/2021

from tkinter import * #Our GUI framework
def ROT13_Translator():
 Rotated_Letters  = { #Dictionary to hold all of our rotated letters
     "A": "N",
     "B": "O",
     "C": "P",
     "D": "Q",
     "E": "R",
     "F": "S",
     "G": "T",
     "H": "U",
     "I": "V",
     "J": "W",
     "K": "X",
     "L": "Y",
     "M": "Z",
     "N": "A",
     "O": "B",
     "P": "C",
     "Q": "D",
     "R": "E",
     "S": "F",
     "T": "G",
     "U": "H",
     "V": "I",
     "W": "J",
     "X": "K",
     "Y": "L",
     "Z": "M",
     " ": " ",
     "a": "n",
     "b": "o",
     "c": "p",
     "d": "q",
     "e": "r",
     "f": "s",
     "g": "t",
     "h": "u",
     "i": "v",
     "j": "w",
     "k": "x",
     "l": "y",
     "m": "z",
     "n": "a",
     "o": "b",
     "p": "c",
     "q": "d",
     "r": "e",
     "s": "f",
     "t": "g",
     "u": "h",
     "v": "i",
     "w": "j",
     "x": "k",
     "y": "l",
     "z": "m",
     ".": ".",
     ",": ",",
     "?": "?",
     "\n" : "\n",
     "0": "0",
     "1": "1",
     "2": "2",
     "3": "3",
     "4": "4",
     "5": "5",
     "6": "6",
     "7": "7",
     "8": "8",
     "9": "9",
     }

 Text_output = ""
 Text_input = output.get(0.0, END)

 for i in Text_input:
     Text_output = Text_output + Rotated_Letters.get(i, "*") #Rotated_Letters[i]
 output.delete(0.0, END)
 output.insert(END, Text_output)


#GUI
root = Tk()
root.title("ROT13 Converter")
root.geometry("500x275")

Title_Label = Label(root, text="ROT13 Converter!")
Title_Label.grid(row=0)

conversion_button = Button(root, text="Convert Text", command=ROT13_Translator)
conversion_button.grid(row=1, column=2,)
info_button = Button(root, text="More Info")
info_button.grid(row=2, column=2,)

output = Text(root, width=35, height=5, wrap=WORD)
output.grid(row=1, column=0, columnspan=2,rowspan=3)

root.mainloop() #Keeps the window open and running