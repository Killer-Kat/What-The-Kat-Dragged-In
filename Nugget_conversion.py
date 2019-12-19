#Gold to chicken nugget conversion.
#Version 3.3, Made by Killer-Kat
#In order to measure the conversion between gold nuggets and chicken nuggets we need to establish a few things.
#Gold is measured in troy ounces and one troy ounce is 1.09714 regular ounces.
#In this instance we are going to convert on a one to one mass ratio.
#As of 12/6/2019 McNuggets are 40 for $8.99 USD and they average 0.5 ounces per nugget.
#Thats 0.455729 Troy Ounces for our gold nuggets.
import re
from bs4 import BeautifulSoup #This helps parse the HTML data
from urllib.request import urlopen #this is needed to get the HTML data
from tkinter import * #this is needed for the gui
import tkinter.messagebox #this is used for the error messages
#this part gets the web page and scrapes it for its html data.
my_url = "https://www.jmbullion.com/charts/gold-price/"
gold_url = urlopen(my_url)
page_html = gold_url.read()
gold_url.close()
#This converts the raw HTML data into a float that the script can use for its calculations.
page_soup = BeautifulSoup(page_html, "html.parser")
containers = page_soup.findAll("div", {"id": "gounce"})
gold_price = float("".join(filter(lambda d: str.isdigit(d) or d == '.', str(containers)))) #dont know how this works, it was written by thund on stack overflow
#print("the valvue of gold is $" + str(gold_price) + " per Troy ounce")

gold_nugget_price = (gold_price * 0.455729) #This is the price of 0.455729 troy ounces of gold
Forty_Piece = 0.22475 #This is the price of one chicken nugget based on the mcdonald's 40 piece meal.
#Here we are defining the conversions, this helps when trying to add to the program

def Gold2Chicken():
 #Gold to chicken Nugget conversion.
 try:
  Nuggets = float(Nug_input.get())
  Dollars = Nuggets * gold_nugget_price
  G2C = Dollars / Forty_Piece #This is where the magic happens, and by magic I mean math.
 except ValueError:
  tkinter.messagebox.showinfo("Input error", "Error, please input a numerical value.")
 else:
  output.delete(0.0, END) #This clears the output text box so the next line can fill it.
  output.insert(END, (str(Nuggets) + " Gold nuggets is worth " + str(round(G2C)) + " Chicken Nuggets" ))
  labelText.set("Thats $" + str(round(Dollars, 2)) +" worth of nuggets!")
def Chicken2Gold():
 try:
  Nuggets = float(Nug_input.get())
  Dollars = Nuggets * Forty_Piece
  C2G = Dollars / gold_nugget_price
 except ValueError:
  tkinter.messagebox.showinfo("Input error", "Error, please input a numerical value.")
 else:
  output.delete(0.0, END)
  output.insert(END, (str(Nuggets) + " Chicken Nuggets is worth " + str(round(C2G, 5)) + " Gold Nuggets"))
  labelText.set("Thats $ " + str(round(Dollars, 2)) + " worth of nuggets!")

#This is the GUI
root = Tk()
root.title("Gold To Chicken Nuggets")
root.geometry("325x150")
root.resizable(0,0)

label_1 = Label(root, text="Input Amount of Nuggets:")
label_1.grid(row=0, sticky=W)
Nug_input = Entry(root)
Nug_input.grid(row=0, column=1, sticky=W)

labelText = StringVar() #Sets a variable that can be used as the text in the label
label_2 = Label(root, textvariable=labelText)
label_2.grid(row=2, columnspan=2)

button_1 = Button(root, text="Convert Gold to Chicken", command=Gold2Chicken)
button_1.grid(row=1)
button_2 = Button(root, text="Convert Chicken to Gold", command=Chicken2Gold)
button_2.grid(row=1, column=1)

output = Text(root, width=35, height=2, wrap=WORD, background="white")
output.grid(row=4, column=0, columnspan=2)

root.mainloop()