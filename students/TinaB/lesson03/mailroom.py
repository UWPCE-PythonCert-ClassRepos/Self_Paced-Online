#!/usr/bin/env python3
"""
Goal:
The Program

Script to pull list of donors and print a thank you letter.

"""
# list of donors
donors_list = [
    ['William Gates, III', 326892.24, 4],
    ['Mark Zuckerberg', 65982.55, 3],
    ['Jeff Bezos', 52636.27, 1],
    ['Paul Allen', 877.33, 2],
    ['Steven Hawking', 326892.24, 5],
    ['Justin Timberlake', 999658.25, 3]]


def send_thank_you():
    """ function for sending thank you message"""
    donors_list_copy = []
    for donor in donors_list:
        donors_list_copy.append(donor)

    while True:
        print()
        print('Welcome to the Send A Thank You Menu:')
        thankyou_input = input('\tEnter The Last Nanme of a donor \n'
                               '\tType "list" for a list of donors, or \n'
                               '\tType "quit" to quit\n'
                               '---->  ')
        # print(thankyou_input)
        if thankyou_input.isalpha():
            if thankyou_input.lower().startswith('q'):
                break
            elif thankyou_input.lower() == 'list':
                print_donors_names()
                thankyou_input = input('Please enter the name of the donor: ')
                # print(thankyou_input)
            # search through donors for matching name
            for idx, donor in enumerate(donors_list_copy):
                if thankyou_input.lower() in donor[0].lower():
                    donor_check = input(
                        "Is this the donor you are looking for:  {}?   Please enter yes or no:  ".format(donor[0]))
                    if donor_check.lower().startswith('y'):
                        donor_amount = float(
                            input('Please enter a donation amount:  '))
                        donors_list[idx][1] += donor_amount
                        donors_list[idx][2] += 1
                        print_thank_you(donor, donor_amount)
                        break
                #Sprint('{}  {}'.format(donor[0], thankyou_input.lower()))
            else:
                print("No donor matching that name is in the list. We will add {} to the donor list. ".format(
                    thankyou_input))
                donor_fname = input(
                    "Please enter {}'s first name: ".format(thankyou_input))
                donor_name = donor_fname + ' ' + thankyou_input
                donor_amount = float(
                    input('Please enter a donation amount:  '))
                donors_list.append([donor_name, donor_amount, 1])
                print()
                print_thank_you(donor_name, donor_amount)


def print_donors_names():
    """ prints list of donors"""
    print()
    for donor in donors_list:
        print(donor[0])
    print()


def print_thank_you(donor, amount):
    """ prints thank you message"""
    amounts = float(amount)
    print('Dear {},\n '.format(donor))
    print(
        '\tThank you for your generous donation of ${:,.2f}\n'.format(amounts))
    print('Sincerely, \n'
          'ChickTech Donations Department')


def print_main_menu():
    """ prints main menu  """
    print("Welcome to the Mailroom App")
    print('\nOptions Menu:\n'
          '\t1. Send a Thank You\n'
          '\t2. Create a Report\n'
          '\t3. Quit\n')


def print_report():
    """Print report to match example from assignment for donor list """
    print()
    title = ['Donor Name', '|  Total Given', '| Num Gifts',
             '  | Average Gift']
    print('{:<20}{:>12}{:^12}{:>12}'.format(title[0], title[1],
                                            title[2], title[3]))
    print('-'*60)
    print()
    for donor in donors_list:
        print('{:<20}{}{:>12,.2f}{:>12}{}{:>12,.2f}'.format(donor[0], '  $',
                                                            donor[1], donor[2], '  $', donor[1] // donor[2]))
    print()


if __name__ == '__main__':
    while True:
        print_main_menu()
        selected_option = int(input('Enter Your Selection Here: '))
        if selected_option == 1:
            send_thank_you()
        elif selected_option == 2:
            print_report()
        elif selected_option == 3:
            print('The End - Clsoing Program')
            break
    else:
            selected_option = input('Please enter "1", "2", or "3": ')
            if selected_option == 1 or selected_option == 2:
                continue
            elif selected_option == 3:
                print('The End - Clsoing Program')
                break
            else:
                print('Game Over - command not recognized... Closing program.')
                break
