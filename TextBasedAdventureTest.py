#Text based adventure test? 
#Not really sure what I want to do but I wont let that stop me from trying.
#I have a passion to learn!
class Room:
    def __init__(self, name, desc, roomID, northRoom=None, eastRoom=None, southRoom=None, westRoom=None):
        self.name = name
        self.desc = desc
        self.roomID = roomID
        self.contents = []
        #These are the rooms that are connected to this room, IE southRoom is the room to the south of this one
        self.northRoom = northRoom
        self.eastRoom = eastRoom
        self.southRoom = southRoom
        self.westRoom = westRoom

        
    
    def __str__(self):
        return f"{self.name}: {self.desc}"

class Item:
    def __init__(self, name, desc, canTake):
        self.name = name
        self.desc = desc
        self.canTake = canTake
    def __str__(self):
        return f"{self.name}: {self.desc}"


    
#Global vars
CurrentRoomID = 0
Inventory = []

#Items
defaultItem = Item("default item", "An incredibly default item, you bask in the glow of its defaultness!", True)
seriousTable = Item("Serious Table", "The most serious table you have ever seen!", False)
#Rooms
defaultRoom = Room("Default Room", "A strikingly default room with a real sense of defaultness about it",0,)
defaultRoom.contents.append(defaultItem)
seriousRoom = Room("Serious Room", "An incredibly serious room, the most serious room you have ever seen",1)
seriousRoom.contents.append(seriousTable)

#Room connections? 
defaultRoom.northRoom = seriousRoom
seriousRoom.southRoom = defaultRoom
#Need to define this after rooms or it doesnt work (wait or does it?)
currentRoom = defaultRoom

def TextParser(text, room):
    global currentRoom
    try:
        split1 = text.split(":")
        verb = split1[0].strip()
        noun = split1[1].strip().lower()
        #print(verb, noun) #for debug, del this line later
        match verb:
            case "Look":
                if noun.lower() == "around": ### what? it shoud load the room by default and also if you specify it.
                    print("You see " + room.desc + " and : ")#+ room.contents[0].name
                    if len(room.contents) == 0:
                        print("Nothing")
                    else:
                        for i in room.contents:
                            print(i.name)
                    if room.northRoom is not None:
                        print("To the north there is: " + room.northRoom.name)
                    if room.eastRoom is not None:
                        print("To the east there is: " + room.eastRoom.name)
                    if room.southRoom is not None:
                        print("To the south there is: " + room.southRoom.name)
                    if room.westRoom is not None:
                        print("To the west there is: " + room.westRoom.name)
                elif noun.lower() == "inventory":
                    print("You have:")
                    for i in Inventory:
                        print(i.name)
                else: 
                    parserLookHint = 0
                    for i in room.contents:
                        if noun == i.name.lower() :
                            print(i.desc)
                            parserLookHint = 1
                            break
                    for i in Inventory:
                        if noun == i.name.lower():
                            print(i.desc)
                            parserLookHint = 1
                            break
                    if parserLookHint == 0:
                         print("Look at what? To look at your surroundings use Look : Around")
                         print("to check your inventory use Look : Inventory")
            case "Take":
                for i in room.contents:
                    if noun == i.name.lower():
                        if i.canTake == True :
                            room.contents.remove(i)
                            Inventory.append(i)
                            print("You take the " + i.name)
                        else: print ("You cant take the " + i.name)
            case "Go": 
                if noun == "north" or noun == "n":
                    if room.northRoom is not False:
                         currentRoom = room.northRoom
                    else: print("You cannot go north here.")
                    
                elif noun == "east" or noun == "e":
                    if room.eastRoom is not None:
                        currentRoom = room.eastRoom
                    else: print("You cannot go east here.")
                elif noun == "south" or noun == "s":
                    if room.southRoom is not None:
                        currentRoom = room.southRoom
                    else: print("You cannot go south here.")
                elif noun == "west" or noun == "w":
                    if room.westRoom is not None:
                        currentRoom = room.westRoom
                    else: print("You cannot go west here.")
            case _: 
                print("The parser didnt recognize your verb, please try again!")
    except IndexError:
        print("Oops! The Parser didnt understand Try again...")
    
  
def Main(promt):
    print(promt)
    TextParser(input(">"), currentRoom)
    Main(currentRoom.name)


Main("Wellcome! To give commands use the format VERB: NOUN")

