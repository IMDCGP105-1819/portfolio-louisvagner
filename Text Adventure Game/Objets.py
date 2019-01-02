# Important objects - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Item:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

items = []
names = []
position = []

uniform = Item("uniform","- shirt and trouser representative of the vault you are in. \n /!\ Put it on before getting out of the barracks.", (2, 0))
    #A mettre sinon <<Intrusion>>

watch = Item("watch","- bracelet giving the time.", (2, 0))
    #avoir une idée de l'heure

broom = Item("broom","- long broom that helps get rid of dust.", (2, 2))
    #chasser les rats
             
notebook = Item("notebook","- block with several sheets of paper, it is possible to write in if used.", (2, 6))
    #permet d'ecrire ce qu'on veut

armor = Item("armor","- protection for the body used for combat.", (0, 5))
    #augmente la défense

gun = Item("gun","- firearm used to defend or kill.", (0 ,5))
    #permet de se defendre

"""extinguisher = Item("extinguisher","Object to extinguish a fire.")
    #eteindre le feu

first_aid = Item("first aid kit","Care kit used between fights.")
    #se soigner

junks_scrap = Item("junks and scrap","old bits of junk and scrap for the sole purpose of being recycled.")
    #pour construire son arme

antiradiation_suit = Item("anti-radiation suit","radiation protection suit.")
    #protège des radiations (pas totalement)

antiradiation_care = Item("anti-radiation care","care that cancels the effects of radiation.")
    #soigne les radiations
             
gun_parts = Item("gun parts","random pieces from gun.")
    #pour construire son arme

bullets = Item("bullets","ammunition used with a gun.")
    #à équiper avec l'arme

muscle_work = Item("weight","common object in a gym to build muscles.")
    #se muscler

shelter_map = Item("map","allows you to find your way when you are lost.")
    #la carte"""

# Objects that can't move - - - - - - - - - - - - - - - - - - - - - - - - - - -

lever = Item("lever","- Opens the Vault door when actioned.", (0, 1))
    #permet d'ouvrir la porte pur sortir

button = Item("button","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (1, 1))
    #permet d'atteindre les autres etages
button = Item("button","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (1, 5))
    #permet d'atteindre les autres etages
button = Item("button","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (1, 9))
    #permet d'atteindre les autres etages

"""class alarm_button:
    pass

class jukebox:
    pass

class fountain:
    pass

class control_panel:
    pass

class medical_bed:
    pass

class microscope:
    pass

class machines:
    pass"""

# Objects with no specific use - - - - - - - - - - - - - - - - - - - - - - - - -

bottles = Item("bottles","- Bottles filled with fresh water.", (2, 2))
    #assouvi la soif

toolbox = Item("toolbox","- box containing several DIY tools. Repairs things broken.", (2, 6))
    #reparer les machines

adhesif_tape = Item("adhesif tape","- very sticky DIY adhesive tape.", (2, 4))
    #colmater les tuyaux

syringes = Item("syringes","- chemicals use for experiments on rats.",(2, 8))
    #produit chimique experimental

rats = Item("rats","- there is a little group of rats playing around.", (0, 5))
    #a faire evacuer avant de rentrer

"""class alarm_clock:
    pass

class plates:
    pass

class boxes:
    pass

class chemicals:
    #peut tuer si on les boits
    pass
"""

items.append(uniform.description)
items.append(watch.description)
items.append(broom.description)
items.append(notebook.description)
items.append(toolbox.description)
items.append(adhesif_tape.description)
items.append(armor.description)
items.append(gun.description)
items.append(lever.description)
items.append(button.description)
items.append(bottles.description)
items.append(syringes.description)
items.append(rats.description)

names.append(uniform.name)
names.append(watch.name)
names.append(broom.name)
names.append(notebook.name)
names.append(toolbox.name)
names.append(adhesif_tape.name)
names.append(armor.name)
names.append(gun.name)
names.append(lever.name)
names.append(button.name)
names.append(bottles.name)
names.append(syringes.name)
names.append(rats.name)

position.append(uniform.location)
position.append(watch.location)
position.append(broom.location)
position.append(notebook.location)
position.append(toolbox.location)
position.append(adhesif_tape.location)
position.append(armor.location)
position.append(gun.location)
position.append(lever.location)
position.append(button.location)
position.append(bottles.location)
position.append(syringes.location)
position.append(rats.location)
