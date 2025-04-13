'''
DOCSTRING
Adventure Game
Author: Amy Diaz
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# TODO: Create an empty list called `inventory` at the top of your code.
#       This will store items the player picks up during the game.

# ---------------
# Global inventory list
# This will hold items the player collects
# --------------
inventory = []

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
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way 
    print(f"Welcome, {player_name}! Your journey begins now.")

    return player_name 

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
    inventory.append(item)
    print(f"You picked up a {item}!")

#------------------------------------------------------------
# Game starts here
# Call the welcome and describe area functions
#------------------------------------------------------------


player_name = welcome_player()
describe_area()

#------------------------------------------------------------

# Main game loop
# run this until the player quiesent
#------------------------------------------------------------

# Start the game Loop
while True: 
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\tType 'i' to view your inventory.")


    decision = input("What will you do (1,2,3 or i): ").lower()

    if decision == 'i':
        print("inventory", inventory )
        continue

    if decision == "1":
        print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory("latern")

    elif decision == "2":
        print(f"{player_name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory("map")

    elif decision == "3": 
        print(f"You stay still, listening to the distant sounds of the forest.")
    else: 
        print("Invalid choice. Please choose 1, 2, or 3.")
    
    # Ask if they want to continue
    play_again = input("Do you want to coninue exploring? (yes or no):").lower()

    if play_again != "yes":
        print(f"Thanks for playing, {player_name}, see you next time.")

        break # Exit the loop and end the game