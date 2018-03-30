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

# """ Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”."""
fruit = ["Apples","Pears","Oranges","Peaches"]
# print(fruit)

# # """ Ask the user for another fruit and add it to the end of the list. """
# add_fruit = input("Please enter a fruit to add to the end of list. ")
# fruit.append(add_fruit)
# print(fruit)

# # """ Ask the user for a number and display the number back to the user and the 
# #  # fruit corresponding to that number (on a 1-is-first basis). Remember that Python 
# #  uses zero-based indexing, so you will need to correct. """
# fruit_number = int(input("Please enter a number. "))
# print(fruit_number, fruit[fruit_number -1])

# """ Add another fruit to the beginning of the list using “+” and display the list. """
add_fruit = input("Please enter a fruit to add to the beginning of the list. ")
fruit = list(add_fruit) + fruit
print(fruit)

# # """ Add another fruit to the beginning of the list using insert() and display the list. """
# add_fruit = input("Please enter a fruit to add to the beginning of the list. ")
# fruit.insert(0,add_fruit)
# print(fruit)

# # """ Display all the fruits that begin with “P”, using a for loop """
# first_letter = [i[0] for i in fruit]
# for x in first_letter:
#     if x.title() == "P":
# 	    print(x, end=' ')
# print()


# # Series 2
# # 1. Display the list.
# # 2. Remove the last fruit from the list.
# # 3. Display the list.
# # 4. Ask the user for a fruit to delete, find it and delete it.
# # 5b. (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

# """ Display the list. """
# fruit = ["Apples","Pears","Oranges","Peaches"]
# print(fruit)

# # """ Remove the last fruit from the list. """
# fruit.pop()
# print(fruit)

# # """ Ask the user for a fruit to delete, find it and delete it. """
# del_fruit = input("Enter the name of a fruit to delete. ")
# if del_fruit in fruit:
# 	fruit.remove(del_fruit)
# print(fruit)


# Series 3
# 1. Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the 
# fruit all lowercase).
# 2. For each “no”, delete that fruit from the list.
# 3. For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values 
# (a while loop is good here)
# 4. Display the list.

""" Display the list. """
# fruit = ["Apples","Pears","Oranges","Peaches"]
# print(fruit)

# copy_fruit = fruit[:]
# for i in fruit:
#     prompt_y_n = input("Do you like {}? ".format(i))
#     prompt_y_n = prompt_y_n.lower()
#     while prompt_y_n != "yes" and prompt_y_n != "no":
#         prompt_y_n = input("Please enter yes or no. ")
#         prompt_y_n = prompt_y_n.lower()
#     if prompt_y_n == "no":
#         copy_fruit.remove(i)
# print(copy_fruit)
# print(fruit)


# # Series 4
# # 1. Make a copy of the list and reverse the letters in each fruit in the copy.
# # 2. Delete the last item of the original list. Display the original list and the copy.

# fruit = ["Apples","Pears","Oranges","Peaches"]
# print(fruit)

# new_fruit = fruit.copy()
# reversed_list = []
# for tree in new_fruit:
# 	new_tree = tree[::-1]
# 	reversed_list.append(new_tree)
# fruit.pop()
# print(fruit)
# print(reversed_list)
