#!/user/bin/env python3

#SERIRES 1
'''Create a list with fruit'''
list = ["Apples", "Pears", "Oranges", "Peaches"]

"""Print the list"""
print(list)

"""Ask the user for another fruit""" 
response = input("Enter another fruit to add to the list. > ")

"""Add the user response to the list and display"""
list.append(response)
print(list)

"""Ask the user for a number and display the corresponding fruit on 1-5 basis"""
response = int(input("Enter the number of a fruit you want to see"))
response = response-1

print(response , " ", list[response])

"""Add another fruit using + and display the list"""
fruit = ["Grapes"]
list = fruit + list
print(list)

"""Add another fruit using append and display it"""
fruit = "Strawberries"
list.insert(0, fruit)
print(list)

for i in list:
    if i[0]=="P":
        print(i)
        continue
    else:
        pass

#SERIES 2

print(list)
"""delete last item on the list"""
list.pop(-1)
print(list)
"""Ask the user for a fruit to delete, find  it, and delete it"""
response = input("Enter a fruit to delete. >")
for i in list:
    if i == response:
        list.remove(i)
        continue
    else:
        pass

print(list)

#SERIES 3
"""Ask user if they like a fruit. if no, remove from list"""

for item in list[:]:
    response = input("Do you like " + item.lower() + "? >")
    if response == "yes":
        pass
    elif response == "no":
        list.remove(item)
        continue

print(list)


#SERIES 4
""""Create a copy of the list"""
list_copy = list[:]

for item in list_copy[:]:
   print(item[::-1])

"""Delete the last iem of the original list"""
list.pop(-1)

"""Print the list and the copy of the orignial list"""
print(list)
print(list_copy)
