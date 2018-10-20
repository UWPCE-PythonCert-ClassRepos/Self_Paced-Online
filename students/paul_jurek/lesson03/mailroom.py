"""runs the command line app for the mailroom as part of lesson 3"""

# setup initial donor list
donors = {'Bill Gates': [100000, 5, 3000000],
          'Paul Allen': [10, 1000000],
          'Warren Buffet': [300000000],
          }


def thank_you():
    """If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and
    re-prompt.  If the user types a name not in the list, add that name
    to the data structure and use it.  If the user types a name in the
    list, use it.  Once a name has been selected, prompt for a donation
    amount.  Turn the amount into a number – it is OK at this point for
    the program to crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history
    of the selected user.  Finally, use string formatting to compose an
    email thanking the donor for their generous donation. Print the email
    to the terminal and return to the original prompt.
    It is fine (for now) to forget new donors once the script quits running."""
    exit_ind = False
    while not exit_ind:
        thank_you_input = input('Please select name: ')

        if thank_you_input.lower().strip() == 'list':
            display_donors()
        elif thank_you_input.lower().strip() == 'quit':
            exit_ind = True
        else:
            if thank_you_input not in donors:
                create_donor(thank_you_input)
            donation_amount = float(input("Select donation amount: "))
            create_donation(fullname=thank_you_input, amount=donation_amount)
            send_thank_you(fullname=thank_you_input)
            exit_ind = True


def display_donors():
    """diplays donors"""
    [print(donor) for donor in donors.keys()]


def create_donation(fullname, amount):
    """adds a donation to the donors dict from user input"""
    donors[fullname].append(amount)


def create_donor(fullname):
    """adds new donor to donors"""
    donors[fullname] = []


def send_thank_you(fullname):
    """prints thank you message to terminal for donation"""
    print(f'Thank you {fullname} for your generous donation!')


def report():
    """handles process for main screens report selection

    If the user (you) selected “Create a Report”, print a list of your donors,
    sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and average
    donation amount as values in each row. You do not need to print out all
    their donations, just the summary info.
    Using string formatting, format the output rows as nicely as possible.
    The end result should be tabular (values in each column should align
    with those above and below)
    After printing this report, return to the original prompt.
    At any point, the user should be able to quit their current task and
    return to the original prompt.
    From the original prompt, the user should be able to quit the script
    cleanly.
    Your report should look something like this:
    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14
    """
    print(f"{'Donor Name':<26}|{'Total Given':^13}|{'Num Gifts':^11}|{'Average Gift':^13}")
    print('-'*66)
    # TODO: create helper function to summarize donations
    # TDOD: create helper function to build table below headers

if __name__ == '__main__':
    # initial placeholder for input
    user_input = None

    # run until user specifies to get out
    while user_input != 'quit':
        user_input = input('Options:\n'
                           '\tSend a Thank You\n'
                           '\tCreate a Report\n'
                           '\tquit\n'
                           'Please input option: ')

        # cleans up user input to make more robust.
        user_input = user_input.lower().strip()

        if user_input == 'send a thank you':
            thank_you()
        elif user_input == 'create a report':
            report()
