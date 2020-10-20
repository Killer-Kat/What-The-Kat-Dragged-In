#Annual loss expectancy calculator
#Made by KillerKat on Github
#I know this is pretty pointless but its more to help me remeber Risk Management than to be an actual tool.

#Gets user input and does maths to calculate the annualized rate of occurrence
SLE = float(input("Enter single loss expectancy for the asset : $"))
ARO = float(input("Enter annualized rate of occurrence : "))
ALE = (SLE * ARO)

print("The ALE for the asset is $", end="")
print(ALE)

input("Press enter to exit")