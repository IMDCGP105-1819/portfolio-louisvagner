class Room:
    def __init__(self, description, items):
        self.description = description
        self.items = items

barracks = Room("You are in the barracks, you can see in the room different objects as an alarm clock, a uniform and an alarm button.", ["alarm clock","uniforms","watch","alarm button"])
barracks_list = ["uniform","watch"]
#alarm clock
#uniforms
#watch
#alarm button

dining_room = Room("You are in the dinig room, you can see in the room different objects as some bottles, some plates, a jukebox, a fountain, a broom and an alarm button.", ["bottles","plates","jukebox","fountain","broom","alarm button"])
dining_list = ["bottles","broom"]
#bottles
#plates
#jukebox
#fountain
#broom
#alarm button

power_plant = Room("You are in the power plant, you can see in the room different objects as a notepad, a toolbox, a control panel and an extinguisher.", ["notepad","toolbox","control panel","extinguisher"])
power_list = ["notepad"]
#notepad
#toolbox
#control panel
#extinguisher

water_treatment_plant= Room("You are in the water treatment plant, you can see in the room different objects as a notepad, atoolbox, an adhesif paper, a control panel and an extinguisher.", ["notepad","toolbox","adhesif","control panel","extinguisher"])
water_list = ["notepad","adhesif"]
#notepad
#toolbox
#adhesif
#control panel
#extinguisher

hospital = Room("You are in the hospital, you can see in the room different objects as beds, first aid kit, a lot of syringes.", ["beds","first aid kit","syringes"])
hospital_list = []
#beds
#first aid kit
#syringes

storage_room = Room("You are in the storage room, you can see in the room different objects as some boxes, junk and scrap, armors and guns and some weird rats.", ["boxes","junk boxes","armors","guns","rats"])
storage_list = ["armors","guns"]
#boxes
#junks and scrap
#armors
#guns
#rats

science_lab = Room("You are in the science lab, you can see in the room different objects as chemicals, a huge microscope, some anti-radiation suits and anti-radiation care.", ["chemicals","microscope","anti-radiation suit","anti-radiation care"])
science_list = ["syringes"]
#syringes
#chemicals
#microscope
#anti-radiation suit
#anti-radiation care

vault_door = Room("You are in the vault door, you can see in the room a lever.", ["lever"])
vault_list = ["lever"]
#lever

armory = Room("You are in the armory, you can see in the room different objects as gun parts, bullets and machines.", ["gun parts","bullets","machines"])
armory_list = []
#gun parts
#bullets
#machines

weight_room = Room("You are in the weight room, you can see in the room different objects as weights, ropes and a work bench.", ["weights","ropes","work bench"])
waight_list = []
#weights
#ropes
#work bench

elevator = Room("You are in the elevator, you can see on the wall level buttons and the shelter's map.", ["level button","shelter map"])
#level buttons
#shelter map
