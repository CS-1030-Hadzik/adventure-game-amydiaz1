'''
DOCSTRING
Adventure Game
Author: Amy Diaz
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# Welcome message and introducton
print("Welcome to the Adventure Game!")  
print('Your journey begins here...')

# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concatenate strings to create a personalized message
print("Welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more readable way 
print(f"Welcome, {player_name}! Your journey begins now.")

#Describe the starting area 
starting_area = """
You find yourself in a dark forest
The sound of rustling leaves fills the air
A fainy path lies ahead, leading deeper into the 
unknown...
"""
print(starting_area)

# Start the game Loop
while True: 
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")

    decision = input("What will you do (1,2,3): ")
    if decision == "1":
        print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
    elif decision == "2":
        print(f"{player_name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
    elif decision == "3": 
        print(f"You stay still, listening to the distant sounds of the forest.")
    else: 
        print("Invalid choice. Please choose 1, 2, or 3.")
# # Ask the player for their first decision
# decision = input("Do you wish to take the path (yes or no): ").lower()

# # Invalied reponse loop until they give a valid response 
# while decision not in ["yes", "no"]: 
#     print("Invalid choice. Please type 'yes'or'no'.")
#     # option for the user to make a new decision
#     decision = input("Do you wish to take the path (yes or no): ").lower()

# # Respond based on the player's decision
# if decision == "yes":
#     print (f"Brave choice, {player_name}! You step on the path and venture foward")
# elif decision == "no":
#     print (f"{player_name} , you decide to wait. Perhaps courge will find you later.")
# else:
#     print("Confused, you stand still, unsure of what to do.")