import random

# This is the python code for Lab 2 of Week 2


# Define the array
choices = ["Rock", "Paper", "Scissors"]

# Get player input
print("Choose your option:")
print("1: Rock")
print("2: Paper")
print("3: Scissors")
player_choice = int(input("Enter your choice (1, 2, 3): "))

# Error handling for valid input
while player_choice < 1 or player_choice > 3:
    print("Error: Choice must be between 1 and 3")
    player_choice = int(input("Enter your choice (1, 2, 3): "))
    
# Computer's choice using random
computer_choice = random.randint(1, 3)

computer_choice = computer_choice - 1  # Adjust for zero indexing
player_choice = player_choice - 1  # Adjust for zero indexing

print("You chose: " + choices[player_choice])
print("Computer chose: " + choices[computer_choice])

# Determine the winner
if(computer_choice == player_choice):
    print("It's a tie! Both chose " + choices[player_choice])
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print(choices[player_choice] + " beats " + choices[computer_choice] + " –– You win!" )
else:
    print(choices[computer_choice] + " beats " + choices[player_choice] + " –– Computer wins" )

if(choices[player_choice] != "Rock"):
        print("You didn't pick the classic Rock...")