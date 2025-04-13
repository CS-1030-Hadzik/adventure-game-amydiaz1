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
# Function: welcome_player
# Greets the player, asks for their name,
# and returns the name as a string
# ------------------
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

# ---------------
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
   
# ---------------------------------------------------------
# Function: add_to_inventory
# Accepts an item name as a parameter
# adds it to the inventory list,
# and confirm the pickup to the player 
# ----------------------------------------------------------

def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

#------------------------------------------------------------
# Game starts here
# Call the welcome and describe area functions
#------------------------------------------------------------


player = welcome_player()
describe_area()

# TODO: Add a new menu option for "Search for a hidden valley"
# TODO: In the cave choice:
#       - If player.has_lantern is True: allow entry and add "treasure" to inventory
#       - Else: display a message that it’s too dark
# TODO: In the valley choice:
#       - If player.has_map is True: allow entry and add "rare herbs" to inventory
#       - Else: display a message that you can’t find the valley
# TODO: After picking up new items, confirm to the player they got it
# TODO: Save your changes (Ctrl+S or Command+S)
# TODO: Commit with a message like:
#       REF unlock new areas based on inventory items
# TODO: Push your commits to GitHub

#------------------------------------------------------------

# Main game loop
# run this until the player quiesent
#------------------------------------------------------------

# Start the game Loop
while True: 
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Explore a nearby cave.")
    print("\t4. Search for a hidden valley.")
    print("\t5. Stay where you are.")
    print("\tType 'i' to view your inventory.")


    decision = input("What will you do (1,2,3,4,5 or i): ").lower()

    # open the inventory 
    if decision == 'i':
        print("inventory", player.inventory)
        continue

     # take the left path --- Dark woods
    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory("latern")
        player.has_lantern = True

    # take the right path --- Mountain
    elif decision == "2":
        print(f"{player.name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory("map")
        player.has_map = True

    # Enter the cave, only if they have latern in inventory 
    elif decision == "3":

        # if they have latern 
        if player.has_lantern:
            print(f"{player.name}, bravely enter the dark cave")
            print(f"Inside the cave, you find hidden treasure!")
            add_to_inventory(player, "treasure")

        # if no lantern
        else: 
            print("It's too dark to explore the cave without a latern")
            print("Maybe you should find a light source.")

    elif decision == "4":
        # Conditional Logic: need map to find hidden valley 
        if player.has_map:
            print(f"{player.name}, you study the map carefully...")
            print("You discover a hidden path to a beautiful secret valley filled with rare herbs.")
            add_to_inventory(player, "rare herbs")
        else:
            print("You wander in circles, unable to find anything special without a map.")

    # stay where you are
    elif decision == "5": 
        print(f"You stay still, listening to the distant sounds of the forest.")
    else: 
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 'i'.")
    
    # Ask if they want to continue
    play_again = input("Do you want to coninue exploring? (yes or no):").lower()

    if play_again != "yes":
        print(f"Thanks for playing, {player.name}, see you next time.")

        break # Exit the loop and end the game