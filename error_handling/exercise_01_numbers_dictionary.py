"""
Original code for review:

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]

print(numbers_dictionary)
"""

numbers_dictionary = {}


line_to_fill_dict = input()

while line_to_fill_dict != "Search":
    try:
        number_as_string = line_to_fill_dict
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line_to_fill_dict = input()


line_to_search_dict = input()

while line_to_search_dict != "Remove":
    try:
        searched = line_to_search_dict
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line_to_search_dict = input()


line_to_remove_from_dict = input()

while line_to_remove_from_dict != "End":
    try:
        to_remove = line_to_remove_from_dict
        del numbers_dictionary[to_remove]
    except KeyError:
        print("Number does not exist in dictionary")
        
    line_to_remove_from_dict = input()

print(numbers_dictionary)
