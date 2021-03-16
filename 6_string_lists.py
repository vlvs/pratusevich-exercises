'''
Ask the user for a string and print out whether the string is a 
palindrome or not.
'''

user_input = input("\nEnter a string to check if it's a palindrome: ")

if user_input.lower() == user_input.lower()[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
