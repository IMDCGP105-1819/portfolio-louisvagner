import Salles, Objets, Personnage
import time

print("                                                                                                          "
      "......................................................................................................... "
      "                                                                                                          "
      "* * *   (Beginning of transmittion) - Hello fellow human, welcome to my game!  * * *                      "
      "                                                                                                          "
      "Here's the situation: due to some bad choices from the rulers of the Great Empires, nuclear centrals were "
      "left without care and without surpervision. This lack of attention brought to their explosion and the     "
      "spread of nuclear particules in the air. Civilisations are now forced to live in shelters. 704 Shelters   "
      "have been recorded around the world but more than half of the initial population perished...              "
      "                                                                                                          "
      "In this adventure you incarnate a worker in the shelter, you work in a Water treament plant. The incident "
      "that happened on the planet made you lose everything you cared about, your home, your wife and with her,  "
      "your will to live. Anger grew into you and all you want to have is revenge.                               "
      "                                                                                (End of transmition)      "
      "......................................................................................................... "
      "                                                                                                          "
      "                                                                                                          ")

player_up = 0
Victory = 0

print("- ZZzzz.....ZZzzzz....ZZzzzz..... ... ... ... ... ")

rm = Salles.search_room(Personnage.player.playerposition)

inventory = []
Used = []

inventory_position = Personnage.player.playerposition
print(Personnage.player.playerposition)
print(inventory_position)


#ask for input until the game isn't finished
while Victory == 0:
    while player_up == 0:
        wake = input().lower()
        if wake == "wake up":
            print("- you wake up from you bed, the alarm clock shows it's 8:10 in the morning.")
            player_up = 1
        elif wake == "look" or "go" or "take" or "use" or "drop":
            print("- you cannot do this action for the moment")

        elif wake != "wake up":
            print("- invalid action or invalid syntax")
            
    playerinput = input().lower()

    if playerinput == "wake up":
        print("- you are already up")


#move inputs  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    if playerinput == "move":
        if Objets.names[0] not in Used:
            print("You might want to wear your uniform instead of going out half naked.")
            time.sleep(3)

        if Objets.names[0] in Used:
            print("- in which direction do you want to move ?")
            playerinput = input("move ").lower()
            
            if playerinput == "north":
                Personnage.player.move(0, -1)
                rm = Salles.search_room(Personnage.player.playerposition)
                print("- you enter the " + rm.name)
                
            if playerinput == "south":
                Personnage.player.move(0, 1)
                rm = Salles.search_room(Personnage.player.playerposition)
                inventory_position = Personnage.player.playerposition
                print("- you enter the " + rm.name)
                print(Personnage.player.playerposition)
                print(inventory_position)
                print(Objets.position[1])
                
            if playerinput == "east":
                Personnage.player.move(1, 0)
                rm = Salles.search_room(Personnage.player.playerposition)
                print("- you enter the " + rm.name)
                
            if playerinput == "west":
                Personnage.player.move(-1, 0)
                rm = Salles.search_room(Personnage.player.playerposition)
                print("- you enter the " + rm.name)
                
            if playerinput == "up":
                Personnage.player.move(0,-4)
                rm = Salles.search_room(Personnage.player.playerposition)
                print("- you went up one floor.")
                
            if playerinput == "down":
                Personnage.player.move(0, 4)
                rm = Salles.search_room(Personnage.player.playerposition)
                print("- you came down one floor.")
                

