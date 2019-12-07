#Simple program to turn a score into a letter grade. Made by Killer Kat.
#I offhandedly tried asking siri to tell me what the grade corresponding to a percent was and I was suprised that it didnt.
#So I wrote this for fun, feel free to use it as long as you arent Apple.

#this calculates a percentage based on user input
Current_Points = float(input("Input current Points in class: "))
Total_Points = float(input("Input total points possible: "))
percent = ((Current_Points / Total_Points) * 100)

#grade = float(input("Enter Your Grade: "))
grade = percent

if grade >= 93:
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
 print ("FAIL")
else:
 print ("ERROR")
 
input("Press Enter to close")
