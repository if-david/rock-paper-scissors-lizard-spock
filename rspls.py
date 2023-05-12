# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to comp_numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# Libraries and variables
import random
import os
os.system("cls")


# compute random guess for comp_comp_number using random
comp_number = random.randint(0, 4)
comp_choice = ''

#Contadores con valores de inicio
player_number = 0

# mensajes de inicio
print("Welcome to Rock-paper-scissors-lizard-Spock")
os.system("pause") #Pasa a la siguiente pantalla

# helper functions

# convert the player_choice to player_number using the function player_choice_to_player_number()
def player_choice_to_player_number(player_choice):
    # convert player_choice to comp_number using if/elif/else
    if player_choice == "rock":
        player_number = 0
    elif player_choice == "spock":
        player_number = 1
    elif player_choice == "paper":
        player_number = 2
    elif player_choice == "lizard":
        player_number = 3
    elif player_choice == "scissors":
        player_number = 4
    else:
        print("Please enter a valid choice! \n")
        player_number = None
    # don't forget to return the result!
    return player_number

# convert comp_comp_number to comp_choice using the function comp_number_to_comp_choice()
def comp_number_to_comp_choice(comp_number):
    # delete the following pass statement and fill in your code below
    if comp_number == 0:
        comp_choice = 'rock'
    elif comp_number == 1:
        comp_choice = 'spock'
    elif comp_number == 2:
        comp_choice = 'paper'
    elif comp_number == 3:
        comp_choice = 'lizard'
    elif comp_number == 4:
        comp_choice = 'scissors'
    return comp_choice
    
    
    # convert comp_number to a player_choice using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    player_number = player_choice_to_player_number(player_choice)
    # print out the message for the player's choice
    print(f'Player chooses {player_choice}')
    print(f'Computer chooses {comp_number_to_comp_choice(comp_number)}')
    result = player_number - comp_number
    if result == 0:
        print('Player and computer tie!')
    if result < 0:
        print('Computer wins!')
    else:
        print('Player wins!')
    # print a blank line to separate consecutive games
    print()
        
    
    

    

    

    

    
    
    # print out the message for computer's choice

    # compute difference of comp_comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls('rock')
rpsls('spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

# always remember to check your completed program against the grading rubric


