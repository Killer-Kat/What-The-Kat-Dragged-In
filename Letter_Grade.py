#Simple program to turn a score into a letter grade. Made by Killer Kat.
#I offhandedly tried asking siri to tell me what the grade corresponding to a percent was and I was suprised that it didnt.
#So I wrote this for fun, feel free to use it as long as you arent Apple.
grade = float(input("Enter Your Grade: "))

if grade >= 90:
 print ("Your grade is A!")
elif grade >= 80:
 print ("Your grade is B")
elif grade >= 70:
 print ("Your grade is C")
elif grade >= 60:
 print ("Your grade is D")
elif grade >= 0:
 print ("FAIL")
 
input("Press Enter to close")
