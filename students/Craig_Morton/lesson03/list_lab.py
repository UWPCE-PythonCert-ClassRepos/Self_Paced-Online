# ------------------------------------------------- #
# Title: Lesson 3, pt 2/4, List Lab Exercise
# Dev:   Craig Morton
# Date:  8/19/2018
# Change Log: CraigM, 8/19/2018, List Lab Exercise
#  ------------------------------------------------ #

# !/usr/bin/env python3

# Start of series 1 ##########

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.  Display the list (plain old print() is fine
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list, "\n")

# Ask the user for another fruit and add it to the end of the list
# Display the list
user_input = input("Please add a fruit to your list: ")
fruit_list.append(user_input.title())
print(fruit_list, "\n")

# Ask the user for a fruit index value and display the value as well as the corresponding fruit
user_input = " "
index_value = None
while not user_input.isdigit():
    user_input = input("Please enter the index value of the fruit you wish to display: ")
    if user_input.isdigit():
        index_value = int(user_input)
        if index_value > len(fruit_list):
            user_input = " "
print(index_value, fruit_list[index_value - 1], "\n")

# Add another fruit to the beginning of the list using “+” and display the list
user_input = input("Please add a fruit: ")
fruit_list = [user_input.title()] + fruit_list
print(fruit_list, "\n")

# Add another fruit to the beginning of the list using insert() and display the list
user_input = input("Please add another fruit: ")
fruit_list.insert(0, user_input.title())
print(fruit_list, "\n")

# Display all the fruits that begin with “P”, using a for loop
print("Displaying all fruits that start with the letter 'P':")
for fruit in fruit_list:
    if fruit[0] == "P":
        print(fruit, end=" ")
print("\n")

# Start of series 2 ##########

# Display the list
print("# Series 2 \n")
print(fruit_list, "\n")

# Remove the last fruit from the list and Display the list
print("Removing the last fruit from the list")
fruit_list.pop(len(fruit_list) - 1)
print(fruit_list, "\n")

# Ask the user for a fruit to delete, find it and delete it
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_list = fruit_list * 2
value = 0
while value == 0:
    print("List of fruit: ", fruit_list)
    user_input = input("Please enter a fruit to delete (The fruit must be included in the list): ")
    value = fruit_list.count(user_input.title())
while value > 0:
    fruit_list.remove(user_input.title())
    value = fruit_list.count(user_input.title())
print(fruit_list, "\n")

# Start of series 3 ##########

print("# Series 3 \n")
fruit_list = list(set(fruit_list))
print(fruit_list, "\n")

# Ask the user for input displaying a line that asks if they like each fruit from the list
# For each "no", delete that fruit from the list
# For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (use while loop)
# Display the list
fruit_list_while_loop = list(fruit_list)
for fruit in fruit_list_while_loop:
    user_input = "meh"
    while user_input != 'yes' and user_input != 'no':
        ask = "Do you like " + fruit + "('yes' or 'no'?): "
        user_input = input(ask)
        user_input = user_input.lower()
    if user_input == 'no':
        fruit_list.remove(fruit)
print(fruit_list, "\n")

# Start of series 4 ##########

print("# Series 4 \n")

# Make a copy of the list and reverse the letters in each fruit in the copy
# Delete the last item of the original list. Display the original list and the copy
fruits_reversed = list()
for fruit in fruit_list:
    fruits_reversed.append(fruit[::-1])
fruit_list.pop(len(fruit_list) - 1)

print(fruits_reversed, "\n")
print(fruit_list)
