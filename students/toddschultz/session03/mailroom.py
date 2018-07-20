#!/usr/bin/env python3

global donors
donors = ["Baby Huey", 1123.00, 456.00, 1789.00, "Mighty Mouse", 99.99, "Fred Flintstone", 5550.00, 5555.00, "Road Runner", 199999.00, "Papa Smurf", 1001.00, 1002.00, 1003.00]

def prompt():
    action = input("Would you like to (S)end a Thank You, (C)reate a Report or (Q)uit? ")
    if action.lower() == "s":
        thank_you()
    elif action.lower() == "c":
        create_report()
    elif action.lower() == "q" or action.lower() == "quit":
        print("Have a nice day!")
    else:
        print("Please enter S, C, or Q.")
        prompt()

def thank_you():
    person = (input("Who would you like to send a Thank You to?\nYou can type 'list' to get a list of current donors: "))
    if person.lower() == "quit" or person.lower() == "q":
        print ("Have a nice day!")
    elif person.lower() == "list":
        try_again()
    elif person in donors:
        donation = float(input("How much was the donation? "))
        location = donors.index(person)
        donors.insert((location + 1),donation)
        print("\n" + person + ":\n")
        print("\tThank you very much for your generouse donation. Your")
        print(f'${donors[location+1]:.2f} donation will allow us to continue our efforts.')
        print("Our charity would not exist without your support.\n")
        print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
        prompt()
    else:
        new = (input("That looks like a new donor. Would you like to add a new donor? (Y)es or (N)o? "))
        if new.lower() == "yes" or new.lower() == "y":
            donors.append(person)
            prompt()
        else:
            prompt()

def try_again():
        donors_list = []
        for i in donors:
            if type(i) is str:
                donors_list.append(i)
        print("\nPlease select from the names below, be sure to spell them correctly.")
        print(', '.join(donors_list))
        thank_you()

def create_report():
#First gather the names of the donors from the global list
    donors_list = []
    for i in donors:
        if type(i) is str:
            donors_list.append(i)
#Get the integers that come after each donor in the global list
    print("\nDonor Name\t\t| Total Given | Num Gifts | Average Gift")
    print("----------------------------------------------------------------")
    c = len(donors)
    for x in donors_list:
        total = 0.00
        num = 0
        average = 0.00
        a = donors.index(x)
        b = a + 1
        while type(donors[b]) is float:
            total = total + donors[b]
            b += 1
            num += 1
            if b == c:
                break
#Now we have donor, donations, number of donations, total, and average; need to format it. 

        print("{:<22}".format(donors[a]), "  $", "{:11.2f}".format(total), "\t\t{:<2}".format(num), "{:2}".format("$"), "{:10.2f}".format(total/num))
    print("\n")
    prompt()

if __name__ == '__main__':
    prompt() 
