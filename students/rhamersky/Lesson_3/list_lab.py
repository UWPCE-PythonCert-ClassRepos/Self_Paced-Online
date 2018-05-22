#!/usr/bin/env python3
# Description: This program will teach the user about Python list.
# Developer: Ryan Hamersky
# Date: 05/08/2018
# Rev: A - 05/15/2018 add comments to the code.

# -----Data Section-----
l = ["Apples", "Pears","Oranges", "Peaches"]

# -----Process Section-----
# Series 1 #

print()  # --> Formatting
print("Series 1")
print()  # --> Formatting

print(l)  # --> Displays fruit list 'l'

l.append(input("Please, add a fruit to the end of the list. ").title())  # --> Ask user for new fruit

print(l)  # --> Displays new list to user.

index = int(input("Please, enter a number to display the fruit. "))  # --> Receive number input from user.

fruit = l[index-1]  # --> Finds fruit from the number the user inputted.

print(fruit)  # --> Prints the fruit to the user.

new_fruit = [input("Please, add another fruit to the beginning of the list. ").title()]   # --> Ask the user for a fruit.

l = new_fruit+l  # --> Adds a new fruit to the beginning of the list.

print(l)  # --> Prints new list.

# Asks user for a fruit and inserts the fruit at the beginning of the list.
l.insert(0,input("Please, add another fruit to the beginning of the list. ").title())

print(l)  # --> Prints new list.

# Prints all the fruits that begin with the letter 'P'.
for fruits in l:
    if "P" is fruits[0] or "p" is fruits[0]:
        print(fruits)

########################################

# Series 2 #

print()  # --> Formatting
print("Series 2")
print()  # --> Formatting

copy_l = l[:]  # --> Creates a copy from the new list from series 1.

print(copy_l)  # --> Display list to the user.

del copy_l[-1]  # --> Deletes the last item in the list.

print(copy_l)  # --> Displays list to the user.

# Ask the user which fruit they would like to remove form the list.
delete_fruit = input(("What fruit would you like to delete from the list? ")).title()

# Deletes fruit if in the list.
if delete_fruit in copy_l:
    copy_l.remove(delete_fruit)

else:
    print(delete_fruit+" does not exist in the list")

print(copy_l)  # --> Displays list to the user.

########################################

# Series 3 #

print()  # --> Formatting
print("Series 3")
print()  # --> Formatting

copy2_l = l[:]  # --> Creates a copy from the new list from series 1.

# print(copy2_l)  # --> Used during testing.

fruit_count = 0
fruit = 0
delete_fruit = []

# Creates a delete fruit list. These items will be removed from series 1 list.
while fruit_count < len(copy2_l):
    remove_fruit = input("Do you like " + copy2_l[fruit].lower() + "? ").capitalize()
    while not (remove_fruit == "Yes" or remove_fruit == "No"):
        print("Please, enter yes or no.")
        remove_fruit = input("Do you like " + copy2_l[fruit].lower() + "? ").capitalize()
    if remove_fruit == "No":
        delete_fruit.append(copy2_l[fruit])
    fruit_count += 1  # --> Counter for the while loop.
    fruit += 1  # --> Index counter

# Removes fruit from the list that the user wishes to remove.
for fruit in delete_fruit:
    copy2_l.remove(fruit)


print(copy2_l)  # --> Displays new list to the user.

###########################################

# Series 4 #

print()  # --> Formatting
print("Series 4")
print()  # --> Formatting

copy3_l = []

for item in range(len(l)):
    x = l[item]  # --> Creates fruit
    new = x[::-1]  # --> Reverses the name of the fruit.
    copy3_l.append(new)  # --> makes new list of fruit

del l[-1]  # --> Deletes the last item.

print(l)
print(copy3_l)

input("\n" + "Press enter to exit. ")