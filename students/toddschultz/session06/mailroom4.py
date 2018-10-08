#!/usr/bin/env python3

global donors
donors = [["baby huey", 1123.00, 456.00, 1789.00], ["mighty mouse", 99.99], ["fred flintstone", 5550.00, 5555.00], ["road runner", 199999.00], ["papa smurf", 1001.00, 1002.00, 1003.00]]

def menu_selection(prompt, dispatch_dict):
    try:
        while True:
            response = input(prompt)
            if dispatch_dict[response]() == "exit_menu":
                break
    except KeyError:
        print ("\nPlease enter 1, 2, 3, or 4.")
        menu_selection(main_prompt, main_dispatch)

def send_thank_you():
    ''' Check for list or quit, otherwise call create_thank_you. '''
    person = (input("Who would you like to send a Thank You to?\nYou can type 'list' to get a list of current donors: ").lower())
    if person == "quit" or person == "q":
        print ("Have a nice day!")
    elif person == "list":
        try_again()
    try:
        donation = float(input("How much was the donation? "))
    except ValueError:
        print("Please enter a number.")
        send_thank_you()

    create_thank_you(donation, person)

def create_thank_you(donation, person):
    ''' Create Print the thank you if match is found, otherwise call new_donor(). '''
    for i in donors:
        if i[0] == person:
            i.append(donation)
            d = dict()
            d['name'] = i[0].title()
            d['amount'] = donation
            d['total'] = (sum(i[1:]))
            d['donations'] = (len(i) - 1)
            print("\n{name}\n".format(**d))
            print("\tThank you very much for your generous donation. Your")
            print("${amount:.2f} donation will allow us to continue our efforts.".format(**d))
            print ("You have donated {donations} times totalling ${total:.2f}; AWESOME!!!".format(**d))
            print("Our charity would not exist without your support.\n")
            print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
    else:
        is_new_donor(person, donation)

def is_new_donor(person,donation):
    ''' Provide the option to add a new donor, or go back to the main menu. '''
    new = (input("That looks like a new donor. Would you like to add a new donor? (Y)es or (N)o? ").lower())
    if new == "yes" or new == "y":
       add_new_donor(person, donation)
    else:
        print("Ok, I won't add the new donor.")

def add_new_donor(person, donation):
    donors.append([person])
    donors[-1].append(donation)
    print_thank_you(person, donation)

def print_thank_you(person, donation):
    d = dict()
    d['name'] = person
    d['amount'] = donation
    print("\n{name}\n".format(**d))
    print("\tThank you very much for your generouse donation. Your")
    print("${amount:.2f} donation will allow us to continue our efforts.".format(**d))
    print("Our charity would not exist without your support.\n")
    print("Sincerely:\n\nLeadership Team at Charity X.\n\n")

def create_report(): 
    ''' Create the list of donors for the report, then call display_report. '''
    donors_list = []
    z = 0
    for i in donors:
        donors_list.append([i[0]]) #name
        donors_list[z].append(sum(i[1:])) #total
        donors_list[z].append(len(i)) #number + 1
        aa=sum(i[1:])
        donors_list[z].append(aa/len(i)) #average
        z += 1
    display_report(donors_list)

def display_report(donors_list):
    ''' format and print the report. '''
    print("\nDonor Name\t\t| Total Given | Num Gifts | Average Gift")
    print("----------------------------------------------------------------")
    donors_list.sort(key = lambda x: int(x[1]),reverse=True)
    for i in donors_list:
        print("{:<22}".format(i[0]).title(), "  $", "{:11.2f}".format(i[1]), "\t\t{:<2}".format(i[2]-1), "{:2}".format("$"), "{:10.2f}".format(i[3]))
    print("\n")

def make_donors_list(): #Letters
    ''' Make list of all the donors then call create_letters() '''
    donors_list = []
    z = 0
    for i in donors:
        donors_list.append([i[0]]) #name
        donors_list[z].append(sum(i[1:])) #total
        donors_list[z].append(len(i)) #number + 1
        aa=sum(i[1:])
        donors_list[z].append(aa/len(i)) #average
        z += 1
    create_letters(donors_list)

def create_letters(donors_list):
    ''' Create the letter files from the donors list '''
    for i in donors_list:
        name = (i[0])
        total = (i[1]) 
        with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session06/letters/' + name + ".txt", 'w') as f:
            f.write("\n\n" + name + ":\n\tThank you very much for your generous donations. ")
            f.write(f"your donation total of ${total:.2f} is awesome! ")
            f.write("Our charity would not exist without your support.\\n")
            f.write("Sincerely:\n\nLeadership Team at Charity X.\n\n")
    print("Letters Complete!\n")

def quit():
    return "exit_menu"

main_prompt = ("\nMAIN MENU\n"
                "what option would you like?\n"
                "1 - Send a Thank You\n"
                "2 - Create a report\n"
                "3 - Send letters\n"
                "4 - Exit\n"
                ">>> ")

main_dispatch = {"1": send_thank_you,
                 "2": create_report,
                 "3": make_donors_list,
                 "4": quit,}

def try_again():
        print("\nPlease select from the names below, be sure to spell them correctly.\n")
        donors_list = [print(i[0].title()) for i in donors if type(i[0]) is str]
        send_thank_you()

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)














