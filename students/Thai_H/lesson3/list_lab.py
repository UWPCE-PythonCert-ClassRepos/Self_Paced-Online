#!/usr/bin/env python3
# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
orig_fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_list = orig_fruit_list[:]



# Display the list (plain old print() is fine…).
print ('\nSeries 1: fruit list = {}'.format(fruit_list) )

# Ask the user for another fruit and add it to the end of the list.
# Display the list.
a_fruit = input('\nEnter a fruit to append to list: ')
fruit_list.append(a_fruit)
print ('New fruit list = {}'.format(fruit_list) )

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
a_number = input('\nEnter a number matching to the fruit : ')
print('Fruit number {} is {} \n'.format(a_number, fruit_list[int(a_number) - 1]) )

# Add another fruit to the beginning of the list using “+” and display the list.
fruit_list = ['Mangosteen'] + fruit_list
print ('Prefix a new fruit to the list: {}\n'.format(fruit_list))

# Add another fruit to the beginning of the list using insert() and display the list.
fruit_list.insert(0, 'Rambutan')
print ('Prefix another fruit to the list: {}\n'.format(fruit_list))

# Display all the fruits that begin with “P”, using a for loop.
print ('The following fruit names start with letter P: ', end='')
for fruit in fruit_list:
    if fruit[0].upper() == 'P':
        print (fruit, end = ' ')
print('\n')
#
#
# Series 2
# Using the list created in series 1 above:
fruit_list = orig_fruit_list[:]
# Display the list.
print ('\nSeries 2: fruit list = {}'.format(fruit_list) )

# Remove the last fruit from the list.
# Display the list.
fruit_list.pop()
print ('\nUsed .pop() function to remove the last fruit. Now the fruit list = {}\n'.format(fruit_list) )

# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_list = orig_fruit_list[:] * 2
print ('\nFruit list now doubled = {}'.format(fruit_list) )
fruit_to_delete = ''
while fruit_to_delete not in fruit_list:
    fruit_to_delete = input('Which fruit to delete? ')
while fruit_to_delete in fruit_list:
    fruit_list.remove(fruit_to_delete)

print ('\nFruit list after {} was removed = {}'.format(fruit_to_delete, fruit_list) )

# Series 3
# Again, using the list from series 1:
fruit_list = orig_fruit_list[:]
print ('\nSeries 3: fruit list = {}'.format(fruit_list) )
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

for each_fruit_item in fruit_list[:]:
    fruit_preference = ''
    while fruit_preference not in ['y', 'n']:
        fruit_preference = input('\nDo you like {} (y/n)? '.format(each_fruit_item.lower()))
    if fruit_preference == 'n':
        fruit_list.remove(each_fruit_item)
print ('\n\nFruit list = {}'.format(fruit_list) )


# Series 4
# Once more, using the list from series 1:
# Make a copy of the list and reverse the letters in each fruit in the copy.\
fruit_list = orig_fruit_list[:]
reversed_fruit_name = []
for fruit_item in fruit_list[:]:
    reversed_fruit_name.append( fruit_item[::-1] )

# Delete the last item of the original list. Display the original list and the copy.
fruit_list.pop()
print ('\n\nFruits before reversed = {}'.format(fruit_list) )
print ('\n\nFruit list - reversed = {}'.format(reversed_fruit_name) )