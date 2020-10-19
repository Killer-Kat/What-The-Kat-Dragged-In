#Wellcome to the Tech Sectors favorite gameshow, WHEEL, OF , BUZZWORDS!
#Do you have what it takes to spin the wheel and discover the design for your latest product?
#V1.0

import random
from tkinter import *
#These lists store the buzzwords and products.
buzzwords = ["Cloud Native", "Blockchain", "Container Based", "Zero Trust", "Machine Learning", "Augmented Reality", "5G"]
products = [ "IPS System", "IOT Device", "Smart Fridge", "Teleconferencing Service", "Social Media Network", "Business Collaboration Platform", "VR Headset", "Self Driving Car", "Electric Toothbrush"]

#print("Hello and wellcome to, WHEEL, OF, BUZZWORDS!!!")
#print("Silicon Valley's hottest new gameshow!")

#This function generates the output message.
def Spin():
 buzz1 = buzzwords[random.randrange(0, 7, 1)]
 buzz2 = buzzwords[random.randrange(0, 7, 1)]
 if buzz1 == buzz2:
  print("Looks like you are making a " + buzz1 + " & " + buzz2 + " " + products[random.randrange(0, 9, 1)] + " you must really like "  + buzz1 +"!")
 else: 
  print ("Looks like you are making a " + buzz1 + " & " + buzz2 + " " + products[random.randrange(0, 9, 1)] + ".")

#This part is the GUI
root = Tk()
root.title("WHEEL OF BUZZWORDS!")
root.geometry("500x500")

label_1 = Label(root, text="WHEEL OF BUZZWORDS!")
label_1.pack()
label_2 = Label(root, text="Silicon Valley's hottest new gameshow!")
label_2.pack()

button_1 = Button(root, text="Spin the Wheel!", command=Spin)
button_1.pack()

root.mainloop()