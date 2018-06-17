#!/usr/bin/env python3

fruit_list = [ “Apples”, “Pears”, “Oranges”, “Peaches”]

print(fruit_list)

# Ask for another fruit
new_fruit = input("Enter another fruit > ")

fruit_list.append(new_fruit)

print(fruit_list)

# Ask for another fruit
fruit_number = input("Enter a number > ")

print(fruit_number, fruit_list[fruit_number - 1])

# Add more fruits
fruit_list = "Cherries" + fruit_list

print(fruit_list)

fruit_list = fruit_list.insert(0, "Blueberries")

# Show all "P" fruits
for fruit in fruit_list:
    if fruit[0] == 'P':
        print(fruit)