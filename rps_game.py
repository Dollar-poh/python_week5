import random

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
        return  "You Win!!! Computer input was " + computer + " and your input was " + player_choice
    else:
        return "Computer Wins!!! Computer input was " + computer + " and your input was " + player_choice



player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()

x = random.randint(0, 2)
comp_choices = ["Rock", "Paper", "Scissors"]
computer = comp_choices[x]
# print(computer)


game_on = False
while game_on == False:
    if (player1_input == "R") or (player1_input == "P") or (player1_input =="S"):
        game_on = True
        player_choice = convert_player_input(player1_input)
        print(playing(player_choice, computer))
    else:
        player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()











    # while player1_input != "R" or "P" or "S":
    # print("Try again")
    # player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()

