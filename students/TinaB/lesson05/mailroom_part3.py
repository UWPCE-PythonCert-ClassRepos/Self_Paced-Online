#!/usr/bin/env python3
"""
$ chmod +x mailroom_part3.py
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


def menu_selection(prompt, dispatch_dict):
    """menu function"""
    while True:  # loop forever until they quit
        response = input(prompt)
        print(response)
        if dispatch_dict[response]() == "exit menu":
            print("I am here")
            break


def single_print_sub_menu():
    '''Sub Menu for Print single Thank you menu'''
    menu_selection(single_print_sub_prompt, single_print_sub_dispatch)


def quit_menu():
    '''Quit menu function and method'''
    print("Quitting this menu now")
    return "exit menu"

# functions for prompts ----


def get_name_input():
    ''' Function to select user input to return to print function'''
    name_input = input(
        "Please enter the name of the donor:  ")

    for donor, donations in DONORS_DICT.items():
        if name_input.lower() in donor.lower():
            donor_check = input(
                "Is this the donor you are looking for: {}?\nPlease type yes or no >> ".format(donor))
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
            "Does the spelling look right: {}?\nPlease type yes or no >> ".format(new_donor_name))
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
        print("No donor name chosed, exit to menu")
    else:
        donor_amount = check_number_input()

        DONORS_DICT.setdefault(donor_name, []).append(donor_amount)

        thank_you_letter = print_thank_you(donor_name, donor_amount)
        print(thank_you_letter)


def print_donors_names():
    """ prints list of donors"""
    print("\nDonors")
    print("-"*20)
    [print(d, "\n") for d in DONORS_DICT]
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
            print("Please enter a number for donation amaount!")
        else:
            return number


def print_thank_you(donor_name, amount):
    """ prints thank you message"""
    d = {'name': donor_name, 'donation': amount}
    thank_you = '\nDear {},\n '.format(donor_name)
    thank_you += '\tThank you for your generous donation of ${donation:,.2f}\n'.format(
        **d)
    thank_you += 'Sincerely, \nThe ChickTech Donations Department\n'
    return thank_you


def print_thank_you_total(donor):
    """ prints thank you message"""
    donor_output = {"name": donor}
    print(donor)
    all_donations = DONORS_DICT[donor]
    donor_output['last_donation'] = all_donations[- 1]
    total = 0
    for gift in all_donations:
        total += gift
    donor_output['total_donations'] = total
    thank_you = '''\nDear {name} \n
        \t Thank you for your most recent generous donation of ${last_donation:,.2f}
        \t You're support of {total_donations} over the years has helped us fund many great programs!
        \t Again, thank you! We love your support.
            Sincerely,
            \n The ChickTech Donations Department\n
    '''.format(**donor_output)
    return thank_you


def print_report_test():
    '''test print all function'''
    print()
    for donor in DONORS_DICT:
        print(print_thank_you_total(donor))


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
        for donor_amount in donations:
            donor_info[1] += donor_amount
            donor_info[2] += 1
        donor_info[3] = donor_info[1] // donor_info[2]
        donor_list.append(donor_info)

        print('{:<22}{}{:>12.2f}{:>10}{:>8}{:>12.2f}'.format(donor, '$',
                                                             donor_info[1], donor_info[2], '$', donor_info[3]))
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
            donor_thanks.write(''.join(letter_output))
        letters_count += 1
    print("Created {} Thank You letters in this folder: {}".format(
        letters_count, new_folder))


#------Needs to be after the functions or code won't wrk. -------
main_prompt = ("\nWelcome to the Mailroom App\n"
               "Options Menu:\n"
               '\t1. Send a Single Thank You\n'
               '\t2. Create a Report\n'
               '\t3. Send Letters to Everyone\n'
               '\t4. report test\n'
               '\tq. Quit Program\n'
               "Type 1,2,3,4 or q to exit >> "
               )

main_dispatch = {"1": single_print_sub_menu,
                 "2": print_report,
                 "3": send_letters_everyone,
                 "4": print_report_test,
                 "q": quit_menu,
                 }

single_print_sub_prompt = ("\nWelcome to the Send A Thank You Menu:\n"
                           "How would you like to find a donor: \n"
                           '\t1. Lookup Donor By Name \n'
                           '\t2. Print List of donors\n'
                           '\t3. Print Donors list with donations\n'
                           "Type 1,2,3 or q to return to main menu >>> "
                           )

single_print_sub_dispatch = {"1": send_single_thank_you,
                             "2": print_donors_names,
                             "3": print_donors_and_donations,
                             "q": quit_menu,
                             }

if __name__ == '__main__':
    while True:
        menu_selection(main_prompt, main_dispatch)
