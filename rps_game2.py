import random

# 1. Prompts the user to enter a value: R, P or S


def input_player_choice():
    player_choice = input("Enter R for Rock, P for Paper or S for Scissors:>> ").upper()
    while player_choice not in ["R", "P", "S"]:
        print("Invalid Entry")
        player_choice = input("Enter R for Rock, P for Paper or S for Scissors:>> ").upper()
    print("Player Input is ", player_choice)

    return player_choice

player_choice = input_player_choice()

# 2. The program should convert this value into Rock, Paper, or Scissors respectively


def convert_player_choice_to_string(player_choice):
# OPTION 1:
#     if player_choice == "R":
#         player_choice_str = "Rock"
#     elif player_choice == "P":
#         player_choice_str = "Scissors"
#     elif player_choice == "S":
#         player_choice_str = "Rock"
#     else:
#         print("Invalid Choice")
#
#     print("Player chose ", player_choice_str)
#
#     return player_choice_str
#
# player_choice_str = convert_player_choice_to_string(player_choice)

# OPTION 2
    player_choice_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    player_choice_str = player_choice_dict[player_choice]

    print("Player chose ", player_choice_str)

    return player_choice_str

player_choice_str = convert_player_choice_to_string(player_choice)


# 3. Asks the computer to generate a random value between 0 and 2

def comp_random_value():
    comp_choice = random.randint(0,2)
    return comp_choice
    print("Computer choice is ", comp_choice)
comp_choice = comp_random_value()


# 4. Convert the computer’s choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
def convert_comp_choice_to_string(comp_choice):
    comp_choice_list = ["Rock", "Paper", "Scissors"]