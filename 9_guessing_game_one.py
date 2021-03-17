'''
Generate a random number between 1 and 9. Ask the user to guess the 
number, then print whether it's too low, too high, or exactly right.

Extras:
1. Keep the game going until the user types 'exit';
2. Keep track of how many guesses the user has taken, print out that 
information when the game ends.
'''

import random

guess_count = 0

def generate_random_number():
    global random_number
    random_number = random.randint(1, 9)

def get_first_user_input():
    global user_input
    user_input = input("Guess the random number between 1 and 9: ")
    increment_guess_count()

def increment_guess_count():
    global guess_count
    guess_count += 1

def reset_guess_count():
    global guess_count
    guess_count = 0

def evaluate_guesses():
    global user_input
    while user_input.lower() != "exit":
        if int(user_input) < random_number:
            user_input = input("Your guess is too low. Try again: ")
            increment_guess_count()
        elif int(user_input) > random_number:
            user_input = input("Your guess is too high. Try again: ")
            increment_guess_count()
        else:
            print(f"Exactly right! That took {guess_count} attempt(s).")
            reset_guess_count()
            play()

def play():
    generate_random_number()
    get_first_user_input()
    evaluate_guesses()

play()
