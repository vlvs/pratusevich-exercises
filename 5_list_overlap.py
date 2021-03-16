'''
Take two lists and write a program that returns a list that contains 
only the elements that are common between the lists, without duplicates.
Make sure your program works on two lists of different sizes.

Extras:
1. Use two randomly generated lists;
2. Write this in one line of Python.
'''

import random

first_random_list = random.sample(range(100), random.randint(0, 30))
second_random_list = random.sample(range(100), random.randint(0, 30))
overlap_list = [x for x in first_random_list if x in second_random_list]

print(f'''
List #1:\n{sorted(first_random_list)}

List #2:\n{sorted(second_random_list)}

Overlap:\n{sorted(overlap_list)}
''')
