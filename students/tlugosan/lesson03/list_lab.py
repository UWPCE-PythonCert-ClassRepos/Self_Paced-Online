#! python

# region SERIES1
"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”"""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

"""Display the list"""
print(fruit_list)

"""Ask for another fruit and add it to the end"""
response1 = input("Please provide another fruit: ")
fruit_list.append(response1.capitalize())

"""Display list."""
print(fruit_list)
print()

"""Ask for a number and display the number and the corespnding fruit on a 1-is basis."""
response2 = int(
    input("Please provide a number between 1 and %s: " % len(fruit_list)))
while True:
    if response2 < 1 or response2 > len(fruit_list):
        response2 = int(
            input("Try again a number between 1 and %s: " % len(fruit_list)))
    else:
        break
print("%d : %s" % (response2, fruit_list[response2 - 1]))
print()

"""Add another fruit at the beginning of the list using +  then print the list"""
response3 = input("Please provide another fruit: ")
fruit_list = [response3.capitalize()] + fruit_list
print(fruit_list)
print()

""" Add another fruit at the beginning at the list using insert() function"""
response4 = input("Please provide another fruit: ")
fruit_list.insert(0, response4.capitalize())
print(fruit_list)
print()

"""Display all the fruits that start with P using a for loop"""
print("Fruit that start with letter P: ", end=" ")
for item in fruit_list:
    if item.startswith("P"):
        print(item, end=" ")

print()
# endregion

# region SERIES2
"""Display the fruit list."""
print(fruit_list)

"""Remove the last fruit from the list."""
fruit_list.remove(fruit_list[len(fruit_list) - 1])
print("Last fruit from the list was removed")

"""Display list."""
print(fruit_list)
print ()

"""Prompt the user to delete for a fruit to delete, find it and remove it( This assumes just first occurrence."""
response5 = input("Pick a fruit from the list to delete: ")
if fruit_list.__contains__(response5.capitalize()):
    fruit_list.remove(response5.capitalize())
print(fruit_list)
print ()

""" Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences."""
fruit_list += fruit_list
print(fruit_list)
response6 = input("Pick another fruit from the list to delete: ")
while True:
    if fruit_list.__contains__(response6.capitalize()):
        while fruit_list.__contains__(response6.capitalize()):
            fruit_list.remove(response6.capitalize())
        break
    else:
        response6 = input("This fruit doesn't exist in the list. Please try again: ")
print(fruit_list)

# endregion
