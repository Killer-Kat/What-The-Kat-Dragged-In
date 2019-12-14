#Gold to chicken nugget conversion.
#Version 1.0, Made by Killer-Kat
#In order to measure the conversion between gold nuggets and chicken nuggets we need to establish a few things.
#Gold is measured in troy ounces and one troy ounce is 1.09714 regular ounces.
#In this instance we are going to convert on a one to one mass ratio.
#As of 12/6/2019 McNuggets are 40 for $8.99 USD and they average 0.5 ounces per nugget.
#Thats 0.455729 Troy Ounces for our gold nuggets.

Choice = int(input("Choose an option: 1: Gold Nuggets to Chicken Nuggets, 2: Chicken Nuggets to Gold Nuggets. "))


Price = 673.37 #This is the price of 0.455729 troy ounces of gold as of 12/6/2019
Forty_Piece = 0.22475 #This is the price of one chicken nugget based on the mcdonald's 40 piece meal.

if Choice == 1:
 #Gold to chicken Nugget conversion.
 Nuggets = float(input("Amount of Gold Nuggets to Convert "))
 Dollars = Nuggets * Price
 print("Thats $", end="")
 print (round(Dollars), end="")
 print (" worth of gold.")
 G2C = Dollars / Forty_Piece #This is where the magic happens, and by magic I mean math.

 #This just prints the final statement.
 print (str(Nuggets) + " Gold nuggets is worth " + str(round(G2C)) + " Chicken Nuggets" )
elif Choice == 2:
 Nuggets = float(input("Amount of Chicken Nuggets to Convert "))
 Dollars = Nuggets * Forty_Piece
 C2G = Dollars / Price
 print(C2G)
input("Press Enter to close")