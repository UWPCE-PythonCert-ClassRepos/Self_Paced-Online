#!/usr/bin/env python3
"""
Sean Tasaki
5/10/2018
Lesson03.list_lab
"""

"""Series 1
"""
print("Beginning Series 1")
list1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(list1)
fruit = input("What fruit would you like to add to the list?\n> ")
list1.append(fruit.title())
print(list1)

index = input("Please enter a number between 1-5\n> ")
while int(index) < 1 or int(index) > 5:
	print("Invalid number.")
	index = input("Please enter a number between 1-5\n> ")
index1 = int(index) - 1
print(int(index), list1[index1])

fruit = input("Which fruit would you like to add to the beginning of the list?\n> ")
list1 = [fruit.title()] + list1

fruit = input("Enter another fruit to add to the beginning\n> ")
list1.insert(0, fruit.title())
print(list1)

print("Fruits in your list that start with 'P':")
list_with_P_fruits = []
for x in list1:
	if x[0] =='P':
		list_with_P_fruits.append(x)
	else:
		continue
print(list_with_P_fruits)
print()
list1_main = list1[:]
"""Series 2
"""

print("Beginning Series 2")
print("Here is your current list from Series 1:\n", list1_main)
print("Removing the last fruit from the list:")
list1_main.pop()
print(list1_main)
delete = input("Which fruit would you like to delete?\n> ")
for x in list1_main:
	if x.lower() == delete.lower():
		list1_main.remove(x)
	else:
		continue

print(list1_main)
print()

"""Series 3
"""

print("Beginning with Series 3")
list1_main = list1[:]
print("Here is your list from Series 1:\n",list1_main)
list_copy = list1_main[:]
for x in list_copy:
	fruit = input(f"Do you like {x}? > ")
	if fruit.lower() == 'no':
		list1_main.remove(x)
	else:
		print(f"Of course you like {x}. {x} are delicious!")

print("Here is a list of the fruits you like:\n", list1_main)
print()

"""Series 4
"""
print("Beginning with Series 4")
list1_main = list1[:]
print("Here is your list from Series 1: \n", list1_main)
list_copy = list1_main.copy()

for x, fruit in enumerate(list_copy):
	list_copy[x] = fruit[::-1]
print("Here is a copied list with the letters in each fruit reversed", list_copy)
del list1_main[-1]
print()
print("And here is the original list with the last item deleted", list1_main)
