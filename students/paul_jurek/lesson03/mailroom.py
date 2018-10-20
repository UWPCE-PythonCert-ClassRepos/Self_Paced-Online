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
    while exit_ind == False:
        thank_you_input = input('Please select name: ')
        
        if thank_you_input == 'list':
            display_donors()
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

    # TODO: add functions for each option in top to be called
