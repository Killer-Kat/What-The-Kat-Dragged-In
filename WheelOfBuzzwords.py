#Wellcome to the Tech Sectors favorite gameshow, WHEEL, OF , BUZZWORDS!
#Do you have what it takes to spin the wheel and discover the design for your latest product?
#V1.0

import random

buzzwords = ["Cloud Native", "Blockchain", "Container Based", "Zero Trust", "Machine Learning", "Augmented Reality", "5G"]
products = [ "IPS System", "IOT Device", "Smart Fridge", "Teleconferencing Service", "Social Media Network", "Business Collaboration Platform", "VR Headset"]

print("Hello and wellcome to, WHEEL, OF, BUZZWORDS!!!")
print("Silicon Valley's hottest new gameshow!")

print("Looks like you are making a " + buzzwords[random.randrange(0, 7, 1)] + " & " + buzzwords[random.randrange(0, 7, 1)] + " " + products[random.randrange(0, 8, 1)])
input()