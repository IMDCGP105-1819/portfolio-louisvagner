# Important objects - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

items = []

items.append(Item("uniform", "vault uniform"))
items.append(Item("watch", ""))
items.append(Item("broom", ""))
items.append(Item("notebook", ""))
items.append(Item("adhesif_tape", ""))
items.append(Item("armors", ""))
items.append(Item("guns", ""))
items.append(Item("bottles", ""))
items.append(Item("syringes", ""))
items.append(Item("rats", ""))

uniform = Item("uniform","shirt and trouser representative of the vault you are in.")
    #A mettre sinon <<Intrusion>>

watch = Item("watch","bracelet giving the time.")
    #avoir une idée de l'heure

broom = Item("broom","long broom that helps get rid of dust.")
    #chasser les rats
             
notebook = Item("notebook","block with several sheets of paper, it is possible to write in if used.")
    #permet d'ecrire ce qu'on veut

toolbox = Item("toolbox","box containing several DIY tools. Repairs things broken.")
    #reparer les machines

adhesif_tape = Item("adhesif tape","very sticky DIY adhesive tape.")
    #colmater les tuyaux

armors = Item("armors","protection for the body used for combat.")
    #augmente la défense

guns = Item("guns","firearm used to defend or kill.")
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

lever = Item("lever","Opens the Vault door when actioned.")
    #permet d'ouvrir la porte pur sortir

level_button = Item(" press button","Can lead you to the lower and upper levels of the vault, just press the buttons.")
    #eteindre le feu

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

bottles = Item("bottles","Bottles filled with fresh water.")
    #assouvi la soif

syringes = Item("syringes","chemicals use for experiments on rats.")
    #produit chimique experimental

rats = Item("rats","there is a little group of rats playing around.")
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
