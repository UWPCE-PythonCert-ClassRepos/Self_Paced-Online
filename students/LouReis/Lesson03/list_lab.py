#!/usr/bin/env python3
# list_lab.py

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
response = [input("Enter the name of another fruit> ")]
fruit_list = fruit_list + response
print(fruit_list)
# fruit_list.append(response)
pick = input("Enter a number to pick a fruit in the list> ")
pick_int = int(pick)
pick_int = pick_int - 1
print(fruit_list[pick_int])
fruit_list = ['Bananas'] + fruit_list
print(fruit_list)
fruit_list.insert(0, 'Kiwi')
print(fruit_list)
