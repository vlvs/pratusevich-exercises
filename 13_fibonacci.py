'''
Write a program that asks the user how many Fibonacci numbers to 
generate and then prints them out.
'''

def get_length():
    return int(input("How many Fibonacci numbers should be generated? "))

def fibonacci_sequence(length):
    sequence = [0, 1]
    if length == 1:
        return [sequence[0]]
    if length == 2:
        return sequence
    if length >= 3:
        for number in range(length):
            last_value = sequence[len(sequence)-1]
            second_last_value = sequence[len(sequence)-2]
            if number > 1: sequence.append(last_value + second_last_value)
        return sequence

print(fibonacci_sequence(get_length()))
