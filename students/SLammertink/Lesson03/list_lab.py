#! /usr/bin/env python3
# Author: SLammertink
# UW Self-paces Lesson 03 List_lab.py

# Print a fruit list

## Series 1 ##

print(' ')
print('Now we will print a list with the given fruits: ')

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
print(' ')
# Ask the user to add a fruit to the list then print the list

new_fruit = input("Which fruit would you like to add to the list: ")
fruit_list.append(new_fruit)
print(fruit_list)
print(' ')

# Ask the user to enter a number and print the fruit related to this number in the list:
print('Now we ask the user to enter a number and print the fruit associated with that number in the list: ')
print(' ')
number_asked = int(input("Please enter a number:  "))
for i, fruit in enumerate(fruit_list, 1):
    if i == number_asked:
        print("The number you entered was {} and the corresponding fruit is {}.".format(number_asked, fruit))

print(' ')

# Now we add a fruit using the '+' sign to the beginning of the list:
print("Now we add the fruit 'Mango' to the beginning of the list using the '+' sign: ")
add_fruit = ['Mango']
new_fruit_list = add_fruit + fruit_list
print(new_fruit_list)
print(' ')
# Now we add another fruit using the insert() method to the begiining of the list:

print('Now we add the fruit Avocado to the beginning of the list using the insert statement:')
new_fruit_list.insert(0, 'Avocado')
print(new_fruit_list)
print(' ')
# Now we print all the fruits that start with a 'P':

print('Now we will print all fruits in the list that start with a P: ')
for fruit in new_fruit_list:
    if fruit.startswith("P"):
        print(fruit, end = ' ')
print('')
print('')

## Series 2 ##

# Display the list created in series 1

print("Now displaying the list created in series 1:")
print(new_fruit_list)
print('')
# Remove the last fruit from the list:
new_fruit_list.pop(-1)
# Display the list
print("Display the list with the last item removed: ")
print(new_fruit_list)
print('')

# Ask the user for a fruit to delete, find it and delete it

del_fruit = input("Which fruit would you like to delete? - enter its name - ")
if del_fruit in new_fruit_list:
    new_fruit_list.remove(del_fruit)
print(new_fruit_list)

# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences

print('')
print("Will now double the new_fruit_list and delete all these fruits ")
double_fruits = new_fruit_list * 2

# Ask the user to select a fruit to delete

del_fruit = input("Which fruit do you want to delete from the list? ")
if del_fruit in double_fruits:
    double_fruits.remove(del_fruit)
elif del_fruit not in double_fruits:
    print("Please enter a fruit that is in the list ")
print(double_fruits)
print('')

## Series 3 ##

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase)
# For each “no”, delete that fruit from the list
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list

for fruit in new_fruit_list:
    while True:
        like_fruit = input("Do you like {} ? ".format(fruit.lower()))
        if like_fruit == 'yes':
            break
        elif like_fruit == 'no':
            new_fruit_list.remove(fruit)
            break
        else:
            print("Please answer with a 'yes' or a 'no'!")
print(new_fruit_list)
print('')

## Series 4 ##

# make a copy of the list in series 1

copy_list = new_fruit_list.copy()

# reverse the letters of each word in this list
for word in copy_list:
     word[::-1]

# Delete the last word of the original list (new_fruit_list)
new_fruit_list.pop(-1)

# print the original list then the copied list with the letters in the words reversed

print("The original list :", new_fruit_list, end = ' ')
print("THe copied list: ", copy_list, end = ' ' )
