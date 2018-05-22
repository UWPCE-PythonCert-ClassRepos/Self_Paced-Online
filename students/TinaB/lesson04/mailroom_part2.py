#!/usr/bin/env python3
"""
$ chmod +x mailroom_part2.py
"""
import datetime
import os

# list of donors
donors_list_dictionary = [{"firstname": "William", "lastname": "Gates", "donations": [326892.24, 122, 22, 12], "donate_times": [4]},
                          {"firstname": "Mark", "lastname": "Zuckerberg", "donations": [
                              30, 60, 65982.55], "donate_times": [3]},
                          {"firstname": "Jeff", "lastname": "Bezos",
                              "donations": [52636.27], "donate_times": [1]},
                          {"firstname": "Paul", "lastname": "Allen",
                              "donations": [877.33, 22], "donate_times": [2]},
                          {"firstname": "Steven", "lastname": "Hawking", "donations": [
                              326892.24, 123, 123.33, 123, 123], "donate_times": [5]},
                          {"firstname": "Justin", "lastname": "Timberlake", "donations": [999658.25, 1233, 123], "donate_times": [3]}]

# Menus
def menu_selection(prompt, dispatch_dict):
    while True:  # loop forever until they quit
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


def single_print_sub_menu():
    menu_selection(single_print_sub_prompt, single_print_sub_dispatch)


def quit():
    print("Quitting this menu now")
    return "exit menu"

# functions for prompts ----


def get_name_input():
    # Function to select user input to return to print function
    user_input = input("\nLookup donor by: \n"
                       "\t1. Firstname: \n"
                       "\t2. Lastname:\n"
                       "Please enter 1 or 2 >>  ")

    donor_return = []
    donor_check = 0
    if int(user_input) == 1:
        fname = input(
            "Type the first name of the donor you are looking for:  ")
    else:
        lname = input("Type the last name of the donor you are looking for:  ")

    for donor in donors_list_dictionary:
        # print(donor["firstname"].lower())
        if int(user_input) == 1:
            if fname.lower() in donor["firstname"].lower():
                donor_check = input("Is this the donor you are looking for: {} {}?  Please enter yes or no:  ".format(
                    donor["firstname"], donor["lastname"]))
                if donor_check == "yes":
                    donor_return.append(donor["firstname"])
                    donor_return.append(donor["lastname"])
                    donor_check = 1
                    break
            else: # firstname is not in list
                print("HERE!")
                first_name = fname
                last_name = input(
                    "No donor with that first name found in donor list. Please provide a last name to add donor to list: ")
                donor_return.append(first_name)
                donor_return.append(last_name)
                break

        else:  # user input = 2
            if lname.lower() in donor["lastname"].lower():
                donor_check = input(
                    "Is this the donor you are looking for:  {} {}?   Please enter yes or no:  ".format(donor["firstname"], donor["lastname"]))
                if donor_check == "yes":
                    donor_return.append(donor["firstname"])
                    donor_return.append(donor["lastname"])
                    donor_check = 1
                    break
                else:
                    last_name = lname
                    first_name = input(
                        "No donor with that last name found in donor list. Please provide a first name for addition to donor list")
                    donor_return.append(first_name)
                    donor_return.append(last_name)
                    break

    return donor_return, donor_check


def send_single_thank_you():
    """ function for sending thank you message"""
    donor_name, donor_check = get_name_input()
    donor_amount = float(input('Please enter a donation amount for {} {}: '.format(
        donor_name[0], donor_name[1])))

    # search through donors with returned name - 1 means name is in list, 0 means not in list
    if donor_check == 1:
        for donor in donors_list_dictionary:
            if donor["firstname"] == donor_name[0] and donor["lastname"] == donor_name[1]:
                donor["donations"].append(donor_amount)
                donor["donate_times"]+=1
                thank_you_letter = print_thank_you(
                    donor["firstname"], donor_amount)
                print(thank_you_letter)
                break
    else:
        # add new donor to list
        donors_list_dictionary.append(
            {"firstname": donor_name[0], "lastname": donor_name[1], "donations": [donor_amount], "donate_times": 1})
        thank_you_letter = print_thank_you(donor_name[0], donor_amount)
        print(thank_you_letter)


def print_donors_names():
    """ prints list of donors"""
    print()
    for d in donors_list_dictionary:
        print("{firstname} {lastname}".format(**d))
    print()


def print_thank_you(donor_fname, amount):
    """ prints thank you message"""
    d = {'name': donor_fname, 'donation': amount}
    thank_you = '\nDear {},\n '.format(donor_fname)
    thank_you += '\tThank you for your generous donation of ${donation:,.2f}\n'.format(
        **d)
    thank_you += 'Sincerely, \nThe ChickTech Donations Department\n'
    return thank_you


def print_thank_you_total(donor):
    """ prints thank you message"""
    #d = {'name': donor_fname, 'donation': amount}
    donor_output = {"firstname": donor["firstname"],"lastname": donor["lastname"] }
    all_donations = donor["donations"]
    donor_output['last_donation'] = all_donations[len(all_donations) - 1]
    total = 0
    for gift in all_donations:
        total += gift
    donor_output['total_donations'] = total
    thank_you = '''\nDear {firstname} {lastname}\n
        \t Thank you for your most recent generous donation of ${last_donation:,.2f}\n
        \t You're support of {total_donations} over the years has helped us fund many great programs!
        \t Again, thank you! We love your support.
            Sincerely, 
            \n The ChickTech Donations Department\n
    '''.format(**donor_output)
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
    for donor in donors_list_dictionary:
        donor_fullname = "{firstname} {lastname}".format(**donor)
        # donor object will hold fullname, donation total, donation times, average donation
        donor_info = [donor_fullname, 0, 0, 0]
        for donor_amount in donor["donations"]:
            donor_info[1] += donor_amount
            donor_info[2] += 1
        donor_info[3] = donor_info[1] // donor_info[2]
        donor_list.append(donor_info)

        print('{:<22}{}{:>12.2f}{:>10}{:>8}{:>12.2f}'.format(donor_fullname, '$',
                                                             donor_info[1], donor_info[2], '$', donor_info[3]))
    print()


def send_letters_everyone():
    """Creates a letter for everyone in the database, and writes them to file."""
    letters_count = 0
    new_folder = str(datetime.datetime.now())
    try:
        os.mkdir(new_folder)
    except OSError as oserr:
        print("\nError with directory creation.Something must have gone wrong!\n")
        return
    for donor in donors_list_dictionary:
        # create file in date folder titled with donor name
        filename = "./{dir}/{firstname}_{lastname}.txt".format(**donor, dir=new_folder)
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
               "Type 1,2,3 or q to exit >> "
               )

main_dispatch = {"1": single_print_sub_menu,
                 "2": print_report,
                 "3": send_letters_everyone,
                 "q": quit,
                 }

single_print_sub_prompt = ("\nWelcome to the Send A Thank You Menu:\n"
                           "How would you like to find a donor: \n"
                           '\t1. Lookup Donor By Name \n'
                           '\t2. Print List of donors\n'
                           "Type 1,2 or q to return to main menu >>> "
                           )

single_print_sub_dispatch = {"1": send_single_thank_you,
                             "2": print_donors_names,
                             "q": quit,
                             }

if __name__ == '__main__':
    while True:
        menu_selection(main_prompt, main_dispatch)
