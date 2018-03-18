#!/usr/bin/env python3

a_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

# SERIES 1
def series_one():
    print(a_list)
    another_fruit = input("Enter a new fruit: ")
    a_list.append(another_fruit)
    print(a_list)
    number_from_user = input("Now enter number corresponding to fruit: ")
    new_number = a_list[int(number_from_user)-1]
    print(new_number + " " + number_from_user)
    another_fruit = ['Bananas']
    print(another_fruit + a_list)
    next_fruit = 'Kiwis'
    a_list.insert(0, next_fruit)
    print(a_list)
    for i in a_list:
        if i.startswith("P"):
            print(i)

#series_one()

# SERIES 2

def series_two():
    print(a_list)
    a_list.pop()
    print(a_list)
    ask_to_remove_fruit = input("Which fruit should we delete: ")
    for fruit in a_list:
        if ask_to_remove_fruit in a_list:
            a_list.remove(ask_to_remove_fruit)
            print(a_list)
#series_two()

# SERIES 3

def series_three():
    new_list = a_list[:]
    for i in a_list:
        answer = input("Do you like " + i.lower() + "? ")
        while answer != "yes" and answer != "no":
            answer = input("Please enter yes or no: ")
        if answer == "no":
            new_list.remove(i)
    print(new_list)

#series_three()

# SERIES 4

def series_four():
    new_list = a_list.copy()
    list_items_reversed = []
    for item in new_list:
        new_item = item[::-1]
        list_items_reversed.append(new_item)
    a_list.pop()
    print(a_list)
    print(list_items_reversed)

#series_four()
