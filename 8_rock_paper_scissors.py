'''
Make a two-player Rock-Paper-Scissors game. Ask for players' moves 
using Python's input function, compare them, print out a message of 
congratulations to the winner, and ask if players want to play again.
'''

valid_moves = ["rock", "paper", "scissors"]

first_move_message = "Player #1, input your move: "
second_move_message = "Player #2, input your move: "
invalid_move_message = '''That's not a valid move.
Try typing in 'rock', 'paper' or 'scissors': '''

def get_first_move():
    global first_move
    first_move = input(first_move_message)
    while first_move.lower() not in valid_moves:
        first_move = input(invalid_move_message)
    return first_move

def get_second_move():
    global second_move
    second_move = input(second_move_message)
    while second_move.lower() not in valid_moves:
        second_move = input(invalid_move_message)
    return second_move

def resolve_play():
    if first_move == second_move:
        print(f"Both players used {first_move}. It's a tie.")
    elif first_move == "rock" and second_move == "paper":
        print("Paper covers rock. Player #2 wins!")
    elif first_move == "rock" and second_move == "scissors":
        print("Rock crushes scissors. Player #1 wins!")
    elif first_move == "paper" and second_move == "rock":
        print("Paper covers rock. Player #1 wins!")
    elif first_move == "paper" and second_move == "scissors":
        print("Scissors cuts paper. Player #2 wins!")
    elif first_move == "scissors" and second_move == "rock":
        print("Rock crushes scissors. Player #2 wins!")
    elif first_move == "scissors" and second_move == "paper":
        print("Scissors cuts paper. Player #1 wins!")

def play_again():
    play_again = input("Play again? (Y/n) ")
    if play_again.upper() == "Y": play()

def play():
    get_first_move()
    get_second_move()
    resolve_play()
    play_again()

play()
