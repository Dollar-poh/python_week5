import random

# functions

def ask_players_input():
    # variables
    random_number = random.randint(0, 2)
    comp_choices = ["Rock", "Paper", "Scissors"]
    computer = comp_choices[random_number]
    game_on = False

    # logic
    while game_on is False:
        player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()
        if (player1_input == "R") or (player1_input == "P") or (player1_input == "S"):
            game_on = True
            player_choice = convert_player_input(player1_input)
            # Added game results
            game_result = start_game(player_choice, computer)
            print(game_result)
            # start the game again?
            play_again()


def convert_player_input(letter):
    if letter == "R":
        return "Rock"
    elif letter == "P":
        return "Paper"
    else:
        return "Scissors"


def start_game(player_choice, computer):
    if player_choice == computer:
        return f"It's a draw! \nComputer input was {computer} \nand your input was {player_choice}"
    elif (player_choice == "Rock" and computer == "Scissors") or (player_choice == "Paper" and computer == "Rock") or (player_choice == "Scissors" and computer == "Paper"):
        return f"You Win!!! \nComputer input was {computer} \nand your input was {player_choice}"
    else:
        return f"Computer Wins!!! \nComputer input was {computer} \nand your input was {player_choice}"
# try to breakdown elifs in the functions above to make sure we get msgs like "scissor cuts paper "

def play_again():
    another_game = input("Shall we play again? 'Y' or 'N'\n").upper()
    if another_game == "Y":
        ask_players_input()
    elif another_game == "N":
        print("Have a great day!\t Play again soon")
    else:
        play_again()


ask_players_input()



    # else:
    #     player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()


    # while player1_input != "R" or "P" or "S":
    # print("Try again")
    # player1_input = input("Please type R for Rock, P for Paper or S for Scissors: >> \n").upper()

