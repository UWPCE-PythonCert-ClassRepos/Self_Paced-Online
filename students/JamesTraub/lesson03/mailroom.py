#!/usr/bin/env python3.6
# James Traub 04-17-18
# Lesson 3 - Mailroom Lab Exercise, Part 1

# Write a small command-line script called mailroom.py.
# This script should be executable. 
# The script should accomplish the following goals:
# It should have a data structure that holds a list 
# of your donors and a history of the amounts they have donated.
# This structure should be populated at first with at least 
# five donors, with between 1 and 3 donations each.
# You can store that data structure in the global namespace.
# The script should prompt the user to choose from a menu 
# of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)

# Create list containg (("Donor #1[use index?]:" donor name, 
# Donation 01-01: 10, Donation 01-02: 10, Donation 01-03: 10), 
# ("Donor #2 [use index?]:", donation 02-01: 10, Donation 02-02: 10),)

def thanks():


def reporting():
    

print()
print("    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("        Mailroom Main Menu")
print("    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n")
print("    Option 1: \'Send a Thank You\'\n")
print("    Option 2: \'Create a Report\'\n")
print("    Option 3: \'Quit\'\n")
print()

menu_input = ''

while menu_input != '3':
    menu_input = input("Please enter an option from the Mailroom Main Menu: ")
    if menu_input == '1':
    	print("Send a Thank you")
    elif menu_input == '2':
        print("Create a Report")
    else:
        print("Good bye.")
