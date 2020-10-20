#Quantitative Risk Calculator
#Made by KillerKat on Github
#I know this is pretty pointless but its more to help me remeber Risk Management than to be an actual tool.
from tkinter import * #This is the framework for the GUI
import tkinter.messagebox #This neat function allows for a good looking error prompt.

def ALE_Calc():
 try:
  #Gets user input and does maths to calculate the annualized rate of occurrence
  SLE = float(SLE_input.get())
  ARO = float(ARO_input.get())
  ALE = (SLE * ARO)
  labelText.set("The Annual Loss Expectancy for the asset is $" + str(ALE))
 except ValueError:
  tkinter.messagebox.showinfo("Input error", "Error, please input the value of the asset in the following format: $0.00")
 
def help():
 tkinter.messagebox.showinfo("More Info", "Quantitative Risk is a numeric estimate of risk normaly expressed in cash value. It is used to evaluate the overall risk undertaken by a project or asset. This calculator gets the Annual Loss Expectancy of an asset which is the dollar amount of risk associated with an asset durring a 1 year time frame.")

#GUI
root = Tk()
root.title("Quantitative Risk Calculator")
root.geometry("350x150")
root.resizable(0,0)

label_1 = Label(root, text="Single Loss Expectancy :")
label_1.grid(row=0, sticky=W)
SLE_input = Entry(root)
SLE_input.grid(row=0, column=1, sticky=W)
label_2 = Label(root, text="Annualized Rate of Occurrence :")
label_2.grid(row=1, sticky=W)
ARO_input = Entry(root)
ARO_input.grid(row=1, column=1, sticky=W)

button_1 = Button(root, text="Calculate ALE", command=ALE_Calc)
button_1.grid(row=3)
help_button = Button(root, text="More info", command=help)
help_button.grid(row=3, column=1)
#This is the output
labelText = StringVar()
output_label = Label(root, textvariable=labelText)
output_label.grid(row=4, columnspan=2)

root.mainloop()