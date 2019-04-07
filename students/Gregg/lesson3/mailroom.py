#!/usr/bin/env python3
"""Use current knowledge to set up an interactive program"""

#Todo - restructure so there is only one message handler, with dict mapping prompt, input options, functions and next states
#Todo - input a dictionary to the letter writing function
# this is a pain because I need to make the dictionary just to take it apart...it
#Todo add option to save all leters
#need additional save function


donors = [
    "William Gates, III",
    "Mark Zuckerberg",
    "Jeff Bezos",
    "Paul Allen",
    "bob"
]

donations = [
    [3, 5, 7],
    [4.50, 8, 2],
    [7.77],
    [3.6, 4.5],
    [40]
]


def recurring_prompt(quit_string, prompt, default_action, input_tup=(), action_tup=(), pass_text=False, pass_args = None):
    """Continues prompting with prompt until the quit_string is returned

    Prompt handler is set up to return values based on the functions in
    action_list, so one of these functions should return the quit_string
    otherwise there is no way to quit
    """
    while(True):
        result = prompt_handler(prompt, default_action, input_tup, action_tup, pass_text, pass_args)
        if result == quit_string:
            break


def prompt_handler(prompt, default_action, input_tup=(), action_tup=(), pass_text=False, pass_args = None):
    """Prompts the user, then runs function/action based on input

    Will quit all nested "handled prompts" with "q" using quitable input
    """
    text_in = quitable_input(prompt)
    if text_in is None:
        return "Return to main menu"
    else:
        if text_in in input_tup:
            input_idx = input_tup.index(text_in)
            next_action = action_tup[input_idx]
        else:
            next_action = default_action
        if (pass_args is None) and not(pass_text):
            result = next_action()
        else:
            arg_list = []
            if pass_text:
                arg_list.append(text_in)
            if pass_args:
                arg_list+=list(pass_args)
            arg_tuple = tuple(arg_list)
            result = next_action(*arg_tuple)
        return result


def quitable_input(text_prompt):
    """Used in prompt handler so that input of q will return to main menu"""
    text_in = input(f'{text_prompt}\nInput: ')
    if text_in == 'q':
        return None
        # I think none will work better than False
        # Then I can check is None, which will fail even for an empty string
    else:
        return text_in


def print_list(list_in, descriptor_str):
    """prints the elements of the list with some nice UI text"""
    # makes it more flexible so I could print other lists if I wanted to
    # such as the donations for a given donor
    print("These are the {} currently in the database:".format(descriptor_str))
    printed_things = False
    for thing in list_in:
        printed_things = True
        print(thing)
    print('')
    return printed_things


def list_donors(text_in):
    """print all the donors currently as keys of donations dictionary"""
    print_list(donors, 'donors')
    result = thank_you_menu()
    return result


def thank_you(donor):
    """Prompt the necessary actions to send thankyou to donor"""
    if not(donor in donors):
        new_donor(donor, donors, donations)
    add_donation_prompt = f"How much did {donor} donate today?"
    donor_idx = donors.index(donor)
    result = add_donation_handler(add_donation_prompt, donor_idx)
    return result


def new_donor(donor, donors, donations):
    """add a new donor to the donations dictionary"""
    print("That donor isn't in our database yet, lets add them.")
    donors.append(donor)
    donations.append([])


thankyou_string = 'Thank you, {}, for you generous ${} donation.'.format


def add_donation_handler(add_donation_prompt, donor_idx):
    result = prompt_handler(add_donation_prompt, add_donation, pass_text = True, pass_args = (add_donation_prompt, donor_idx))
    return result


def add_donation(donation, add_donation_prompt, donor_idx):
    """add a donation to the list for given donor in donations dict"""
    try:
        donations[donor_idx].append(float(donation))
    except ValueError as E:
        print(f'{donation} is not a number, please enter a number')
        result = add_donation_handler(add_donation_prompt, donor_idx)
        return result
    this_thx_string = thankyou_string(donors[donor_idx], donation)
    sent = send_thank_you(donor_idx, this_thx_string)
    return sent


