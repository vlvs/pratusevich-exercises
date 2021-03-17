'''
Take a list of numbers and write a program that prints out all the 
elements of the list that are less-than 10.

Extras:
1. Instead of printing the elements one by one, make a new list that 
has all the elements less-than 10 from the original list in it and 
print out this new list;
2. Ask the user for a number and return a list that contains only 
elements from the original list that are smaller than the number given 
by the user.
'''

sample_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
threshold = int(input("\nInput a threshold for the new list:\n"))
new_list = [number for number in sample_list if number < threshold]

print(f"\nHere's the new list: {new_list}")
