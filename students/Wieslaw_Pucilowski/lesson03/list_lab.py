#!/usr/bin/env python3

__author__ = "Wieslaw Pucilowski"

# Series 1

fruits=["Apples", "Pears", "Oranges", "Peaches", "Pineapples"]
list_fruits=fruits

print("List of fruits:")
print(list_fruits)

list_fruits.append(input("What fruit would you like to add to the list: "))
print("List of fruits:")
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

num=input("Enter the number but not greater than "+str(len(list_fruits))+": ")
print("The number", num, "is for fruit",list_fruits[int(num)-1])

list_fruits=["Plums"]+list_fruits
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

list_fruits.insert(0,"Mangos")
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

for fruit in list_fruits:
	if fruit[0] == "P":
		print(fruit)

# Series 2
list_fruits=fruits

print("Series 2")

print("Removing last item fron the list")
list_fruits=list_fruits[:-1]
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

del_fruit=input("What fruit to remove from the list:")

if del_fruit in list_fruits:
	list_fruits.remove(del_fruit)
else:
	print(del_fruit,"Fruit not found in the list")

print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

# Series 3
list_fruits=fruits

print("Series 3")
for fruit in list_fruits:
	answer="None"
	while answer.lower() not in ['yes','no']:
		answer=input("Do you like "+fruit.lower()+" ? [yes/no]:")
	if answer.lower()=='no':
		list_fruits.remove(fruit)
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))

# Series 4
list_fruits=fruits

print("Series 4")
list_fruits_reverse=[]
for i in list_fruits:
    list_fruits_reverse.append(i[::-1])

del list_fruits[-1]
#list_fruits.pop()
print(list_fruits)
print(", ".join(["{}"]*len(list_fruits)).format(*list_fruits))
print(list_fruits_reverse)
print(", ".join(["{}"]*len(list_fruits_reverse)).format(*list_fruits_reverse))
