'''
DOCSTRING
Adventure Game
Author: Amy Diaz
Version: 2.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

#------------------------------------------------------------------------
# Player class to sotre player info and game state
# ----------------------------------------------------------------------
class Player: 
    # initializer - constructor
    def __init__(self, name):
        self.name = name 
        self.inventory = []
        self.health = 100 
        self.has_map = False 
        self.has_lantern = False 
# ---------------

# -------------------------
# Function: describe_area
# Print the opening description of the area
# ------------------
def describe_area():
    # Describe the starting area 
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A fainy path lies ahead, leading deeper into the 
    unknown...
    """)
   
# ----------------------------------------------------------

def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# stay still ---------------------------------------
def stay_still(player):
    print("You stay still, you feel as if you are being watched.")
    print("It starts to get to you.")
    player.health -= 10
    print(f"{player.name}, your health is now {player.health.}.")



def explore_dark_woods(player):
        print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")

        # if they do not have the lantern
        if "lantern" not in player.inventory:
            add_to_inventory("latern")
            player.has_lantern = True
        else: 
            print("You've already found the lantern here!")
# if they do have lantern message

def explore_mountain_pass(player):
    print(f"{player.name}, you head toward the mountain pass...")
    if "map" not in player.inventory:
        add_to_inventory(player, "map")
        player.has_map = True
    else:
        print("You've already picked up")

def explore_cave(player):
        print("You walk up to the entracne of the cave."
        "It appears to be dark inside.")
    if player.has_lantern == True:
            print(f"{player.name} you bravely enter the cave")
            print("Inside the cave, you find a treasure chest!")
            add_to_inventory(player, "Treasure")

    if player.has_lantern == False:
            print("You can't see far enough to travel safely.")
            print("You need a light source to explore further.")
            print("You feel a precence approaching.")
            print("As fear consomes you, you run away.")
            print("You trip from running away")
            player.health -= 10

def explore_hidden_valley(player):
        print("You search for a place called hidden valley.")

    if player.has_map == True:
            print("You find a hidden valley, "
                  "a place of beauty and tranquility.")
            print("You can rest here and regain your strength.")
            player.health = 100
            print("Your health is now full.")
            print("You find a treasure chest!")
            add_to_inventory(player, "Rare Herbs")
            print("You have found rare herbs.")

    if player.has_map == False:
            print("You can't seem to find Hidden Valley.")
            print("You may need guidance of some kind.")       
            player.health -= 10 

#-----------------------------------------------------------------

def check_win(player):
    return "Treasure" in player.inventory and "Rare Herbs" in player.inventory

def check_lose(player):
    return player.health <= 0
#------------------------------------------------------------
# Game starts here
# Call the welcome and describe area functions
#------------------------------------------------------------
def welcome_player():
    # Welcome message and introducton
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here...')

    # Ask for the player's name
    name = input("What is your name, adventurer?")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way 
    print(f"Welcome, {player.name}! Your journey begins now.")

    return player


player = welcome_player()
describe_area()


#------------------------------------------------------------

# Main game loop
# run this until the player quiesent
#------------------------------------------------------------

# Start the game Loop
while True: 
    print("\nYou see mutiple paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Explore a nearby cave.")
    print("\t4. Search for a hidden valley.")
    print("\t5. Stay where you are.")
    print("\tType 'i' to view your inventory.")
    print("\tCurrent Health: {player.health}")


    decision = input("What will you do (1,2,3,4,5 i or F): ").lower()

    # open the inventory 
    if decision == 'i':
        print("inventory", player.inventory)
        continue

    if decision == "1":
        explore_dark_woods(player)

    # take the right path --- Mountain
    elif decision == "2":
        explore_mountain_pass(player)

    # Enter the cave, only if they have latern in inventory 
    elif decision == "3":
        explore_cave(player)

    # hidden valley 
    elif decision == "4":
       explore_hidden_valley(player)

    # stay where you are
    elif decision == "5": 
        print(f"You stay still, listening to the distant sounds of the forest.")
        stay_still(player)

    else: 
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, i or F.")
    
#-------------------------------------------------------------------------------

    #win 
    if check_win(player):
        print(f"\nCongratulations {player.name}! You have found both the treasure and the rare herbs.")
        print("You are victorious and can now leave the forest.")
        break
    #lose
    if check_lose(player):
        print(f"\n{player.name}, you have ran out of health. Your adventure ends here....")
        break

    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break  # Exit the loop and end the game