def send_thank_you(donor_idx, this_thx_string):
    """send the thank you to the donor"""
    # leaving this as a sperate function because at some point I expect
    # to actually do things other than printing here
    print(f"Heres the thank you that should be sent to {donors[donor_idx]}:")
    print(this_thx_string)
    print('')
    return True


def create_donation_report():
    """Create a report of summarry statistics for the current database

    The columns are name, total, number and average
    """
    row_list = []
    row_list.append(format_column_header())
    row_list.append('_' * 68)
    donor_rows_list = []
    hisorical_donation_amount_list = []
    for donor in donors:
        donor_stats = get_row(donor)
        hisorical_donation_amount_list.append(donor_stats[1])
        donor_rows_list.append(format_row(donor_stats))
    hisorical_donation_amount_list, donor_rows_list = zip(*sorted(zip(hisorical_donation_amount_list, donor_rows_list), reverse=True))
    #donor_rows_list.sort(hisorical_donation_amount_list)
    row_list += donor_rows_list
    report_string = ('\n').join(row_list)
    print(report_string)
    return report_string


def format_column_header():
    """format the column headers"""
    headers = 'Donor name', 'Total Given', 'Num Gifts', 'Average Gift'
    return "{:<26}|{:^13}|{:^13}|{:^13}".format(*headers)


def get_row(donor):
    """retrieve the statistics for a given donor"""
    name = donor
    donor_idx = donors.index(donor)
    total = total_given(donor_idx)
    num = num_donations(donor_idx)
    avg = average_given(donor_idx)
    return name, total, num, avg


def format_row(row_tupl):
    """format a donors statistics so the columns will match"""
    return "{:<27}${:>12.2f} {:>12}  ${:>12.2f}".format(*row_tupl)


def list_donations(donor_idx):
    """Return a list of all amounts made by donor ordered chronologically"""
    # Including this in anticipation that the dta struct might become more complicated
    return donations[donor_idx]


def total_given(donor_idx):
    """Return the total amount donated by donor"""
    return sum(list_donations(donor_idx))


def average_given(donor_idx):
    """Return the average amount donated by donor"""
    try:
        avg = sum(list_donations(donor_idx)) / len(list_donations(donor_idx))
    except ZeroDivisionError as E:
        avg = 0
    return avg

def num_donations(donor_idx):
    """Return the total number of donations donated by donor"""
    return len(list_donations(donor_idx))


thank_you_prompt = (
    "Enter a full name to send them a thank you\n"
    "Enter 'list' to see current donors"
)
thankyou_input_list = ['list']
thankyou_action_list = [list_donors]
thank_you_default = thank_you


def thank_you_menu():
    prompt_handler(thank_you_prompt, thank_you_default, thankyou_input_list, thankyou_action_list, pass_text=True)

def quit_mailbox():
    """When the user cues, quit the loop entirely"""
    return "quit_mailroom"

def invalid_input():
    print("That isn't a valid input.")

primary_prompt = (
    "\nWould you like to Send a Thank You (enter TY), "
    "Create a Report (enter CR) or quit (enter Q).\n"
    "At any point enter q to return to this prompt"
)
primary_input_list = ['TY', 'CR', 'Q']
primary_action_list = [thank_you_menu, create_donation_report, quit_mailbox]
primary_default = invalid_input


def primary_menu():
    recurring_prompt('quit_mailroom', primary_prompt, primary_default, primary_input_list, primary_action_list, )


def tests():
    """Test the functions"""
    try:
        # Not sure how to test send thankyou functionailty
        # Not sure how to mock inputs, not worth it too look up on my own right now
        # Seems like we should have a mock dictionary that we can add something to
        pass
    except Exception as E:
        print('The following tests failed:')
        print("Gregg's Mailroom appears to be broken. Please contact him")
        form_string = (
            "To proceed with limited functionality and potential "
            "unexpected behavior enter Y"
        )
        proceed = input(form_string)
        if not(proceed == "Y"):
            raise(E)


if __name__ == "__main__":
    tests()
    print("Welcome to Gregg's Mailroom 1.1\n")
    primary_menu()
