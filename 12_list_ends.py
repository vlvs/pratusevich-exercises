'''
Write a program that takes a list of numbers and makes a new list of 
only the first and last elements of the original list.
'''

import random

def sample_list():
    return random.sample(range(100), random.randint(0, 30))

def extract_list_ends(input_list):
    return [input_list[0], input_list[len(input_list)-1]]

print(extract_list_ends(sample_list()))
