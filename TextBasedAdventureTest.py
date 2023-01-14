#Text based adventure test? 
#Not really sure what I want to do but I wont let that stop me from trying.
#I have a passion to learn!
class Room:
    def __init__(self, name, desc, roomID):
        self.name = name
        self.desc = desc
        self.roomID = roomID
        self.contents = []
    
    def __str__(self):
        return f"{self.name}: {self.desc}"

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def __str__(self):
        return f"{self.name}: {self.desc}"


    
#Global vars
CurrentRoomID = 0

#Items
defaultItem = Item("default item", "An incredibly default item, you bask in the glow of its defaultness!")
#Rooms
defaultRoom = Room("Default Room", "A strikingly default room with a real sense of defaultness about it",0,)
defaultRoom.contents.append(defaultItem)

#No idea if this will work, googled it but found nothing
allItems = [defaultItem] # Wait I might not even need this!
#Need to define this after rooms or it doesnt work (wait or does it?)
currentRoom = defaultRoom

def TextParser(text, room):
    try:
        split1 = text.split(":")
        verb = split1[0].strip()
        noun = split1[1].strip().lower()
        #print(verb, noun) #for debug, del this line later
        match verb:
            case "Look":
                if noun.lower() == "around": ### what? it shoud load the room by default and also if you specify it.
                    print("You see " + room.desc + " and : "+ room.contents[0].name)
                else: 
                    parserLookHint = 0
                    for i in room.contents:
                        if noun == i.name.lower() :
                            print(i.desc)
                            parserLookHint = 1
                            break
                    if parserLookHint == 0:
                         print("Look at what? To look at your surroundings use Look : Around")
                    
            case _: 
                print("The parser didnt recognize your verb, please try agian!")
    except IndexError:
        print("Oops! The Parser didnt understand Try again...")
    
  
def Main(promt):
    print(promt)
    TextParser(input(">"), currentRoom)
    Main(defaultRoom)

Main("Wellcome! To give commands use the format VERB: NOUN")

