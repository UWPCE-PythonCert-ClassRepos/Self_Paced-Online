#!/usr/bin/env python3
"""
$ chmod +x mailroom_part4.py
"""
import datetime
import os

DONORS_DICT = {"William Gates": [326892.24, 122, 22, 12],
               "Mark Zuckerberg": [30, 60, 65982.55],
               "Jeff Bezos": [52636.27],
               "Paul Allen": [877.33, 22],
               "Steven Hawking": [326892.24, 123, 123.33, 123, 123],
               "Justin Timberlake": [999658.25, 1233, 123]}

# Menus

def menu_selection(menu_input, user_entry):
    """menu function"""
    try:
        menu_input[user_entry]['menu_dispatch']()
    except KeyError:
        print("{} is not a valid choice. ".format(user_entry))
        return False
    else:
        return True

def quit_menu():
    '''Quit menu function and method'''
    print("Quitting this menu now")
    return "exit menu"

def main_menu():
    '''Create Main Menu'''
    main_menu_title = "\nWelcome to the Mailroom App\nWhat would you like to do?\n"
    print_menu_options(MAIN_MENU, main_menu_title)


def single_print_menu():
    '''Create single print sub Menu'''
    single_print_menu_title = "\nWelcome to the Send A Thank You Menu:\nHow would you like to find a donor: \n"
    print_menu_options(SINGLE_PRINT_SUB_MENU, single_print_menu_title)


def print_menu_options(menu_input, menu_title):
    ''' Prints  Menu'''
    while True:
        print(menu_title)
        for key, value in menu_input.items():
            # prints each option and then prompts for user input
            print(key, value['menu_prompt'])
        response = input("\nEnter a number or q to exit menu>>>  ")
        menu_selection(menu_input, response)
        if response == 'q':
            return


# functions for prompts and processing ----

def get_name_input():
    ''' Function to select user input to return to print function 
        USER INTERACTION'''
    name_input = input(
        "Please enter the name of the donor:  ")

    for donor, donations in DONORS_DICT.items():
        if name_input.lower() in donor.lower():
            donor_check = input(
                "Is this the donor you are looking for: {}?\nPlease type yes or no >> ".format(
                    donor))
            if donor_check == 'yes':
                return donor

    print("{} is not in our records. Let's add {} to our list!".format(
        name_input, name_input))
    while True:
        new_donor_name = input(
            "Please enter the full name of the donor or type 'exit' to quit>> ")
        if new_donor_name == 'exit':
            return "quit"
        name_check = input(
            "IS this the donor name you would like to add: {} ?\nPlease type yes or no exit to quit>> ".format(new_donor_name))
        if name_check == 'yes':
            print("Adding {} to donor list".format(new_donor_name))
            return new_donor_name
        elif name_check == 'exit':
            return "quit"
        else:  # anything other then yes
            print(
                "Let's try entering the donor name again. Or type 'exit' to quit to menu.")

def send_single_thank_you():
    """ function for sending thank you message - gets/ adds single donation and prints thank you"""
    donor_name = get_name_input()
    if donor_name == "quit":
        print("No donor name entered, exiting to menu")
    else:
        donor_amount = check_number_input()

        DONORS_DICT.setdefault(donor_name, []).append(donor_amount)

        thank_you_letter = print_thank_you(donor_name, donor_amount)
        print(thank_you_letter)


def print_donors_names():
    """ prints list of donors"""
    print("\nDonors")
    print("-"*20)
    [print(d) for d in DONORS_DICT]
    # for d in DONORS_DICT:
    #     print(d)


def print_donors_and_donations():
    print("\nDonors and donations")
    print("-"*30, "\n")
    [print(key, "=>", val, '\n') for key, val in DONORS_DICT.items()]
    # for key, val in DONORS_DICT.items():
    #     print(key, "=>", val)


def check_number_input():
    '''Error Handling: Checks if number was entered by converting the number to a float'''
    while True:
        try:
            number = float(input('Please enter a donation amount : '))
        except ValueError:
            print("Please enter a number for donation amount!")
        else:
            if number > 0.0:
                return number
            else:
                print('Please enter a donation amount above 0.')


