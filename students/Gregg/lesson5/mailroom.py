#!/usr/bin/env python3
"""Use current knowledge to set up an interactive program"""

import datetime
from collections import defaultdict

donations = {
    "William Gates, III": [3, 5, 7],
    "Mark Zuckerberg": [4.50, 8, 2],
    "Jeff Bezos": [7.77],
    "Paul Allen": [3.6, 4.5],
    "bob": [.01]
}
donations = defaultdict(list, donations)
# todo
# add file writing


def menu(prompt, menu_dict, quit_string='q'):
    """Continues prompting with prompt until the quit_string is returned

    Prompt handler is set up to return values based on the functions in
    action_list, so one of these functions should return the quit_string
    otherwise there is no way to quit
    """
    def menu_function(key_in):
        menu_handler(key_in, menu_dict)

    while(True):
        result = quitable_function_prompt(prompt, menu_function, quit_string)
        if result is not None:
            break


def menu_handler(key_in, menu_dict):
    """use a switch dict to choose route the program based on input

    includes nice handling of invlaid options
    """
    try:
        selected_action = menu_dict[key_in]
    except KeyError as E:
        print("That isn't one of the menu options")
        raise(E)
    else:
        selected_action()


def quitable_function_prompt(prompt, function_in, quit_string='q'):
    """Runs function with user input unless input is quit string

    Will repeat if the input is invalid
    """
    result = input(prompt_formatter(prompt))
    if result == quit_string:
        return result
    try:
        function_in(result)
    except (KeyError, ValueError) as E:
        # I feel like maybe these should be custom errors?
        # made dbugging a bit of a pain
        print('Unable to continue, please try again')
        quitable_function_prompt(prompt, function_in)


prompt_formatter = '{}\nInput: '.format


def primary_menu():
    """Guide user through the mailroom UI"""
    menu(primary_prompt, primary_switch_dict, quit_string='Q')


primary_prompt = (
    "\nWould you like to Send a Thank You (enter TY), "
    "Create a Report (enter CR), send thank you letters to everyon (enter SL) "
    "or quit (enter Q).\n"
    "At any point enter q to return to this prompt"
)


def prompt_thank_you():
    """Guide user to create a thank you for a new donation"""
    quitable_function_prompt(thank_you_prompt, thank_you)


thank_you_prompt = (
    "Enter a full name to send them a thank you\n"
    "Enter 'list' to see current donors"
)


def thank_you(donor):
    """Prompt the necessary actions to send thankyou to donor"""
    print(donor)
    if donor == 'list':
        list_donors()
        prompt_thank_you()
    else:
        add_donation_prompt = f"How much did {donor} donate today?"

        def add_donation_for_donor(donation_amount):
            new_donation_handler(donation_amount, donor)
        quitable_function_prompt(add_donation_prompt, add_donation_for_donor)


def list_donors():
    """print all the donors currently as keys of donations dictionary"""
    print_list(donors(donations), 'donors')


def print_list(list_in, descriptor_str):
    """prints the elements of the list with some nice UI text"""
    # makes it more flexible so I could print other lists if I wanted to
    # such as the donations for a given donor
    print("These are the {} currently in the database:".format(descriptor_str))
    for thing in list_in:
        print(thing)
    print('')


def donors(donations):
    """Retunr the donors in the database"""
    # putting this in in case the data strict changes
    return list(donations.keys())


def new_donation_handler(donation_amount, donor):
    """add a donation to the list for given donor in donations dict"""
    try:
        add_donation_to_database(donor, donation_amount)
    except ValueError as E:
        print(f'{donation_amount} is not a number, please enter a number')
        raise(E)
    this_thx_string = thankyou_string(donor, float(donation_amount))
    send_thank_you(donor, this_thx_string)


def add_donation_to_database(donor, donation_amount):
    """Add a dontation to to the database for donor"""
    donations_from(donor).append(float(donation_amount))


line1 = 'Dear {},\n\n'
line2 = '\tThank you for you generous donation of ${:.2f}.\n\n'
line3 = '\tIt will be put to good use.\n\n'
line4 = 'Sincerely,\n'
line5 = '-The team'


thankyou_string = (
    '{}{}{}{:>40}{:>45}'.format(line1, line2, line3, line4, line5).format
)


def send_thank_you(donor, this_thx_string):
    """send the thank you to the donor"""
    # leaving this as a sperate function because at some point I expect
    # to actually do things other than printing here
    print(f"Heres the thank you that should be sent to {donor}:")
    print(this_thx_string)
    print('')


def create_donation_report(donors):
    """Create a report of summarry statistics for the current database

    The columns are name, total, number and average
    """
    row_list = []
    headers = 'Donor name', 'Total Given', 'Num Gifts', 'Average Gift'
    format_column_header = "{:<26}|{:^13}|{:^13}|{:^13}".format
    row_list.append(format_column_header(*headers))
    row_list.append('_' * 68)

    donor_rows_list = [get_row(donor) for donor in donors]
    donor_rows_list.sort(key=key1, reverse=True)

    format_row = "{:<27}${:>12.2f} {:>12}  ${:>12.2f}".format
    row_list.extend([
        format_row(*row)
        for row in donor_rows_list
    ])
    report_string = ('\n').join(row_list)
    return report_string


def print_report():
    """Print report to prompt"""
    print(create_donation_report(donations))


def key1(iterable):
    """Sort key for creating report"""
    return iterable[1]


def get_row(donor):
    """retrieve the statistics for a given donor"""
    donors_donations = donations_from(donor)
    total = sum(donors_donations)
    num = len(donors_donations)
    try:
        avg = total / num
    except ZeroDivisionError as E:
        avg = 0
    return donor, total, num, avg


def donations_from(donor):
    """Return a list of all amounts made by donor ordered chronologically"""
    # Including this in anticipation that the data struct might change
    return donations[donor]


def send_letters():
    """Send letters to the donors in the DB that have made donations"""
    for donor in donations:
        send_letter(donor)


def send_letter(donor):
    """Send a thank you letter to a donor for the most recent donation"""
    last_don = last_donation(donor)
    now = datetime.datetime.now().strftime("%m.%d.%Y.%H.%M.%S")
    letter_filename = "{}_{}.txt".format(donor, now)
    try:
        donor_thx_string = thankyou_string(donor, last_don)
    except TypeError as E:
        print((
            "{1} is in our database but has not made a donation.\n"
            "No thank you was saved for {1}"
        ).format(donor)
        )
    else:
        with open(letter_filename, 'w') as letter:
            letter.write(donor_thx_string)
        print(f'Sent letter to {donor}')


def last_donation(donor):
    """Return the value of the last donation made by donor"""
    try:
        last_donation = donations_from(donor)[-1]
    except IndexError as E:
        last_donation = None
    return last_donation


primary_switch_dict = {
    'TY': prompt_thank_you,
    'CR': print_report,
    'SL': send_letters
}


def tests():
    """Test the functions"""
    pass


if __name__ == "__main__":
    tests()
    print("Welcome to Gregg's Mailroom 1.1\n")
    primary_menu()
