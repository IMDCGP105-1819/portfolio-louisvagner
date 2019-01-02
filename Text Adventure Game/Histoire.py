import Salles
import Objets

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

inventory = []


#ask for input until the game isn't finished
while Victory == 0:
    while player_up == 0:
        wake = input().lower()
        if wake == "wake up":
            print("- You wake up from you bed, the alarm clock shows it's 8:10 in the morning.")
            player_up = 1
        elif wake == "look" or "go" or "take" or "use" or "drop":
            print("- You cannot do this action for the moment")

        elif wake != "wake up":
            print("- Invalid action or invalid syntax")
            
    playerinput = input().lower()

    if playerinput == "wake up":
        print("- You are already up")

        
    if playerinput == "look":
        print("- what do you want to look at ?")
        playerinput = input().lower()
        
    #inputs for all rooms
        if playerinput == "room":
            print(Salles.playerposition.description)
        
    #information on every objects in the item list
        if playerinput == "inventory":
            if inventory == []:
                print("- there is nothing in your inventory")
            else:
                print(inventory)
        if playerinput == "uniform":
            print(Objets.uniform.description)
        
        if playerinput == "watch":
            print(Objets.watch.description)

        if playerinput == "broom":
            print(Objets.broom.description)
        
        if playerinput == "notebook":
            print(Objets.notebook.description)
        
        if playerinput == "tape":
            print(Objets.adhesif_tape.description)

        if playerinput == "armors":
            print(Objets.armors.description)
        
        if playerinput == "guns":
            print(Objets.guns.description)

        if playerinput == "bottles":
            print(Objets.bottles.description)

        if playerinput == "syringes":
            print(Objets.syringes.description)

        if playerinput == "rats":
            print(Objets.rats.description)

        if playerinput == "lever":
            print(Objets.lever.description)

        if playerinput == "buttons":
            print(Objets.level_button.description)

    if playerinput == "take":
        print("- what do you want to take ?")
        playerinput = input().lower()

        #removing the object from where it is to the inventory
        if playerinput == "uniform":
            print("- your uniform has been added to your inventory")
            inventory.append("uniform")
        
        if playerinput == "watch":
            print("- your watch has been added to your inventory")
            inventory.append("watch")
           
        if playerinput == "broom":
            print("- a broom has been added to your inventory")
            inventory.append("broom")
          
        if playerinput == "notebook":
            print("- the notebook has been added to your inventory")
            inventory.append("notebook")
         
        if playerinput == "adhesif tape":
            print("- the adhesif tape has been added to your inventory")
            inventory.append("adhesif tape")
         
        if playerinput == "armors":
            print("- an armor has been added to your inventory")
            inventory.append("armors")
         
        if playerinput == "bottles":
            print("- a bottle has been added to your inventory")
            inventory.append("bottles")

        if playerinput == "syringes":
            print("- a syringe has been added to your inventory")
            inventory.append("syringes")
        
        if playerinput == "rats":
            print("- You can't take a rat with you")
          
        if playerinput == "lever":
            print("- You can't take the lever with you, it's a fixed object")
           
        if playerinput == "buttons":
            print("- You can't take the buttons with you, it's fixed in the wall")
         
    if playerinput == "drop":
        print("- what do you want to drop ?")
        playerinput = input().lower()

        #removing the object from the inventory to the room where the player is 
        if playerinput == "uniform":
            print("- You don't have anymore a uniform in your inventory")
            inventory.remove("bottles")
        
        if playerinput == "watch":
            print("- You don't have anymore a watch in your inventory")
            inventory.remove("watch")
        
        if playerinput == "broom":
            print("- You don't have anymore a broom in your inventory")
            inventory.remove("broom")
        
        if playerinput == "notebook":
            print("- You don't have anymore a notebook in your inventory")
            inventory.remove("notebook")
        
        if playerinput == "adhesif tape":
            print("- You don't have anymore a adhesif tape in your inventory")
            inventory.remove("adhesif tape")
        
        if playerinput == "armors":
            print("- You don't have anymore an armor in your inventory")
            inventory.remove("armors")
        
        if playerinput == "guns":
            print("- You don't have anymore a gun in your inventory")
            inventory.remove("guns")
        
        if playerinput == "bottles":
            print("- You don't have anymore a bottle in your inventory")
            inventory.remove("guns")
        
        if playerinput == "syringes":
            print("- You don't have anymore a syringes in your inventory")
            inventory.remove("syringes")
        
    if playerinput == "go north":
        pass
    if playerinput == "go south":
        pass
    if playerinput == "go east":
        pass
    if playerinput == "go west":
        pass
    if playerinput == "go up":
        pass
    if playerinput == "go down":
        pass

    if playerinput == "use Objets":
        pass

