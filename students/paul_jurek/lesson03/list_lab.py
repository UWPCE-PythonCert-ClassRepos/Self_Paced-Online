#!/usr/bin/env python3
"""
As part of lesson 3 list_lab, running through 4 series of
steps and modifying a fruit list.  Comments describe directions."""

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list (plain old print() is fine…).
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
new_fruit = input("Please add fruit to list: ")
fruits.append(new_fruit)

# Display the list.
print(fruits)

# Ask the user for a number and display the number back to the user and the
#     fruit corresponding to that number (on a 1-is-first basis). Remember
#     that Python uses zero-based indexing, so you will need to correct.
# ensuring user puts in index for valid fruits
fruit_index_selection = -1
while int(fruit_index_selection) not in range(1, len(fruits)+1):
    fruit_index_selection = int(input(f"Please select index of fruit which is between 1 and {len(fruits)}: "))
print(fruits[int(fruit_index_selection)-1])

# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ['Mango'] + fruits
print(fruits)

# Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0, 'Dragonfruit')
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in fruits:
    if fruit.lower().startswith('p'):
        print(fruit)

# Series 2
# Using the list created in series 1 above:
# Display the list.
# creating copy of list as we will need original list for part 3
fruits2 = fruits.copy()
print(fruits2)

# Remove the last fruit from the list.
fruits2.pop()

# Display the list.
print(fruits2)

# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a
#     match is found. Once found, delete all occurrences.)
fruits2 *= 2
# hoping user hasn't inserted -1 as fruit
fruit_to_delete = -1
while fruit_to_delete not in fruits2:
    fruit_to_delete = input(f"Select fruit to delete: ")
for _ in range(fruits2.count(fruit_to_delete)):
    fruits2.remove(fruit_to_delete)

# Series 3
# Again, using the list from series 1:
fruits3 = fruits.copy()

# Ask the user for input displaying a line like “Do you like apples?”
#     for each fruit in the list (making the fruit all lowercase).
for fruit in fruits3[:]:
    like_fruit = ''

    # For each “no”, delete that fruit from the list.
    # For any answer that is not “yes” or “no”, prompt the user to answer
    #     with one of those two values (a while loop is good here)
    while like_fruit.lower() not in ['yes', 'no']:
        like_fruit = input(f"Do you like {fruit.lower()}? (yes or no)")
    if like_fruit.lower() == 'no':
        fruits3.remove(fruit)
# Display the list.
    print(fruits3)

# Series 4
# Once more, using the list from series 1:
# Make a copy of the list and reverse the letters in each fruit in the copy.
fruits4 = fruits.copy()
fruits4.reverse()
# Delete the last item of the original list. Display the original list and the copy.
fruits.pop()
print(f'Original List: {fruits}')
print(f'Copied List: {fruits4}')
