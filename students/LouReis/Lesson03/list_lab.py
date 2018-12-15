#!/usr/bin/env python3
# list_lab.py

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
response = [input("Enter the name of another fruit> ")]
fruit_list = fruit_list + response
print(fruit_list)
fruit_list.append(response)
