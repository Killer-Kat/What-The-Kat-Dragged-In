#!/usr/bin/env python3
#Binary to ACSII converter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Text", help="The text you wish to convert, use quotes to encapsulate text with spaces")
parser.add_argument("-tf", "--translate_from", help="Convert from ASCII to Binary", action="store_true", default=False)
args = parser.parse_args()

Output_String = ""
Temp_Var = ""
ASCII_To_Binary = {
    "A" : "01000001",
    "B" : "01000010",
    "C" : "01000011",
    "D" : "01000100",
    "E" : "01000101",
    "F" : "01000110",
    "G" : "01000111",
    "H" : "01001000",
    "I" : "01001001",
    "J" : "01001010",
    "K" : "01001011",
    "L" : "01001100",
    "M" : "01001101",
    "N" : "01001110",
    "O" : "01001111",
    "P" : "01010000",
    "Q" : "01010001",
    "R" : "01010010",
    "S" : "01010011",
    "T" : "01010100",
    "U" : "01010101",
    "V" : "01010110",
    "W" : "01010111",
    "X" : "01011000",
    "Y" : "01011001",
    "Z" : "01011010",
    " " : "00100000",
	"!" : "00100001",
	"\"" : "00100010",
	"#" : "00100011",
	"$" : "00100100",
	"%" : "00100101",
	"&" : "00100110",
	"(" : "00101000",
	")" : "00101001",
    }
Binary_To_ACSII = {
    "01000001" : "A",
    "01000010" : "B", 
    "01000011" : "C",   
    "01000100" : "D",   
    "01000101" : "E",   
    "01000110" : "F",   
    "01000111" : "G",   
    "01001000" : "H",   
    "01001001" : "I",   
    "01001010" : "J",   
    "01001011" : "K",   
    "01001100" : "L",   
    "01001101" : "M",   
    "01001110" : "N",   
    "01001111" : "O",   
    "01010000" : "P",   
    "01010001" : "Q",   
    "01010010" : "R",   
    "01010011" : "S",   
    "01010100" : "T",   
    "01010101" : "U",   
    "01010110" : "V",   
    "01010111" : "W",   
    "01011000" : "X",   
    "01011001" : "Y",
    "01011010" : "Z",
    "00100000" : " ",
	"00100001" : "!",
	"00100010" : "\"",
	"00100011" : "#",
	"00100100" : "$",
	"00100101" : "%",
	"00100110" : "&",
	"00101000" : "(",
	"00101001" : ")",
    }
if args.translate_from == True:
	for i in args.Text:
        	Output_String = Output_String + ASCII_To_Binary.get(i, "UNKNOWN") + " "
else:
	for i in args.Text:
		if i != " ":
			Temp_Var = Temp_Var + i
		else :
			Output_String = Output_String + Binary_To_ACSII.get(Temp_Var, "UNKNOWN")
			Temp_Var = ""


Output_String = Output_String + Binary_To_ACSII.get(Temp_Var, "UNKNOWN")
print(Output_String)
