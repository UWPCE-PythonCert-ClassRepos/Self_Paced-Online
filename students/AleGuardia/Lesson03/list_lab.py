#!/usr/bin/env python3

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)
response = input("Please enter another fruit : ")
fruit_list.append(response)
print(fruit_list)
response = input("Please enter a number :")
print("The fruit corresponding to {} is {}".format(response, fruit_list[int(response)-1]))
