#!/usr/bin/env python3

# Series 1
# 1. Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# 2. Display the list (plain old print() is fine…).
# 3. Ask the user for another fruit and add it to the end of the list.
# 4. Display the list.
# 5. Ask the user for a number and display the number back to the user and the 
# fruit corresponding to that number (on a 1-is-first basis). Remember that Python 
# uses zero-based indexing, so you will need to correct.
# 6. Add another fruit to the beginning of the list using “+” and display the list.
# 7. Add another fruit to the beginning of the list using insert() and display the list.
# 8. Display all the fruits that begin with “P”, using a for loop

""" Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”."""
fruit = ["Apples","Pears","Oranges","Peaches"]
print(fruit)

""" Ask the user for another fruit and add it to the end of the list. """
add_fruit = input("Please enter a fruit to add to the end of list. ")
fruit.append(add_fruit)
print(fruit)

""" Ask the user for a number and display the number back to the user and the 
 fruit corresponding to that number (on a 1-is-first basis). Remember that Python 
 uses zero-based indexing, so you will need to correct. """
fruit_number = int(input("Please enter a number. "))
print(fruit_number, fruit[fruit_number -1])

""" Add another fruit to the beginning of the list using “+” and display the list. """

""" Add another fruit to the beginning of the list using insert() and display the list. """
add_fruit = input("Please enter a fruit to add to the beginning of the list. ")
fruit.insert(0,add_fruit)
print(fruit)

""" Display all the fruits that begin with “P”, using a for loop """
first_letter = [i[0] for i in fruit]
print(first_letter)
for x in first_letter:
    if x == "P" or x == "p":
	    print(x, end=', ')