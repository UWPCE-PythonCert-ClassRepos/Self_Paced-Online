#!/usr/bin/env python3
"""Use current knowledge to set up an interactive program"""

donations = {
    "William Gates, III": [3, 5, 7],
    "Mark Zuckerberg": [4.50, 8, 2],
    "Jeff Bezos": [7.77],
    "Paul Allen": [3.6, 4.5],
    "bob": [.01]
}
return_to_primary_prompt = [False]

# This doesn't seem like the cleanest way to do this, but I coultn't
# come up with anything better without turning it into a full blow stat machine
# that has a centralized handler thingy for every possible transition
# That can then return to the start state if necessary
# It seems like it works ok for this limited example


def quitable_input(text_prompt):
    text_in = input(f"{text_prompt}\nInput: ")
    if text_in == 'q':
        return_to_primary_prompt[0] = True
        return False
    else:
        return text_in


def primary_prompt():
    """Text cue to help user select an action"""
    prompt_string = (
        "\nWould you like to Send a Thank You (enter TY), "
        "Create a Report (enter CR) or quit (enter Q).\n"
        "At any point enter q to return to this prompt\n"
        "Input: "
    )
    return prompt_string


def thank_you_prompt():
    """Text cue to help user send a thankyou"""
    prompt_string = (
        "Enter a full name to send them a thank you\n"
        "Enter 'list' to see current donors"
    )
    return prompt_string


def donation_amount_prompt():
    """Text cue to help user enter a donation amount"""
    prompt_string = "How much did this person donate?"
    return prompt_string


def handle_primary_prompt(action):
    """Handle the possible user responses to the primary prompt"""
    map_inputs = {
        "TY": handle_thankyou_prompt,
        "CR": create_donation_report
    }
    action_handled = False
    try:
        action_handled = map_inputs[action]()
    except KeyError as E:
        print(f"{action} That isn't a valid input")
    return action_handled


def handle_thankyou_prompt():
    """Handle the possible user responses to the thankyou prompt"""
    text_in = quitable_input(thank_you_prompt())
    if return_to_primary_prompt[0]:
        return False
    else:
        map_inputs = {
            "list": list_donors,
        }
        action_handled = False
        try:
            action_handled = map_inputs[text_in]()
            handle_thankyou_prompt()
        except KeyError as E:
            action_handled = thank_you(text_in)
        return action_handled


def new_donor(donor):
    """add a new donor to the donations dictionary"""
    print("That donor isn't in our database yet, lets add them.")
    donations[donor] = []
    return True


def list_donors():
    """print all the donors currently as keys of donations dictionary"""
    print("These are the donors currently in the database:")
    for donor in donations:
        print(donor)
    print('')
    return True


def add_donation(donor):
    """add a donation to the list for given donor in donations dict"""
    donation = quitable_input(f"How much did {donor} donate today?")
    if return_to_primary_prompt[0]:
        return False
    try:
        donations[donor].append(float(donation))
    except ValueError as E:
        print(f'{donation} is not a number, please enter a number')
        donation = add_donation(donor)
    return donation


def format_thankyou(donor, donation):
    """create the text string thanking a donor for their dontion"""
    thankyou_string = (
        f'Thank you, {donor}, for you generous ${donation} donation.'
    )
    return thankyou_string


def send_thank_you(donor, thankyou_string):
    """send the thank you to the donor"""
    print(f"Heres the thank you that should be sent to {donor}:")
    print(thankyou_string)
    print('')
    return True


def thank_you(donor):
    """Prompt the necessary actions to send thankyou to donor"""
    if return_to_primary_prompt[0]:
        return False
    if not(donor in donations):
        new_donor(donor)
    donation = add_donation(donor)
    if return_to_primary_prompt[0]:
        return False
    thankyou_string = format_thankyou(donor, donation)
    sent = send_thank_you(donor, thankyou_string)
    return sent


def create_donation_report():
    """Create a report of summarry statistics for the current database

    The columns are name, total, number and average
    """
    row_list = []
    row_list.append(format_column_header())
    row_list.append('_' * 68)
    for donor in donations:
        donor_stats = get_row(donor)
        row_list.append(format_row(donor_stats))
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
    total = total_given(donor)
    num = num_donations(donor)
    avg = average_given(donor)
    return name, total, num, avg


def format_row(row_tupl):
    """format a donors statistics so the columns will match"""
    return "{:<27}${:>12.2f} {:>12}  ${:>12.2f}".format(*row_tupl)


def list_donations(donor):
    """Return a list of all amounts made by donor ordered chronologically"""
    # Including this in anticipation that the dta struct might become more complicated
    return donations[donor]


def total_given(donor):
    """Return the total amount donated by donor"""
    return sum(list_donations(donor))


def average_given(donor):
    """Return the average amount donated by donor"""
    return sum(list_donations(donor))/len(list_donations(donor))


def num_donations(donor):
    """Return the total number of donations donated by donor"""
    return len(list_donations(donor))



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
    print("Welcome to Gregg's Mailroom")
    return_to_primary_prompt = [False]
    while(True):
        return_to_primary_prompt[0] = False
        action = input(primary_prompt())
        if action == "Q":
            break
        else:
            handled = handle_primary_prompt(action)
