#!/usr/bin/env python3

"""
Script Series for List Lab Assignment.

"""
# Series 1 ----------------------------------------------
print("Beginning Series One")

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

# Ask the user for another fruit and add it to the end of the list.
fruit_response = input("Type the name of a fruit to add to the list : ")
fruit_list.append(fruit_response)
print(fruit_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
#
fruit_num = int(input("Type a number to find the fruit at that index : "))
if 0 <= fruit_num < len(fruit_list):
    print("The fruit at position {:d} is {}".format(
        fruit_num, fruit_list[fruit_num-1]))
    #print(fruit_list[fruit_num -1])
else:
    print("Either the number entered is too small or too big for out list. Please try again")

# Add another fruit to the beginning of the list using “+” and display the list.
second_fruit_response = input(
    "Let's add another fruit to the begginng of our list. Enter a fruit here: ")
print("You entered {:s}".format(second_fruit_response))
new_fruit_list = [second_fruit_response, ] + fruit_list
print(new_fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.
third_fruit_response = input(
    "Great! Let's add another fruit to the begginng of our list. Enter a fruit here: ")
print("You entered {:s}".format(third_fruit_response))
new_fruit_list.insert(0, third_fruit_response)
print(new_fruit_list)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in new_fruit_list:
    if fruit[0] == "P":
        print(fruit)
    continue

# Series 2 --------------------------------
# Display the list.
print("Beginning Series 2: The list of fruits from series one: {}".format(new_fruit_list))

# Remove the last fruit from the list. Display the list
series_2_fruit_list = new_fruit_list[:-1]
print("The list with the last fruit removed: {}".format(series_2_fruit_list))

# Ask the user for a fruit to delete, find it and delete it.
#(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
doubled_fruit_list = series_2_fruit_list * 2
print("Here is our doubled list: {}".format(doubled_fruit_list))
fruit_to_delete = input(
    "Please enter a fruit you would like to delete from the list: ")

while fruit_to_delete not in doubled_fruit_list:
    fruit_to_delete = input(
        "That fruit isn't in the list. Enter a fruit from the list: ")

for fruit in doubled_fruit_list:
    if fruit == fruit_to_delete:
        doubled_fruit_list.remove(fruit)

print("You chose to delete {:s}. \
Here is the list with that fruit removed: {}".format(fruit_to_delete, doubled_fruit_list))

# Series 3 --------------------------------
# Again, using the list from series 1:
print("Beginning Series 3: The list of fruits from series one: {}".format(new_fruit_list))
# Ask the user for input displaying a line for each fruit in the list (making the fruit all lowercase).
series_3_fruit_list = new_fruit_list[:]
for fruit in new_fruit_list:
    user_choice = input("Do you like to eat {:s}?".format(fruit.lower()))
    # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
    while user_choice not in ("Y", "y", "yes", "YES", "Yes", "N", "n", "NO", "No"):
        input("Please answer yes or no. Do you like to eat {:s}?".format(
            fruit.lower()))
    # For each “no”, delete that fruit from the list.
    if user_choice in ("N", "n", "NO", "No"):
        series_3_fruit_list.remove(fruit)
print("Here is the list of fruits you like: {}".format(series_3_fruit_list))

# Series 3 --------------------------------
print("Beginning Series 4: The list of fruits from series one: {}".format(new_fruit_list))
# Make a copy of the list and reverse the letters in each fruit in the copy.
series_4_fruit_list = new_fruit_list[:]
series_4_fruit_list_rev = []

for fruit in series_4_fruit_list:
    series_4_fruit_list_rev.append(fruit[::-1])
print(series_4_fruit_list_rev)

# Delete the last item of the original list. Display the original list and the copy.
series_4_fruit_list = series_4_fruit_list[:-1]
print("Original list: {}".format(series_4_fruit_list))
print("Copied list: {}".format(series_4_fruit_list_rev))
