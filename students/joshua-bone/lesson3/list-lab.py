#!/usr/bin/env python3

# Joshua Bone - UW Python 210 - Lesson 3
# 12/10/2018
# List Lab Exercise
import time
from collections import OrderedDict

PAUSE = 0.5
LONG_PAUSE = 1.5


def slow_print(*args):
    time.sleep(PAUSE)
    print(*args)


def slow_input(s):
    time.sleep(PAUSE)
    return input(s)

slow_print("Series 1")
s1 = ["Apples", "Pears", "Oranges", "Peaches"]
slow_print("The fruit basket contains: ", s1)
s1.append(input("What fruit should we add? "))
slow_print("Added %s" % s1[-1])
slow_print("The fruit basket contains: ", s1)
slow_print("You selected: ",
           s1[int(input("Enter the number of the fruit to display: ")) - 1])
new_fruit = "Pomegranates"
slow_print("Adding %s" % new_fruit)
s1 = [new_fruit] + s1
slow_print("The fruit basket contains: ", s1)
new_fruit = "Passionfruit"
slow_print("Adding %s" % new_fruit)
s1.insert(0, new_fruit)
slow_print("The fruit basket contains: ", s1)
starts_with = "P"
slow_print("Fruits that start with %s: " % starts_with,
           [f for f in s1 if f[0] == starts_with])

# Series 2
time.sleep(LONG_PAUSE)
slow_print("\n\nSeries 2")
slow_print("The fruit basket contains: ", s1)
slow_print("Removed the last fruit: ", s1.pop())
slow_print("The fruit basket contains: ", s1)
slow_print("Doubling the fruit basket...")
s1 = s1 * 2
while True:
    slow_print("The fruit basket contains: ", s1)
    to_remove = slow_input("Enter the name of the fruit to remove: ")
    if to_remove in s1:
        s1 = list(filter(lambda f: f != to_remove, s1))
        slow_print("Removed: ", to_remove)
        break
    slow_print("Sorry, %s was not found in the fruit basket." % to_remove)
slow_print("The fruit basket contains: ", s1)

# Series 3
time.sleep(LONG_PAUSE)
slow_print("\n\nSeries 3")
slow_print("Removing duplicates from fruit basket.")
s1 = list(OrderedDict.fromkeys(s1))
f = 0
while f < len(s1):
    ans = slow_input("Do you like %s? (yes/no): " % s1[f])
    if ans.lower() == "no":
        slow_print("We've removed %s from your basket." % s1.pop(f))
    elif ans.lower() == "yes":
        f += 1
    else:
        slow_print("Sorry, I don't understand. Please answer yes or no.")
slow_print("The fruit basket contains: ", s1)

# Series 4
slow_print("\n\nSeries 4")
s1_copy = [s[::-1] for s in s1]
s1.pop()
slow_print("The reversed fruit basket contains: ", s1_copy)
slow_print("The fruit basket contains: ", s1)

