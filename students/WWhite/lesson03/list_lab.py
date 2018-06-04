#!/usr/bin/env python3

# -------------------------------------#
# Desc: Slicing Lab
# Dev: Will White
# Date: 4/8/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#


def series_1():
    list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(list_fruit)
    list_fruit.append(input("Please input a fruit to add to the list: "))
    print(list_fruit)
    index_input = input("Please input a number: ")
    print(list_fruit[int(index_input)-1])
    fruit_plus = input("Please input another fruit to the list: ")
    list_fruit = [fruit_plus] + list_fruit
    print(list_fruit)
    fruit_insert = input("Please input another fruit to the list: ")
    list_fruit.insert(0, fruit_insert)
    print(list_fruit)
    for i in range(len(list_fruit)):
        if list_fruit[i][0] == 'p':
            print(list_fruit[i])


def series_2():
    list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(list_fruit)
    list_fruit.pop()
    print(list_fruit)
    fruit_delete = input("Please input the name of a fruit you would like to delete: ")
    for i in list_fruit:
        if i.lower() == fruit_delete.lower():
            list_fruit.remote(i)


def series_3():
    list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    new_list = list_fruit[:]
    for i in list_fruit:
        user_response = input("Do you like " + i + "? ")
        while user_response.lower() != 'yes' and user_response.lower() != 'no':
            user_response = input("Please answer 'yes' or 'no': ")
        if user_response.lower() == 'no':
            new_list.remove(i)
    print(new_list)


def series_4():
    list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    new_list_fruit = list_fruit[:]
    for i in range(len(new_list_fruit)):
        new_list_fruit[i] = new_list_fruit[i][-1::-1]
    list_fruit.pop()
    print(list_fruit)
    print(new_list_fruit)
