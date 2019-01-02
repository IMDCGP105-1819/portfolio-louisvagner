import Personnage, Objets

class Room:
    def __init__(self, name, description, items, location):
        self.name = name
        self.description = description
        self.items = items
        self.location = location

    def print_items(self):
        item_str = ""
        for item in self.items:
            item_str = item_str + item + ", "
            
        print(item_str[0:-2])

        

def search_room(location):
    for room in rooms:
        if room.location == location:
            return room
        
rooms = []
rooms.append( Room("vault door", "- you are in the vault door. There is way out to the east. Item(s) in the room:", [Objets.names[8]], (0, 1)))
#lever

rooms.append(Room("elevator", "- you are in the elevator of floor 0. There is way out to the east and to the west. You can also go down a floor. Item(s) in the room:", [Objets.names[9]], (1, 1)))
rooms.append(Room("elevator", "- you are in the elevator of floor -1. There is way out to the east and to the west. You can also go down or up a floor. Item(s) in the room:", [Objets.names[9]], (1, 5)))
rooms.append(Room("elevator", "- you are in the elevator of floor -2. There is way out to the east and to the west. You can also go up a floor. Item(s) in the room:", [Objets.names[9]], (1, 9)))
#level buttons
#shelter map

rooms.append(Room("barracks", "- you are in the barracks. There is way out to the south. Item(s) in the room:", [Objets.names[0],Objets.names[1]], (2, 0)))
#alarm clock
#uniforms
#watch
#alarm button

rooms.append(Room("dining room", "- you are in the dining room. There is way out to the west and to the north. Item(s) in the room:", [Objets.names[10],Objets.names[2]], (2, 2)))
#bottles
#plates
#jukebox
#fountain
#broom
#alarm button

rooms.append(Room("storage room", "- you are in the storage room. There is way out to the east. Item(s) in the room:",[Objets.names[6],Objets.names[7],Objets.names[12]], (0, 5)))
#boxes
#junks and scrap
#armors
#guns
#rats

rooms.append(Room("power plant", "- you are in the power plant. There is way out to the north. Item(s) in the room:", [Objets.names[3],Objets.names[4]], (2, 6)))
#notebook
#toolbox
#control panel
#extinguisher

rooms.append(Room("water treatment plant", "- you are in the water treatment plant. There is way out to the south. Item(s) in the room:", [Objets.names[5]], (2, 4)))
#notebook
#toolbox
#adhesif
#control panel
#extinguisher

rooms.append(Room("armory","- you are in the armory. There is way out to the south. Item(s) in the room:", [], (0, 8)))
#gun parts
#bullets
#machines

rooms.append(Room("weight room", "- you are in the weight room. There is way out to the north. Item(s) in the room:", [], (0, 10)))
#weights
#ropes
#work bench

rooms.append(Room("hospital","- you are in the hospital. There is way out to the south. Item(s) in the room:", [Objets.names[9]], (2, 8)))
#beds
#first aid kit
#syringes

rooms.append(Room("science lab", "- you are in the science lab. There is way out to the north. Item(s) in the room:", [], (2, 10)))
#chemicals
#microscope
#anti-radiation suit
#anti-radiation care

rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (2, 1)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (2, 5)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the west.", [], (2, 9)))
rooms.append(Room("corridor", "- you are in a corridor. You can enter a room to the north, to the south and to the east.", [], (0, 9)))
