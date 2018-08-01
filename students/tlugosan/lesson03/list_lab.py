#! python

"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”"""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
"""Display the list"""
print(fruit_list)
"""Ask for another fruit and add it to the end"""
response1 = input("Please provide another fruit: ")
fruit_list.append(response1.capitalize())
"""Display list."""
print(fruit_list)
"""Ask for a number and display the number and the corespnding fruit on a 1-is basis."""
response2 = int(
    input("Please provide a number between 1 and %s: " % len(fruit_list)))
while True:
    if response2 < 1 or response2 > len(fruit_list):
        response2 = int(
            input("Try again a number between 1 and %s: " % len(fruit_list)))
    else:
        break
print("%d : %s" % (response2, fruit_list[response2 - 1]))
"""Add another fruit at the beginning of the list using +  then print the list"""
response3 = input("Please provide another fruit: ")
fruit_list = [response3.capitalize()] + fruit_list
print(fruit_list)
""" Add another fruit at the beginning at the list using insert() function"""
response4 = input("Please provide another fruit: ")
fruit_list.insert(0, response4.capitalize())
print(fruit_list)
"""Display all the fruits that start with P using a for loop"""
for item in fruit_list:
    if item.startswith("P"):
        print(item, end=" ")

