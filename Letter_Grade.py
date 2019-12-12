#Simple program to turn a score into a letter grade. Made by Killer Kat.
#I offhandedly tried asking siri to tell me what the grade corresponding to a percent was and I was suprised that it didnt.
#So I wrote this for fun, feel free to use it as long as you arent Apple.

print ("This tool will calculate your final grade in a class based on your current score.")
#this calculates a percentage based on user input
Current_Points = float(input("Input current Points in class: "))
Total_Points = float(input("Input total points possible: "))
if Total_Points == 0:
 print ("If the maxium points available are zero that means you passed.") 
 percent = 100
else:
 percent = ((Current_Points / Total_Points) * 100)

grade = percent
print ("You got %" + str(percent)[:5] )

#These if statemnts print what grade you got.
if grade >= 100:
 print ("Your grade is A+, Impressive!")
elif grade >= 93:
 print ("Your grade is A!")
elif grade >= 90:
 print ("Your grade is A-")
elif grade >= 87:
 print ("Your grade is B+")
elif grade >= 83:
 print ("Your grade is B")
elif grade >= 80:
 print ("Your grade is B-")
elif grade >= 77:
 print ("Your grade is C+")
elif grade >= 73:
 print ("Your grade is C")
elif grade >= 70:
 print ("Your grade is C-")
elif grade >= 67:
 print ("Your grade is D+")
elif grade >= 63:
 print ("Your grade is D")
elif grade >= 60:
 print ("Your grade is D")
elif grade >= 0:
 print ("Your grade is an F, That means you fail. You need %" + str((60 - percent))[:5] + " more to pass.")
else:
 print ("ERROR")
 
input("Press Enter to close")