#look input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    if playerinput == "look":
        print("- what do you want to look at ?")
        playerinput = input().lower()
        rm = Salles.search_room(Personnage.player.playerposition)
        
    #inputs for all rooms
        if playerinput == "room":
            print(rm.description)
            rm.print_items()
            print(rm.location)
        
    #information on every objects in the item list
        if playerinput == "inventory":
            if inventory == []:
                print("- there is nothing in your inventory")
            else:
                print(inventory)

        if playerinput == Objets.names[0]:
            if Personnage.player.playerposition != Objets.position[0]:    
                print("There is no uniform in this room.")
            if Personnage.player.playerposition == Objets.position[0]:
                print(Objets.items[0])
            
        if playerinput == Objets.names[1]:
            if Personnage.player.playerposition != Objets.position[1]:
                print("There is no watch in this room.")
            if Personnage.player.playerposition == Objets.position[1]:
                print(Objets.items[1])

        if playerinput == Objets.names[2]:
            if Personnage.player.playerposition != Objets.position[2]:
                print("There is no broom in this room.")
            if Personnage.player.playerposition == Objets.position[2]:
                print(Objets.items[2])
        
        if playerinput == Objets.names[3]:
            if Personnage.player.playerposition != Objets.position[3]:
                print("There is no botebook in this room.")
            if Personnage.player.playerposition == Objets.position[3]:
                print(Objets.items[3])
        
        if playerinput == Objets.names[5]:
            if Personnage.player.playerposition != Objets.position[5]:
                print("There is no adhesif tape in this room.")
            if Personnage.player.playerposition == Objets.position[5]:
                print(Objets.items[5])

        if playerinput == Objets.names[6]:
            if Personnage.player.playerposition != Objets.position[6]:
                print("There is no armor in this room.")
            if Personnage.player.playerposition == Objets.position[6]:
                print(Objets.items[6])
        
        if playerinput == Objets.names[7]:
            if Personnage.player.playerposition != Objets.position[7]:
                print("There is no gun in this room.")
            if Personnage.player.playerposition == Objets.position[7]:
                print(Objets.items[7])
        
        if playerinput == Objets.names[8]:
            if Personnage.player.playerposition != Objets.position[8]:
                print("There is no lever in this room.")
            if Personnage.player.playerposition == Objets.position[8]:
                print(Objets.items[8])
        
        if playerinput == Objets.names[9]:
            if Personnage.player.playerposition != Objets.position[9]:
                print("There is no buttons in this room.")
            if Personnage.player.playerposition == Objets.position[9]:
                print(Objets.items[9])
        
        if playerinput == Objets.names[10]:
            if Personnage.player.playerposition != Objets.position[10]:
                print("There is no bottles in this room.")
            if Personnage.player.playerposition == Objets.position[10]:
                print(Objets.items[10])

        if playerinput == Objets.names[11]:
            if Personnage.player.playerposition != Objets.position[11]:
                print("There is no syringes in this room.")
            if Personnage.player.playerposition == Objets.position[11]:
                print(Objets.items[11])

        if playerinput == Objets.names[12]:
            if Personnage.player.playerposition != Objets.position[12]:
                print("There is no rats in this room.")
            if Personnage.player.playerposition == Objets.position[12]:
                print(Objets.items[12])
        
            
#take input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    if playerinput == "take":
        print("- what do you want to take ?")
        playerinput = input().lower()

        #removing the object from where it is to the inventory
        if playerinput == Objets.names[0]:
            print("- you take your uniform under the arm.")
            inventory.append(Objets.names[0])
            rm.items.remove(Objets.names[0])
        
        if playerinput == Objets.names[1]:
            print("- You put your watch on our wrist.")
            inventory.append(Objets.names[1])
            Objets.position[1] == inventory_position
            rm.items.remove(Objets.names[1])
           
        if playerinput == Objets.names[2]:
            print("- you take the broom with you, the dust on it make you caugh a bit.")
            inventory.append(Objets.names[2])
            rm.items.remove(Objets.names[2])
          
        if playerinput == Objets.names[3]:
            print("- a notebook has been added to your inventory")
            inventory.append(Objets.names[3])
            rm.items.remove(Objets.names[3])
         
        if playerinput == Objets.names[5]:
            print("- an adhesif tape has been added to your inventory")
            inventory.append(Objets.names[5])
            rm.items.remove(Objets.names[5])
         
        if playerinput == Objets.names[6]:
            print("- You take the armor with you, it's really heavy though.")
            inventory.append(Objets.names[6])
            rm.items.remove(Objets.names[6])
            
        if playerinput == Objets.names[7]:
            print("- you take the gun ")
            inventory.append(Objets.names[7])
            rm.items.remove(Objets.names[7])
          
        if playerinput == Objets.names[8]:
            print("- Good luck trying to take the lever with you!")
           
        if playerinput == Objets.names[9]:
            print("- You can't take the buttons with you, it's fixed in the wall!")
         
        if playerinput == Objets.names[10]:
            print("- the bottles has been added to your inventory.")
            inventory.append(Objets.names[10])
            rm.items.remove(Objets.names[10])

        if playerinput == Objets.names[11]:
            print("- the syringes has been added to your inventory.")
            inventory.append(Objets.names[11])
            rm.items.remove(Objets.names[11])
        
        if playerinput == Objets.names[12]:
            print("- You might not want to touch the rats with bare hands.")
        
        #if playerinput != items in Objets.items:
        #print("it seems that the thing you want to take is not here")

            
