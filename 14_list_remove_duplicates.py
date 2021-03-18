'''
Write a function that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicate elements.

Extra: Write two different functions to do this, one using a loop to 
construsct the new list, another using sets.
'''

sample_list = ["Arya", "Daenerys", "Daenerys", "Ygritte", "Ygritte"]

def remove_duplicates(list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list

def convert_to_set(list):
    return set(list)

print(sample_list)
print(remove_duplicates(sample_list))
print(sorted(convert_to_set(sample_list)))
