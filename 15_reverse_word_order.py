'''
Write a program that asks the user for a string containing multiple 
words. Print back the same string with the words in reverse order.
'''

def multi_word_string():
    string_input = input("Input a string with multiple words: ")
    while len(string_input.split()) <= 1:
        string_input = input("That was only one word. Try again: ")
    return string_input

def reverse(input):
    return " ".join(input.split()[::-1])

print(reverse(multi_word_string()))