def print_thank_you(donor_name, amount):
    """ prints thank you message"""
    thank_you = '\nDear {},\n '.format(donor_name)
    thank_you += '\tThank you for your generous donation of ${:,.2f}\n'.format(
        amount)
    thank_you += 'Sincerely, \nThe ChickTech Donations Department\n'
    return thank_you


def print_thank_you_total(donor):
    """ prints thank you message"""
    donor_output = {"name": donor}
    all_donations = DONORS_DICT[donor]
    donor_output['last_donation'] = all_donations[- 1]
    total = sum(all_donations)
    donor_output['total_donations'] = total
    thank_you = '''\n\nDear {name}

Thank you for your most recent generous donation of ${last_donation:,.2f}. You're support of ${total_donations:,.2f}
over the years has helped us fund many great programs!We wanted to write you to thank you and that we 
look forward to your continued support!

Sincerely,


The ChickTech Donations Department'''.format(**donor_output)
    return thank_you


def print_report():
    """Print report to match example from assignment for donor list """
    print()
    title = ['Donor Name', '|  Total Given ', '|   Num Gifts',
             '  | Average Gift']
    print('{:<20}{:>14}{:^14}{:>14}'.format(title[0], title[1],
                                            title[2], title[3]))
    print('-'*65)
    print()
    # Creating list to hold donors info for printing
    donor_list = list()
    for donor, donations in DONORS_DICT.items():
        # donor object will hold fullname, donation total, donation times, average donation
        donor_info = [donor, 0, 0, 0]
        donor_info[1] = sum(donations)
        donor_info[2] = len(donations)
        donor_info[3] = donor_info[1] // donor_info[2]
        donor_list.append(donor_info)

        print('{:<22}{}{:>12.2f}{:>10}{:>8}{:>12.2f}'.format(donor, '$',
                                                             donor_info[1], donor_info[2],
                                                             '$', donor_info[3]))
    print()


def send_letters_everyone():
    """Creates a letter for everyone in the database, and writes them to file."""
    letters_count = 0
    date = datetime.datetime.now()
    new_folder = date.strftime("%Y-%m-%d_%H-%M")
    try:
        os.mkdir(new_folder)
    except OSError:
        print("\nError with directory creation.Something must have gone wrong!\n")
        return
    for donor, donation in DONORS_DICT.items():
        # create file in date folder titled with donor name
        filename = "./{}/{}.txt".format(new_folder, donor)
        with open(filename, 'w') as donor_thanks:
            letter_output = print_thank_you_total(donor)
            donor_thanks.write(letter_output)
        letters_count += 1
    print("Created {} Thank You letters in this folder: {}".format(
        letters_count, new_folder))


def print_letters_to_everyone():
    '''test print all function'''
    print()
    for donor in DONORS_DICT:
        print(print_thank_you_total(donor))


#------Menu Dictionaries of Dictionaries .Needs to be after the functions or code won't work. ------
MAIN_MENU = {
    "1": {'menu_prompt': 'Send a Single Thank You', 'menu_dispatch': single_print_menu},
    "2": {'menu_prompt': 'Create a Report', 'menu_dispatch': print_report},
    "3": {'menu_prompt': 'Send Letters to Everyone', 'menu_dispatch': send_letters_everyone},
    "4": {'menu_prompt': 'Test Print All', 'menu_dispatch': print_letters_to_everyone},
    "q": {'menu_prompt': 'Quit Program', 'menu_dispatch': quit_menu}
}
SINGLE_PRINT_SUB_MENU = {
    "1": {'menu_prompt': 'Lookup Donor By Name', 'menu_dispatch': send_single_thank_you},
    "2": {'menu_prompt': 'Print List of donors', 'menu_dispatch': print_donors_names},
    "3": {'menu_prompt': 'Print Donors list with donations', 'menu_dispatch': print_donors_and_donations},
    "q": {'menu_prompt': 'Quit to Main Menu', 'menu_dispatch': quit_menu}}

if __name__ == '__main__':
    main_menu()

