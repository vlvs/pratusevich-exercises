'''
Write a password generator. Strong passwords have a mix of lowercase 
letters, uppercase letters, numbers, and symbols. The passwords should 
be random, a new password should be generated every time the user asks 
for a new password. Include your run-time code in a main method.

Extra: Ask the user how strong they want their password to be. For weak 
passwords, pick a word or two from a list.
'''

import random
import string

fruits = ["apple", "banana", "lemon", "mango", "orange", "tangerine"]
password_strength_levels = ["1", "2", "3", "weak", "so-so", "strong"]
password_strength_message = '''How strong do you want your password to be?
(1) Weak\n(2) So-So\n(3) Strong\n'''
password_strength_invalid_message = '''Invalid input. Choose '1', '2' or '3':
(1) Weak\n(2) So-So\n(3) Strong\n'''
available_characters = [
    string.ascii_lowercase, 
    string.ascii_uppercase, 
    string.punctuation, 
    string.digits
    ]

def get_password_strength():
    global password_strength
    password_strength = input(password_strength_message)
    while password_strength.lower() not in password_strength_levels:
        password_strength = input(password_strength_invalid_message)
    if password_strength.lower() == "weak": password_strength = "1"
    if password_strength.lower() == "so-so": password_strength = "2"
    if password_strength.lower() == "strong": password_strength = "3"

def generate_weak_password():
    return ''.join(random.choices(fruits, k = 2))

def generate_password(strength):
    if password_strength == "1": return ''.join(random.choices(fruits, k = 2))
    password = []; chars_per_group = 2
    if password_strength == "3": chars_per_group = 5
    for group in available_characters:
        password.append(''.join(random.choices(group, k = chars_per_group)))
    password = list(''.join(password))
    random.shuffle(password)
    return ''.join(password)

get_password_strength()
print(f"Here's the generated password: {generate_password(password_strength)}")
