#!/usr/bin/env python3
# Lesson 3 - Mailroom... part 1

Donations = [ ["Bill Gates", 10.50], ["Bill Gates", 123.45], ["Bill Gates",    1111.11], ["Jeff Bezos", 7.65], ["Jeff Bezos", 1000], ["Paul Allen", 145.90], ["John Nordstrom", 45.67], ["John Nordstrom", 6519.65], ["Mark Zuck", 789.12] ]

### Prompts and Flow Control ###
response = input("Welcome Chris! What would you like to do?\n(S)end a Thank You / (C)reate a Report / (Q)uit\n--> ")

while True:
    if response == "S":
        send_thank_you()
        break
    elif response == "C":
        print_report()
        break
    else:
        print("Goodbye Sir!")
        break


### Function Definitions ###

def send_thank_you():
    # Prompt for a full name
    response = input("Please enter full name of who you'd like to thank:\nBy the way, you can also type 'list' to get a list of names\n-->")

    if response == "list":
        donor_list()
        # Re-prompt for a name
    elif response # Response is name not in list






def donor_list():
    ...

def print_report():
    header = '{:20}{:^15}{:^15}{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * 65)

def total_given():
    ...

def num_gifts():
    ...

def avg_gift():
    ...

def prompt():
    ...
