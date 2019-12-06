#Gold to chicken nugget conversion
#In order to measure the conversion between gold nuggets and chicken nuggets we need to establish a few things.
#Gold is measured in troy ounces and one troy ounce is 1.09714 regular ounces.
#In this instance we are going to convert on a one to one mass ratio.
#As of 12/6/2019 McNuggets are 40 for $8.99 USD and they average 0.5 ounces per nugget.
#Thats 0.455729 Troy Ounces for our gold nuggets.


Nuggets = float(input("Amount of Gold Nuggets to Convert "))
Price = 673.37 #This is the price of 0.455729 troy ounces of gold as of 12/6/2019

Dollars = Nuggets * Price
print("Thats $", end="")
print (Dollars)
G2C = Dollars / 0.22475

print(Nuggets, end="")
print(" Gold nuggets is worth ", end="")
print (G2C, end="")
print (" Chicken Nuggets")

input("Press Enter to close")