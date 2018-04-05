#!/usr/bin/env python3

# Series 1
"""
* Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
* Display the list (plain old print() is fine…).
* Ask the user for another fruit and add it to the end of the list.
* Display the list.
* Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
* Add another fruit to the beginning of the list using “+” and display the list.
* Add another fruit to the beginning of the list using insert() and display the list.
* Display all the fruits that begin with “P”, using a for loop.
"""

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print ("Here is our current list of fruits:",fruit_list, "\n")

new_fruit = input("Please enter another fruit you would like to add: ")
fruit_list.append(new_fruit)

print ("Here is our updated list of fruits:",fruit_list, "\n")

number_choice = input ("Choose a number between 1 and {:d}: ".format(len(fruit_list)))
print("The number {} matches {}".format(number_choice, fruit_list[int(number_choice) -1]), "\n")

new_fruit = input("Please enter another fruit you would like to add: ")
fruit_list = [new_fruit] + fruit_list
print ("Here is our updated list of fruits:",fruit_list, "\n")

new_fruit = input("Please enter another fruit you would like to add: ")
fruit_list.insert(0,new_fruit)    
print ("Here is our updated list of fruits:",fruit_list, "\n")

print ("Here are all the fruits that being with P:")
for fruit in fruit_list:
    if fruit[0] == 'P':
        print (fruit)

print()


#Series 2
"""
Using the list created in series 1 above:

* Display the list.
* Remove the last fruit from the list.
* Display the list.
* Ask the user for a fruit to delete, find it and delete it.
"""

print ("Here is our current list of fruits:",fruit_list, "\n")

fruit_list.pop()

print ("Here is our updated list of fruits after removing the last item:",fruit_list, "\n")

delete_fruit = input("Please enter a fruit you would like to have deleted: ")

for fruit in fruit_list:
    if fruit == delete_fruit:
        fruit_list.remove(fruit)


print ("Here is our updated list of fruits after removing your entry:",fruit_list, "\n")


#Series 3
"""
Again, using the list from series 1:

* Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
* For each “no”, delete that fruit from the list.
* For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
* Display the list.
"""

temp_list = fruit_list[:]

for fruit in temp_list[:]:
    reply = ''
    while reply != 'yes' or reply != 'no':
        reply = input("Do you like {}? ".format(fruit.lower())).lower()
        if reply == 'no':
            temp_list.remove(fruit)
            break
        elif reply == 'yes':
            break

print ("Here are your favorite fruits:",temp_list, "\n")

#Series 4
"""
Once more, using the list from series 1:

* Make a copy of the list and reverse the letters in each fruit in the copy.
* Delete the last item of the original list. Display the original list and the copy.
"""

reverse_list = []

for fruit in fruit_list:
    reverse_list.append(fruit[::-1])

fruit_list.pop()

print("Here is our original list of fruits with the last item removed",fruit_list, "\n")
print("Here is our list of fruits with the letters reversed!",reverse_list, "\n")