#drop input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    if playerinput == "drop":
        print("- what do you want to drop ?")
        playerinput = input().lower()

        #removing the object from the inventory to the room where the player is 
        if playerinput == Objets.names[0]:
            print("- You leave your uniform on a chair or whatever you found.")
            inventory.remove(Objets.names[0])
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append(Objets.names[0])
        
        if playerinput == Objets.names[1]:
            print("- YOu take the watch off your wrist and place it on a table.")
            inventory.remove(Objets.names[1])
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append(Objets.names[1])
            Objets.position[1] = rm
            print(Objets.position[1])
        
        if playerinput == Objets.names[2]:
            print("- You get rid of the broom in a corner of the room.")
            inventory.remove(Objets.names[2])
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append(Objets.names[2])
        
        if playerinput == Objets.names[3]:
            print("- You don't have a notebook anymore in your inventory")
            inventory.remove(Objets.names[3])
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append(Objets.names[3])
        
        if playerinput == "adhesif tape":
            print("- You don't have an adhesif anymore tape in your inventory")
            inventory.remove("adhesif tape")
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append("adhesif tape")
        
        if playerinput == "armor":
            print("- You leave the armor on the floor, on the side, and feel realised.")
            inventory.remove("armor")
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append("armor")
        
        if playerinput == "gun":
            print("- You place the gun in a safe place of the room.")
            inventory.remove("gun")
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append("gun")
        
        if playerinput == "bottles":
            print("- You don't have bottles anymore in your inventory")
            inventory.remove("bottles")
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append("bottles")
        
        if playerinput == "syringes":
            print("- You don't have syringes anymore in your inventory")
            inventory.remove("syringes")
            rm = Salles.search_room(Personnage.player.playerposition)
            rm.items.append("syringes")

        #print("apparently you don't have this in your inventory.")
            
#use input - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

    if playerinput == "use":
        print("Which item do you want to use")
        playerinput = input().lower()

        #use the broom
        if playerinput == Objets.names[2]:
            if Objets.names[0] in inventory:
                print("Do you want to remove the dust or something else?")
                playerinput = input().lower()
                if playerinput == "dust":
                    print("you sweep the floor, there is no more dust in the room")
                if playerinput == Objets.names[12]:
                    print("You chase the rats from the room that are running away")
                    rm.items.remove(Objets.names[12])
                    
            else:
                print("- It's gonna be difficult to use a broom without having a broom.")

        #use the notebook
        if playerinput == Objets.names[3]:
            if Objets.names[3] in inventory:
                print("- Do you want to write in it or to read your notes?")
                playerinput = input().lower()
                if playerinput == "write":
                    noteinput = input("*Shelter 641 Journal* : ")
                if playerinput == "read":
                    print("- Here are your previous notes : " + noteinput)
                    
        #use the watch
        if playerinput == Objets.names[1]:
            if Objets.names[1] in inventory:
                print("- the hands of the watch do not seem to move,seems that there is no battery.")
            else:
                print("- There is no watch on your wrist, you forgot to put it on.")

    #wear the uniform or the armor
    if playerinput == "wear":
        print("- What do you want to wear ?")
        playerinput = input().lower()
        
        if playerinput == Objets.names[0]:
            if Objets.names[0] in inventory:
                print("- You now wear your uniform, you can freely move in the vault.")
                inventory.remove(Objets.names[0])
                Used.append(Objets.names[0])
            else:
                print("- You don't have this equipment in your inventory")

        if playerinput == Objets.names[7]:
            if Objets.names[7] in inventory:
                print("- You are now equiped with a fighting armor.")
                inventory.remove(Objets.names[7])
            else:
                print("- You don't have this equipment in your inventory")
