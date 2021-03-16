'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.

Extra: Ask the user for another number and print out that many copies 
of the previous message.
'''

from datetime import datetime

user_name = input("\nWhat's your name?\n")
user_age = int(input("\nHow many years of age do you complete this year?\n"))
number_of_copies = int(input("\nInput a random number:\n"))

current_year = datetime.now().year
hundredth_year = current_year - user_age + 100

message = f"\n{user_name}, you're gonna be 100 years old in {hundredth_year}."
print(number_of_copies * message)
