#!/usr/bin/env python3
""" Automate a script to send a thank you mail, print a report of donor or quit the program."""
from operator import itemgetter

table_dictionary = {
    'Toni Orlando': [150.00, 200.00, 100.00],
    'Amanda Clark': [1800.00],
    'Robin Hood': [1234.56, 4500.34, 765.28],
    'Gina Travis': [523.10, 75.00],
    'Mark Johnson': [850.00, 20.14]
}


def select_action(actions):
    """User selects an action by its corresponding order number."""
    print('What would you like to do?')
    for i, item in enumerate(actions, 1):
        print("{}) {}".format(i, item))
    choice_actions = input('Pick your selection by their corresponding number: ')
    while True:
        if not choice_actions.isnumeric() or not '1' <= choice_actions < str(len(actions)):
            choice_actions = input('Pick your selection by their corresponding number: ')
        else:
            break
    choice_actions_int = int(choice_actions)
    return choice_actions_int


def sending_thank_you():
    """Lists all the donors or prompts for a name and donation amount to compile the thank you email."""
    send_to_name = input("Who do you want to send the email to? Type 'list' for a list of all the donors. ")
    if send_to_name == 'list':
        display_donor_dictionary(table_dictionary)
        send_to_name = input("Who do you want to send the email to? Type 'list' for a list of all the donors. ")
    if send_to_name not in table_dictionary:
        table_dictionary[send_to_name] = []
    donation_amount = float(input("What donation amount do you want to thank them for? "))
    while True:
        if type(donation_amount) is not float:
            donation_amount = float(input('What donation amount do you want to thank them for? '))
        else:
            break
    table_dictionary[send_to_name].append(donation_amount)
    print("Dear {}, Thank you for your generous contribution of ${:.2f} to our program.".format(send_to_name,
                                                                                                donation_amount))


def display_donor_dictionary(donor_dictionary):
    """Prints the full list of donors and corresponding donation history."""
    for key, item in donor_dictionary.items():
        print("{:<20}: {}".format(key, item))


def print_report():
    """Prints the donor table in equally amount of column width with each donor, total amount, number of gifts and average donation."""
    table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    len_header = len(table_header)
    print("|".join(["{:<20}"] * len_header).format(*table_header))
    print("-" * (20 * len_header + (len_header - 1)))
    new_list = []
    for k, v in table_dictionary.items():
        sum_donations = sum(v)
        total_gifts = len(v)
        average_gift = sum_donations / total_gifts
        new_list.append([k, sum_donations, total_gifts, average_gift])
    sorted_new_list = sorted(new_list, key=itemgetter(1), reverse=True)
    for row in sorted_new_list:
        print("{0:<20} ${1:>19.2f} {2:>20} ${3:>19.2f}".format(*row))


if __name__ == '__main__':
    actions_list = ['Send a Thank You', 'Create a Report', 'quit']
    action = select_action(actions_list)
    while True:
        if action == 1:
            sending_thank_you()
        elif action == 2:
            print_report()
        elif action == 3:
            exit()
        else:
            continue
        next_task = input("Chose another action from the list: ")
        action = int(next_task)
