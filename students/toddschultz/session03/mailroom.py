#!/usr/bin/env python3

global donors
donors = ["Baby Huey", 123.00, 456.00, 789.00, "Mighty Mouse", 999.99, "Fred Flintstone", 50.00, 55.00, "Road Runner", 999.00, "Papa Smurf", 1001.00, 1002.00, 1003.00]

def prompt():
    action = input("Would you like to (S)end a Thank You, (C)reate a Report or (Q)uit? ")
    if action.lower() == "s":
        thank_you()
    elif action.lower() == "c":
        create_report()
    elif action.lower() == "q":
        print("Have a nice day!")
    else:
        print("Please enter S, C, or Q.")
        prompt()

def thank_you():
    person = (input("Who would you like to send a Thank You to? "))
    if person.lower() == "list":
        try_again()
    elif person in donors: 
        donation = float(input("How much was the donation? "))
        location = donors.index(person)
        donors.insert((location + 1),donation)
        print("\n\n" + person + ":\n")
        print("\tThank you very much for your generouse donation.")
        print(f'Your ${donors[location+1]:.2f} donation will allow us to continue our efforts.')
        print("Our charity would not exist without your support.\n")
        print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
        prompt()
    else:
        try_again()

def try_again():
        donors_list = []
        for i in donors:
            if type(i) is str:
                donors_list.append(i)
        print(donors_list) #todo: Make this appear not in bracket, join?
        print("Please select from the names above, be sure to spell them correctly.")
        thank_you()

def create_report():
#First gather the names of the donors from the global list
    donors_list = []
    for i in donors:
        if type(i) is str:
            donors_list.append(i)
#Get the integers that come after each donor in the global list
    c = len(donors)
    for x in donors_list:
        total = 0.00
        num = 1
        average = 0.00
        a = donors.index(x)
        b = a + 1
        while type(donors[b]) is float:
            total = total + donors[b]
            print(donors[a], num, total, total/num)
            b += 1
            num += 1
            if b == c:
                break
#Now we have donor, donations, number of donations, total, and average; need to format it. 





prompt()