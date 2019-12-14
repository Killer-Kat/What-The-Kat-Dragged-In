#Gold to chicken nugget conversion.
#Version 2.0, Made by Killer-Kat
#In order to measure the conversion between gold nuggets and chicken nuggets we need to establish a few things.
#Gold is measured in troy ounces and one troy ounce is 1.09714 regular ounces.
#In this instance we are going to convert on a one to one mass ratio.
#As of 12/6/2019 McNuggets are 40 for $8.99 USD and they average 0.5 ounces per nugget.
#Thats 0.455729 Troy Ounces for our gold nuggets.
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

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

Choice = int(input("Choose an option: 1: Gold Nuggets to Chicken Nuggets, 2: Chicken Nuggets to Gold Nuggets. "))
gold_nugget_price = (gold_price * 0.455729) #This is the price of 0.455729 troy ounces of gold
Forty_Piece = 0.22475 #This is the price of one chicken nugget based on the mcdonald's 40 piece meal.
#This part uses the users choice to convert either gold to chicken or chicken to gold.
if Choice == 1:
 #Gold to chicken Nugget conversion.
 Nuggets = float(input("Amount of Gold Nuggets to Convert "))
 Dollars = Nuggets * gold_nugget_price
 print("Thats $", end="")
 print (round(Dollars), end="")
 print (" worth of gold.")
 G2C = Dollars / Forty_Piece #This is where the magic happens, and by magic I mean math.

 print (str(Nuggets) + " Gold nuggets is worth " + str(round(G2C)) + " Chicken Nuggets" )
elif Choice == 2:
 Nuggets = float(input("Amount of Chicken Nuggets to Convert "))
 Dollars = Nuggets * Forty_Piece
 C2G = Dollars / gold_nugget_price
 print(C2G)
input("Press Enter to close")