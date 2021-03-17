'''
Take two randomly generated lists and return a list that contains only 
the elements that are common between the lists, without duplicates.

Make sure your program works on two lists of different sizes and use at 
least one list comprehension.
'''

import random

def generate_random_list():
    random_list = random.sample(range(100), random.randint(0, 30))
    return random_list

def generate_list_overlap(first_list, second_list):
    overlap_list = [x for x in first_list if x in second_list]
    return overlap_list

print(generate_list_overlap(generate_random_list(), generate_random_list()))
