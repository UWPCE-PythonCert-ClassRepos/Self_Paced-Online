#!/usr/bin/env python

############################## SERIES 1########################################
print(); print('Series 1')
print('____________________________________________________________________')

# Create a list of fruits and print it
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

new_fruit = input('\nEnter a fruit: ')     # Prompt the user to input a fruit
fruits.append(new_fruit)                # Add new fruit to end of fruits list
print(fruits)


# Implement some simple error catching for user input
while True:
    try:
        # Take input from user and try to convert to integer
        index = int(input('\nEnter an index to retrieve the corresponding fruit: '))

        # Try to display the index and corresponding fruit back to the user (index starts at 1)
        print('Index = {:d}\tFruit = {:s}'.format(index, fruits[index-1]))
        break

    # Handle errors related to non-integer or out of range inputs
    except ValueError:
        print("That's not an integer. Please enter an integer from 1 to {:d}.".format(len(fruits)))
    except IndexError:
        print("Index out of range. Please enter an integer from 1 to {:d}.".format(len(fruits)))


# Add another fruit to the beginning of the list using '+'
fruits = ["Mango"] + fruits
print(); print (fruits)

# Add another fruit to the beginning of the list using the insert method
fruits.insert(0,"Papaya")
print(); print(fruits)

# Display all fruits that begin with a 'P' (case insensitive)
print("\nThese fruits start with 'p':")
for fruit in fruits:
    if fruit.lower()[0] == 'p':
        print(fruit)


############################## SERIES 2########################################
print(); print()
print('Series 2')
print('____________________________________________________________________')


# Create a new list from the list in Series 1
fruits2 = fruits[:]

# Display the list from Series 1
print(fruits2)

# Remove the last fruit from the list
fruits2 = fruits2[:-1]
print(); print(fruits2)

# Multiply the list of fruits times 2
fruits2 = fruits2 * 2
print(); print(fruits2)

while True:
    # Ask the user for a fruit to remove, then remove it from the list
    del_fruit = input('\nEnter a fruit to remove from the list: ')

    # Check if the provided fruit (case insensitive) is in the list.
    # If it isn't, keep asking until a fruit in the list is provided.
    if del_fruit.lower() in (fruit.lower() for fruit in fruits2):
        break
    else:
        print("That fruit isn't in the list. Please try again.")

# Find the given fruit in the list (case insensitive) and remove it
for fruit in fruits2[:]:
    if fruit.lower() == del_fruit.lower():
        fruits2.remove(fruit)

# Print list with given fruit removed
print(fruits2)


#################################SERIES 3#######################################
def lower_list(list):
    """Returns a copy of list with all elements in lower case."""
    for i in range(0,len(list)):
        list[i] = list[i].lower()
    return list

print(); print()
print('Series 3')
print('____________________________________________________________________')


# Create a new list from the list in Series 1
fruits3 = fruits[:]

# Display the list from Series 1
print(fruits3)

# Make a copy of fruits3 (do it here so case insensitive duplicate fruit
# checking will work)
temp_fruits = fruits3[:]

# Ask user if they like each unique (case insensitive) fruit in the list
for i,fruit in enumerate(temp_fruits):
    # Check if the user has already been asked about the fruit in question and
    # skip over it if so.
    if lower_list(temp_fruits[:]).index(fruit.lower()) < i:
        if lower_list(fruits3[:]).count(fruit.lower()) < lower_list(temp_fruits[:]).count(fruit.lower()):
            # If the user previously said they don't like the fruit, there will
            # be fewer instances of that fruit in fruits3 (since it would have
            # been removed). If that's the case, remove the fruit from fruits3
            # without asking the user about it again
            fruits3.remove(fruit)
        # Whether the user previously said yes or no about the fruit, don't
        # ask them about the same fruit again.
        continue

    while True:
        # Ask the user if they like each unique fruit in the list
        like_fruit = input('Do you like {:s}? '.format(fruit.lower()))

        if like_fruit.lower() == 'no':
            # If the answer is no, remove the fruit from the list
            fruits3.remove(fruit)
            break
        elif like_fruit == 'yes':
            break
        else:
            # If the user enters something other than 'yes' or 'no', ask them
            # to try again.
            print('Please enter "yes" or "no."')

print(fruits3)

#################################SERIES 4#######################################
print(); print()
print('Series 4')
print('____________________________________________________________________')

# Create a new list from the list in Series 1. Start with an empty list
fruits4 = []
for fruit in fruits:
    # Reverse the order of each string in fruits and append it to fruits4
    fruits4.append(fruit[::-1])

# Print the original and new lists
print('Original list:')
print(fruits)
print('New Series 4 list:')
print(fruits4)
