#!/usr/bin/env python3

global donors
donors = [["baby huey", 1123.00, 456.00, 1789.00], ["mighty mouse", 99.99], ["fred flintstone", 5550.00, 5555.00], ["road runner", 199999.00], ["papa smurf", 1001.00, 1002.00, 1003.00]]

def prompt():
    action = (input("Choose an action:\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\n4 - Quit\n>>>> ").lower())
    if action == "1":
        thank_you()
    elif action == "2":
        create_report()
    elif action == "3":
        letters()
    elif action == "4" or action == "4":
        print("Have a nice day!")
    else:
        print("Please enter 1, 2, 3, or 4\n")
        prompt()

def thank_you():
    person = (input("Who would you like to send a Thank You to?\nYou can type 'list' to get a list of current donors: ").lower())
    if person == "quit" or person == "q":
        print ("Have a nice day!")
    elif person == "list":
        try_again()
    for i in donors:
        if i[0] == person:
            donation = float(input("How much was the donation? "))
            i.append(donation)
            print("\n" + person.title() + ":\n")
            print("\tThank you very much for your generouse donation. Your")
            print(f'${donation:.2f} donation will allow us to continue our efforts.')
            print("Our charity would not exist without your support.\n")
            print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
            prompt()
    new = (input("That looks like a new donor. Would you like to add a new donor? (Y)es or (N)o? ").lower())
    if new == "yes" or new == "y":
        donors.append([person])
        donation = float(input("How much was the donation? "))
        donors[-1].append(donation)
        print("\n" + person.title() + ":\n")
        print("\tThank you very much for your generouse donation. Your")
        print(f'${donation:.2f} donation will allow us to continue our efforts.')
        print("Our charity would not exist without your support.\n")
        print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
        prompt()
    else:
        prompt()

def try_again():
        donors_list = []
        for i in donors:
            if type(i[0]) is str:
                donors_list.append(i[0])
        print("\nPlease select from the names below, be sure to spell them correctly.")
        print(', '.join(donors_list), "\n")
        thank_you()

def create_report():
    donors_list = []
    z = 0
    print(donors)
    for i in donors:
        donors_list.append([i[0]]) #name
        donors_list[z].append(sum(i[1:])) #total
        donors_list[z].append(len(i)) #number + 1
        aa=sum(i[1:])
        donors_list[z].append(aa/len(i)) #average
        z += 1
    print("\nDonor Name\t\t| Total Given | Num Gifts | Average Gift")
    print("----------------------------------------------------------------")
    donors_list.sort(key = lambda x: int(x[1]),reverse=True)
    for i in donors_list:
        print("{:<22}".format(i[0]).title(), "  $", "{:11.2f}".format(i[1]), "\t\t{:<2}".format(i[2]-1), "{:2}".format("$"), "{:10.2f}".format(i[3]))
    print("\n")
    prompt()

def letters():
    donors_list = []
    z = 0
    for i in donors:
        donors_list.append([i[0]]) #name
        donors_list[z].append(sum(i[1:])) #total
        donors_list[z].append(len(i)) #number + 1
        aa=sum(i[1:])
        donors_list[z].append(aa/len(i)) #average
        z += 1
    for i in donors_list:
        name = (i[0])
        total = (i[1]) 
        with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/letters/' + name + ".txt", 'w') as f:
            f.write("\n\n" + name + ":\n\tThank you very much for your generous donation. ")
            f.write(f"your donation total of ${total:.2f} is awesome ")
            f.write("Our charity would not exist without your support.\n")
            f.write("Sincerely:\n\nLeadership Team at Charity X.\n\n")
    prompt()
    print("Letters Complete!\n")
    prompt()




if __name__ == '__main__':
    prompt() 


