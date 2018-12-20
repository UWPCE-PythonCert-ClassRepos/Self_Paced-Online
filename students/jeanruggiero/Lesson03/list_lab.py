#!/usr/bin/env python

############################## SERIES 1########################################
print() #Print blank line for formatting and ease of use
print('Series 1')

# Create a list of fruits and print it
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

new_fruit = input('\nEnter a fruit: ')     # Prompt the user to input a fruit
fruits.append(new_fruit)                # Add new fruit to end of fruits list
print()
print(fruits)


# Implement some simple error catching for user input
while True:
    try:
        # Take input from user and try to convert to integer
        index = int(input('\nEnter an index to retrieve the corresponding fruit: '))

        # Try to display the index and corresponding fruit back to the user (index starts at 1)
        print('\nIndex = {:d}\tFruit = {:s}'.format(index, fruits[index-1]))
        break

    # Handle errors related to non-integer or out of range inputs
    except ValueError:
        print("That's not an integer. Please enter an integer from 1 to {:d}.".format(len(fruits)))
    except IndexError:
        print("Index out of range. Please enter an integer from 1 to {:d}.".format(len(fruits)))


# Add another fruit to the beginning of the list using '+'
fruits = ["Mango"] + fruits
print()
print (fruits)

# Add another fruit to the beginning of the list using the insert method
fruits.insert(0,"Papaya")
print()
print(fruits)

# Display all fruits that begin with a 'P' (case insensitive)
print("\nThese fruits start with 'p':")
for fruit in fruits:
    if fruit.lower()[0] == 'p':
        print(fruit)


############################## SERIES 2########################################
print()
print('Series 2')

# Display the list from Series 1
print()
print(fruits)

# Remove the last fruit from the list
fruits = fruits[:-1]
print()
print(fruits)

# Ask the user for a fruit to remove, then remove it from the list
