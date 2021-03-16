'''
Write one line of Python that takes a previsouly generated random list 
and makes a new list that has only the even elements of the random list.
'''

import random

random_list = random.sample(range(100), random.randint(0, 30))
even_list = [number for number in random_list if number % 2 == 0]

print(f'''
The random list:\n{sorted(random_list)}

The list containing only its even elemenets:\n{sorted(even_list)}
''')
