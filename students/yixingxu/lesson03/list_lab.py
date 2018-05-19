#!/usr/bin/env python3

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
a_list = ["Apples", "Pears", "Oranges" , "Peaches"]
print(a_list)
# Ask the user for another fruit and add it to the end of the list.
added_fruit = input("add another fruit > ")
a_list.append(added_fruit)
print(a_list)
# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
fruit_number = input("Which number of the fruit you want to choose > ")
print(fruit_number, a_list[int(fruit_number)-1])
# Add another fruit to the beginning of the list using “+” and display the list.
added_fruit = 'Grapes'
a_list = [added_fruit] + a_list
print(a_list)
# Add another fruit to the beginning of the list using insert() and display the list.
a_list.insert(0,'Watermelon')
print(a_list)
# Display all the fruits that begin with “P”, using a for loop.
print('Display all the fruits that begin with “P”')
for fruit in a_list:
	if fruit[0] == 'P':
		print(fruit)
series_1_list = a_list[:]
		
# Series 2
print(a_list)
# Remove the last fruit from the list.
a_list.pop()
print(a_list)
# Ask the user for a fruit to delete, find it and delete it.
fruit_delete = input("Which fruit to delete from the list? > ")
a_list.remove(fruit_delete)
print(a_list)

# Series 3
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
a_list = series_1_list[:]
print(a_list)
list_copy = a_list[:]
for fruit in list_copy:
	# For each “no”, delete that fruit from the list.
	# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
	yes_no_fruit = ''
	while yes_no_fruit not in ['yes','no']:
		yes_no_fruit = input("Do you like {} (yes or no)> ".format(fruit.lower()))
	if yes_no_fruit == 'no':
		a_list.remove(fruit)
print('The fruit you like',a_list)

# Series 4

# Once more, using the list from series 1:
a_list = series_1_list[:]
# Make a copy of the list and reverse the letters in each fruit in the copy.
list_copy = a_list[:]
for i,fruit in enumerate(list_copy):
	list_copy[i] = fruit[::-1]
print('reversed fruit names:',list_copy)
# Delete the last item of the original list. Display the original list and the copy.		
a_list = ["Apples", "Pears", "Oranges" , "Peaches"]	
new_list = a_list[:]
new_list.pop()
print('last item deleted list',new_list)
print('original list',a_list)


