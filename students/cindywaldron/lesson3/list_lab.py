#!/usr/bin/env python3

a_list = [ "Apples", "Pears", "Oranges", "Peaches"]

print(a_list)
# ask user to enter a fruit
response = input("Enter a fruit name > ")
#display user's input
print("You entered: " + response)
print(response + " is added to end of list")
# add the input to end of the list
a_list.append(response)
# display the list
print(a_list)
# ask user to enter a number
num = int(input("Enter a number > "))

#display the item
print(a_list[num-1])
# Enter another fruit
response = input("Enter another fruit name > ")
a_list2 = [response]
print(response + " is added to front of list. New list ==>")
# add the fruit to front of the list
print(a_list2 + a_list)
# enter another fruit
response = input("Enter another fruit name > ")
# insert an item to front of the list
a_list.insert(0, response)
print("Inserted " + response + " to front of list.")
#display the list
print(a_list)
# print fruit name starts with 'P'
for item in a_list:
    if 'P' in item:
        print(item)

# Series 2
print("Series 2: Display the list ==>")
print(a_list)
# remove the last fruit
a_list.pop()
print("Removed last item on list, new list ==> ")
print(a_list)
# ask for a fruit to delete
response = input("Enter a fruit to delete > ")
a_list.remove(response)
print(" Removed " + response + ", new list ==> ")
print(a_list)

#Series 3
print("Series 3: Display the list ==>")
print(a_list)
response = 'maybe'
for i in a_list[:]:
    response = input("Do you like " + i.lower() + "? ")
    while response != 'yes' and response != 'no':
        response = input("Do you like " + i.lower() + "? ")
    if response == 'no':
        a_list.remove(i)
print(a_list)

#Series 4
another_list = [x[::-1] for x in a_list][::-1]

print("Delete last item from original list, new list ==>")
a_list.pop()
print(a_list)

print("Reversed the letters in each fruit, new list ==>")
print(another_list)
