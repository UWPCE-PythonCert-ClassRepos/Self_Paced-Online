#!/usr/bin/env python3

# Joshua Bone - UW Python 210 - Lesson 3
# 12/10/2018
# List Lab Exercise

# Series 1
s1 = ["Apples", "Pears", "Oranges", "Peaches"]
print("The fruit basket contains: ", s1)
s1.append(input("What fruit should we add? "))
print("Added %s" % s1[-1])
print("The fruit basket contains: ", s1)
print("You selected: ",
      s1[int(input("Enter the index of the fruit to display: ")) - 1])
new_fruit = "Pomegranates"
print("Adding %s" % new_fruit)
s1 = [new_fruit] + s1
print("The fruit basket contains: ", s1)
new_fruit = "Passionfruit"
print("Adding %s" % new_fruit)
s1.insert(0, new_fruit)
print("The fruit basket contains: ", s1)
starts_with = "P"
print("Fruits that start with %s: " % starts_with,
      [f for f in s1 if f[0] == starts_with])

