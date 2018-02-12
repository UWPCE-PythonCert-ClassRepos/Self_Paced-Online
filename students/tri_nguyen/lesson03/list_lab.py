#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  09-Feb-2018
# ------------------------------------------- #

# ------------------------------------------- #
# Series 1:
# - Create a list that contains 'Apples', 'Pears',
#   'Oranges' and 'Peaches.
# - Display the list.
# - Ask the user for another fruit and add it
#   to the end of the list.
# - Display the list.
# - Ask the user for a number and display the number
#   back to the user and the fruit corresponding
#   to that number.
# - Add another fruit to the beginning of the list
#   using '+' and display the list.
# - Add another fruit to the beginning of the list
# - using insert() and display the list.
# - Display all the fruits that begins with 'P',
#   using a for loop.


fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('--Series 1 of the exercise--'.upper()+'\n')

print('Below is the current list of fruits.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
user_input = input('Please add another fruit: ')
fruit_list.append(user_input.title())

print()
print('Below is a newly updated list of fruits.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
num_from_user = int(input('Please pick a number to get back the corresponding fruit: '))
num_from_user = num_from_user - 1  # Python uses zero based indexing

if fruit_list[num_from_user] in fruit_list[num_from_user]:
    print(num_from_user + 1, '-', fruit_list[num_from_user])

print()
fruit_list = ['Watermelons'] + fruit_list
print('Watermelons has been added to the beginning of the list.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
fruit_list.insert(0, 'Pinnaples')
print('Pinnaples have been added to the beginning of the list.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
print('Below is the list of fruits that begin with "P".')
for fruit in fruit_list:
    if fruit.startswith('P'):
        print(fruit)

# End of Series 1
# ------------------------------------------- #

# ------------------------------------------- #
# Series 2 - Using the list created in series 1:
# - Display the list.
# - Remove the last fruit from the list.
# - Display the list.
# - Ask the user for a fruit to delete, find it
#   and delete it.
# - (Bonus: Multiply the list times two. Keep asking
#    until a match is found. Once found, delete all
#    occurrences).

print('\n'+'--Series 2 of the exercise--'.upper()+'\n')

print('Below is the current list of fruits.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
print('The last fruit ({}) from the list has been removed.'.format(fruit_list[len(fruit_list) - 1]))
fruit_list.pop()
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print()
to_be_deleted = input('Enter a fruit to delete: ')

if to_be_deleted.title() in fruit_list:
    fruit_list.remove(to_be_deleted.title())

print('\nBelow is a newly updated list of fruits.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)


# End of Series 2
# ------------------------------------------- #

# ------------------------------------------- #
# Series 3 - Using the list from series 1:
# - Ask the user for input displaying a line like
#   'Do you like apples?' for each fruit in the list.
#   make the fruit all lowercase.
# - For each 'no', delete that fruit from the list.
# - For any answer that is not 'yes' or 'no', prompt
#   the user to answer with one of those two values.
# - Display the list.

print('\n'+'--Series 3 of the exercise--'.upper()+'\n')

count = 0
answer_set = ('yes', 'no')

while count <= len(fruit_list):

    for idx, fruit in enumerate(fruit_list):

        from_user = input('Do you like ' + fruit.lower() + '? ')

        if from_user.lower() == answer_set[1]:
            print("\nYou don't like " + fruit.lower() + ". It'll be removed.\n")
            fruit_list.remove(fruit)
        elif from_user.lower() == answer_set[0]:
            print('\n' + fruit + ' are good.\n')
        else:
            print('\nPlease enter yes or no\n')
            continue
        count = count + 1

print()
print('Below is the newly updated list of fruits.')
for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

# End of Series 3
# ------------------------------------------- #

# ------------------------------------------- #
# Series 4 - Using the list from series 1
# - Make a copy of the list and reverse the letters
#   in each fruit in the copy.
# - Delete the last item of the original list.
# - Display the original and the copy.
# ------------------------------------------- #

print('\n'+'--Series 4 of the exercise--'.upper()+'\n')

copied_fruit_list = fruit_list.copy()

reversed_letters = []

for fruit in copied_fruit_list:
    reversed_letters.append(fruit[::-1])

fruit_list.pop()

print('\nThe original list of fruits minus the last fruit:')

for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print('\nThe copied list of fruits with reversed letters:')

for idx, fruit in enumerate(reversed_letters):
    print(idx + 1, '-', fruit)

# End of Series 4
# ------------------------------------------- #
