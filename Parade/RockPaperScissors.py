import random


def determine_outcome(player_move, computer_move):
    if (player_move == "ROCK"):
        if (computer_move == "Rock"):
            print("Draw, no points.")
        elif (computer_move == "Paper"):
            print("Paper covers Rock, computer scores!")
        else:
            print("Rock smashes scissors, player scores!")
    if (player_move == "PAPER"):
        if (computer_move == "Paper"):
            print("Draw, no points.")
        elif (computer_move == "Rock"):
            print("Paper covers Rock, player scores!")
        else:
            print("Scissors cuts paper, computer scores!")
    if (player_move == "SCISSORS"):
        if (computer_move == "Scissors"):
            print("Draw, no points.")
        elif (computer_move == "Rock"):
            print("Paper covers Rock, player scores!")
        else:
            print("Scissors cuts paper, computer scores!")


def rpsgame():
    player_score = 0
    computer_score = 0
    moves = ["Rock", "Paper", "Scissors"]
    player_move = input(f"Make your move({moves}): ").upper()
    computer_move = random.choice(moves)
    print("Computer's move: " + computer_move)
    determine_outcome(player_move, computer_move)


rpsgame()
