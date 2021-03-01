import random

# funtions
def convert_player_input(letter):
    if letter == "R":
        return "Rock"
    elif letter == "P":
        return "Paper"
    else:
        return "Scissors"


def playing(player_choice, computer):
    if player_choice == computer:
        return "It's a draw! Computer input was " + computer + " and your input was " + player_choice
    elif (player_choice == "Rock" and computer == "Scissors") or (player_choice == "Paper" and computer == "Rock") or (player_choice == "Scissors" and computer == "Paper"):
        return "You Win!!! Computer input was " + computer + " and your input was " + player_choice
    else:
        return "Computer Wins!!! Computer input was " + computer + " and your input was " + player_choice


# variables
random_number = random.randint(0, 2)
comp_choices = ["Rock", "Paper", "Scissors"]
computer = comp_choices[random_number]
# print(computer)
game_on = False

# logic
while game_on is False:
    player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()
    if (player1_input == "R") or (player1_input == "P") or (player1_input == "S"):
        game_on = True
        player_choice = convert_player_input(player1_input)
        # Added game results
        game_result = playing(player_choice, computer)
        print(game_result)
    # else:
    #     player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()











    # while player1_input != "R" or "P" or "S":
    # print("Try again")
    # player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()

