#Simple program to turn a score into a letter grade. Made by Killer Kat.
#I offhandedly tried asking siri to tell me what the grade corresponding to a percent was and I was suprised that it didnt.
#So I wrote this for fun, feel free to use it as long as you arent Apple.
#Version 2, added gui and other improvements.
from tkinter import *
import tkinter.messagebox #this is used for the error message
def Grade_Percent():
#this calculates a percentage based on user input
 try:
  Current_Points = float(my_score.get())
  Total_Points = float(max_score.get())
  if Total_Points == 0:
   #print ("If the maxium points available are zero that means you passed.") 
   percent = 100
  else:
   percent = ((Current_Points / Total_Points) * 100)
 except ValueError:
  tkinter.messagebox.showinfo("Input error", "Score must be a numerical value.")
  percent = 0
 finally:
  grade = percent
  GradeMSG = ("You got %" + str(round(percent, 2)))

 #These if statemnts print what grade you got.
 if grade >= 100:
  labelText.set( GradeMSG + ": Your grade is A+, Impressive!")
 elif grade >= 93:
  labelText.set(GradeMSG + ": Your grade is A!")
 elif grade >= 90:
  labelText.set(GradeMSG + ": Your grade is A-")
 elif grade >= 87:
  labelText.set(GradeMSG + ": Your grade is B+")
 elif grade >= 83:
  labelText.set(GradeMSG + ": Your grade is B")
 elif grade >= 80:
  labelText.set(GradeMSG + ": Your grade is B-")
 elif grade >= 77:
  labelText.set(GradeMSG + ": Your grade is C+")
 elif grade >= 73:
  labelText.set(GradeMSG + ": Your grade is C")
 elif grade >= 70:
  labelText.set(GradeMSG + ": Your grade is C-")
 elif grade >= 67:
  labelText.set(GradeMSG + ": Your grade is D+")
 elif grade >= 63:
  labelText.set(GradeMSG + ": Your grade is D")
 elif grade >= 60:
  labelText.set(GradeMSG + ": Your grade is D")
 elif grade >= 0:
  labelText.set(GradeMSG + ": Your grade is an F") # You need %" + str(round((60 - percent),2)) + " more to pass.")
 else:
  labelText.set("ERROR")


#GUI
root = Tk()
root.title("Grade Calculator")
root.geometry("325x150")
root.resizable(0,0)
root.configure(background="DeepSkyBLue4")

label_1 = Label(root, text="Current Score:", bg="DeepSkyBLue4", fg="LightSteelBlue2")
label_1.grid(row=0, sticky=W)
my_score = Entry(root, bg="DeepSkyBLue3", fg="LightSteelBlue2")
my_score.grid(row=0, column=1, sticky=W)
label_2 = Label(root, text="Total Possible Score:", bg="DeepSkyBLue4", fg="LightSteelBlue2")
label_2.grid(row=1, sticky=W)
max_score = Entry(root,bg="DeepSkyBLue3", fg="LightSteelBlue2")
max_score.grid(row=1, column=1, sticky=W)

button_1 = Button(root, text="Calculate Grade", command=Grade_Percent, bg="DeepSkyBLue4", fg="LightSteelBlue2")
button_1.grid(row=3)
#This is the output
labelText = StringVar()
label_3 = Label(root, textvariable=labelText, bg="DeepSkyBLue4", fg="LightSteelBlue2")
label_3.grid(row=4, columnspan=2)

root.mainloop()
