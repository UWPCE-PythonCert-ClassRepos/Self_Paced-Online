#!/usr/bin/env python3

#Series One
my_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(my_list)
my_list.append(input("Type another fruit to add to the list: "))
print(my_list)
number = int(input("Pick a number 1-5 to show it's place in the list: "))
print("You picked " + str(number) + " and the corresponding fruit is " + my_list[number - 1])
my_list = ["Mangos"] + my_list
my_list.insert(0, "Papayas")

for fruit in my_list:
    if fruit[0] == "P":
        print(fruit)


#Series Two
print(my_list)
my_list.pop(6)
print(my_list)
delete_it = input("Type which fruit to delete from the list: ")

while delete_it not in my_list:
    delete_it = input("The fruit you tried to delete was not in the list. Make sure your spelling is correct and Capitalized. Try again: ")
else:
    my_list.remove(delete_it)

print(my_list)


#Series Three
new_list = []

for fruit in my_list[:]:
    user_input = input("Do you like {}? yes or no: ".format(fruit.lower()))
    while user_input.lower() != "yes" and user_input.lower() != "no":
        user_input = input("Do you like {}? yes or no: ".format(fruit.lower()))
    if user_input.lower() == "no":
        my_list.remove(fruit)

print(my_list)


#Series Four
my_new_list = []

for fruit in my_list:
    my_new_list.append(fruit[::-1])

my_list.pop()

print("Original List = " + str(my_list))
print("New List = " + str(my_new_list))





