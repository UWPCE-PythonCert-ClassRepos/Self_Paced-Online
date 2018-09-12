#!/usr/bin/env python3

# List Lab Exercise by Alejandro Guardia
# Series 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

# Ask the user for another fruit and add it to the end of the list.
response = input("Please enter another fruit : ")
fruit_list.append(response)
print(fruit_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
response = input("Please enter a number :")
print("The fruit corresponding to {} is {}".format(response, fruit_list[int(response)-1]))

# Add another fruit to the beginning of the list using “+” and display the list.
fruit_list = ["Banana"] + fruit_list
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.
fruit_list.insert(0,"Kiwi")
print(fruit_list)

# Display all the fruits that begin with “P”, using a for loop.
for item in fruit_list:
    if item[0] == "P":
        print(item)


# Series 2

print(fruit_list)

# Remove the last fruit from the list.
fruit_list.pop()
print(fruit_list)

# Ask the user for a fruit to delete, find it and delete it.
response = input("Which fruit do you want to delete? ")
fruit_list.remove(response)
print(fruit_list)

# Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.
fruit_list *=2
print(fruit_list)
response = ""
while response not in fruit_list:
    response = input("Which fruit do you want to delete? ")
while response in fruit_list:
    fruit_list.remove(response)
print(fruit_list)

# Series 3

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
for item in fruit_list:
    response = ""
    while response not in ["yes", "no"]:
        response = input("Do you like {} ? ".format(item.lower()))
    if response == "no":
        fruit_list.remove(item)
print(fruit_list)

# Series 4

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
# Make a copy of the list and reverse the letters in each fruit in the copy.

reverse_list = fruit_list[::]
for i, item in enumerate(reverse_list):
    reverse_list[i] = item[::-1]
fruit_list.pop()
print(fruit_list)
print(reverse_list)

