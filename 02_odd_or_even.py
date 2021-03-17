'''
Ask the user for a number. Print out a message stating whether the 
number is odd or even.

Extras:
1. If the number is a multiple of 4, print out a different message;
2. Ask the user for two numbers: divide one by the other and print out 
a message stating whether one divided evenly into the other or not.
'''

choice_message = '''
Choose an option:
(1) Check if a number is odd or even,
(2) Check if a number divides evenly into another.\n
'''
check_parity_message= "\nInput a number to check if it's odd or even:\n"
check_divisibility_dividend_message = "\nInput the dividend integer:\n"
check_divisibility_divisor_message = "\nInput the divisor integer:\n"
invalid_choice_message = "\nThat's not a valid option.\n"

def get_user_choice():
    user_choice = int(input(choice_message))
    return user_choice

def resolve_user_choice():
    if user_choice == 1: check_parity()
    elif user_choice == 2: check_divisibility()
    else: print_invalid_choice_message()

def check_parity():
    number = int(input(check_parity_message))
    if number % 4 == 0:
        print(f"\n{number} is even and also divisible by 4.")
    elif number % 2 == 0:
        print(f"\n{number} is an even number.")
    else:
        print(f"\n{number} is an odd number.")

def check_divisibility():
    dividend = int(input(check_divisibility_dividend_message))
    divisor = int(input(check_divisibility_divisor_message))
    if dividend % divisor == 0:
        print(f"\nThe dividend {dividend} is divisible by {divisor}.")
    else:
        print(f"\nThe dividend {dividend} is not divisible by {divisor}.")

def print_invalid_choice_message():
    print(invalid_choice_message)

user_choice = get_user_choice()
resolve_user_choice()
