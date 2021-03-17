'''
Create a program that asks the user for a number and then prints out a 
list of all the divisors of that number.
'''

user_input = int(input("\nEnter a number to print out its divisors:\n"))

possible_divisors = range(1, user_input+1)
divisor_list = [x for x in possible_divisors if user_input % x == 0]

print(f"\nHere's the list of divisors of {user_input}:\n{divisor_list}")
