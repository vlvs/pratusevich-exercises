'''
Ask the user for a number and determine whether the number is prime. 
Define functions for the solution.
'''

def get_user_input():
    global input
    input = int(input("Input an integer to check its primality: "))

def primality_of(number) -> bool:
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def print_information_on_input_primality():
    if primality_of(input) is True:
        print(f"{input} is a prime number!")
    else:
        print(f"{input} is not a prime number.")

get_user_input()
print_information_on_input_primality()
