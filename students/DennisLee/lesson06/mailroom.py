#!/usr/bin/env python3

import os

# Initial donor list and the amounts they have donated
donor_history = {
            'Red Herring': [65820.5, 31126.37, 15000],
            'Papa Smurf': [210.64, 1000],
            'Pat Panda': [55324.4],
            'Karl-Heinz Berthold': [3545.2, 10579.31],
            'Mama Murphy': [156316.99, 8500.3, 12054.33],
            'Daphne Dastardly': [82]
        }

def manage_donors():
    """
    Display the menu of choices for donor management.

    :return:  None.
    """
    # create a dictionary of menu items, menu text, and menu caller functions
    choices = {
    '1': {'option': 'Send a thank you', 'function': send_thank_you},
    '2': {'option': 'Create a report', 'function': create_a_report},
    '3': {'option': 'Send letters to everyone', 'function': send_all_letters},
    '4': {'option': 'Quit', 'function': exit_screen}
    }
    
    while True:  # Print the menu list (with numbered choices)
        print("\nMENU:")
        for k, v in choices.items():
            print(k, v['option'])
        response = input("Type a menu selection number: ").strip()
        call_menu_function(choices, response, respond_to_bad_main_menu_choice)
        if response == '4':  # Exit if "Quit" is chosen
            return

def call_menu_function(choice_dict, choice, unfound_key_handler, **kwargs):
    """
    Call a menu function with a dict.

    :choice_dict:  Dict containing the `choice` string, with the dict
                   value being a another dict that contains a 'function'
                   key whose value is the function to call for `choice`.

    :choice:  A string that may or may not be a key in the choice_dict
              dictionary.

    :unfound_key_handler:  The function to call if the specified choice
                           is not a key in the dictionary.

    :kwargs:  Additional keyword arguments to pass to the unfound key
              handler.

    :return:  `True` if a menu function was successfully called;
              `False` otherwise (which also can be the desired result).
    """
    try:  # Get the selection number and call helper function
        choice_dict[choice]['function']()
    except KeyError:
        unfound_key_handler(choice, **kwargs)
        return False
    else:
        return True

def respond_to_bad_main_menu_choice(choice):
    """
    Show error message if the user's main menu choice is invalid.
    
    :choice:  The menu choice string as entered by the user.

    :return:  None.
    """
    print(f"\n'{choice}' is in invalid response.")

def exit_screen():
    """
    Simply print an exit message.

    :return:  None.
    """
    print("\nExiting.\n")
    return

def send_thank_you():
    """
    Add new donations for new or existing donors, and send a thank-you
    letter.

    :return:  None.
    """
    alt_choices = {  # Dict of functions to show donor list or to quit
            '': {'function': exit_screen},
            'quit': {'function': exit_screen},
            'list': {'function': print_donor_list}
    }
    response = input(  # Get the donor name, show all donors, or quit
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()

    call_menu_function(alt_choices, response, get_donation_amount)
    if response == 'list':
        send_thank_you()  # Still want to get a donor to thank

def get_donation_amount(donor):
    """
    Ask user for a donation amount from the specified donor.

    :donor:  The donor name for which to add a donation amount.

    :return:  The donation amount, or `None` if not specified.
    """
    donation_choices = {  # Dict of functions if user wants to quit
            '': {'function': exit_screen},
            'quit': {'function': exit_screen}
    }
    donation = input(
            f"Type amount donated by '{donor}' (or type 'quit'): "
            ).strip().lower()
    # if donation in ('', 'quit'):
    #     exit_screen()
    #     return None
    call_menu_function(donation_choices, donation, add_donation,
            donor_name=donor)

def add_donation(donation, donor_name):
    """
    Add the donation and donor (if new) to the donor history dict.

    :donation:  The amount to be donated.

    :donor_name:  The name of the person making the donation.

    :return:  The donation amount, or `None` if not specified.
    """
    try:  # Add donation to master donor history + print letter
        donation = float(donation)
    except ValueError:
        print('\nNot a valid number.\n')
    else:
        if donation > 0.0:
            donor_history.setdefault(donor_name, [])
            donor_history[donor_name].append(donation)
            text = create_form_letter(donor_name, donation)
            print(text)
            return donation
        else:
            print(
            '\nNegative/zero donation amounts not permitted.')

def print_donor_list():
    """
    Print the full list of donors.

    :return:  None.
    """
    print("\nLIST OF DONORS:")
    for donor in donor_history:
        print(donor)

def create_a_report():
    """
    Print out statistics for the entire donor list.

    :return:  None.
    """
    print('\n')
    print('{:<25s} |  {:>18s} | {:>15s} |  {:>18s}'.format(
        'Donor name', 'Total given', 'Number of gifts', 'Average gift'))
    print('-'*25 + '-|--' + '-'*18 + '-|-' + '-'*15 + '-|--' + '-'*18)

    for i in donor_history:
        stats = calc_donor_stats(i)
        print('{name:<25s} | ${donations:>18,.2f} | {gifts:>15d} | '
                '${average:>18,.2f}'.format(**stats))

def calc_donor_stats(donor):
    """
    Calculate the donation history for a particular donor.

    :donor:  The name of the donor.

    :return:  A dictionary that contains the name, cumulative donation
              amount, number of donations, and average donation from
              that donor. If the donor does not exist, `None` is
              returned.
    """
    try:
        d = donor_history[donor]
    except KeyError:
        print(f"\nThere is no donor '{donor}' in the donor history.\n")
    else:
        donations = round(sum(d), 2)
        gifts = len(d)
        average = round(1.0 * donations / gifts, 2)
        return {'name': donor, 'donations': donations,
                'gifts': gifts, 'average': average}

def send_all_letters():
    """
    Create all of the donor thank-you letters.

    :return:  The folder containing the thank-you letters.
    """
    # Ask for the directory to save the letters to
    print('\nThe current directory is %s' % os.getcwd())
    new_dir = input('\nType the directory to save the letters in'
                    ' (invalid entry defaults to the current directory): '
                    ).strip()
    return save_letters(new_dir)

def save_letters(folder):
    """
    Save the donor thank-you letters to disk.

    :folder:  The folder in which to save the files.

    :return:  The folder containing the thank-you letters.
    """
    cur_dir = os.getcwd()
    try:
        os.mkdir(folder)
    except FileNotFoundError:
        print(f'\nCannot find or create directory "{folder}".')
        print('Will use the current directory instead.\n')
        folder = cur_dir
    except FileExistsError:
        print(f'\nFound directory "{folder}".\n')
    finally:  # Save each letter, with the donor name in each file name
        os.chdir(folder)
        folder = os.getcwd()  # Set folder name to the full OS path
        print(f'Saving to directory {folder}')

        # Create dict of letter names and letter texts, then write files
        letters = {f'_{k}.txt': create_form_letter(k, v[-1])
                  for k, v in donor_history.items()}
        for filename, text in letters.items():
            lines = text.splitlines()
            with open(filename, 'w') as f:
                for line in lines:
                    f.write(line + '\n')

        # Print names of saved letters and return to original directory
        print('The following new letters have been saved in '
                f'{folder}:\n\t{tuple(letters.keys())}')
        os.chdir(cur_dir)
        return folder

def create_form_letter(donor_name, donor_amount):
    """
    Create the form letter using the donor name and amount.

    :donor_name:  The name of the donor.

    :donor_amount:  The amount given by the donor this time.

    :return:  A string containing the filled-in form letter. If the
              donor name is not in the donor history or an invalid or
              nonpositive donor amount is specified, `None` is returned
              instead.
    """
    str = """\n\n\n
            From:     Random Worthy Cause Foundation
            To:       {0:s}
            Subject:  Your generous donation

            Dear {0:s},

            We want to express our gratitude for your donation of ${1:,.2f}
            {2:s}to the Random Worthy Cause Foundation.  To show our
            appreciation, we have enclosed a set of address labels
            and a custom tote bag that lets people know that you are a
            generous supporter of our cause.
            
            Thank you again, and please think of us the next time you want
            to give to a worthy cause.

            Sincerely,



            Mister E. Partner
            Random Worthy Cause Foundation
            """
    try:
        d = donor_history[donor_name]
    except KeyError:
        print(f"\nThere is no donor '{donor_name}' in the donor history.\n")
    else:
        try:
            amt = round(donor_amount, 2)
        except TypeError:
            print(f"\nAmount '{donor_amount} is not a number.'\n")
        else:
            if amt <= 0.0:
                print(f"\n{donor_amount} is not a valid donation amount.\n")
            elif amt not in d:
                print(f"\n{donor_amount} is not in the donation history of "
                        f"{donor_name}.\n")
            else:
                # If a donor has given before, add a parenthetical clause 
                # stating the total donation amount and number of donations
                str2 = ''
                gifts = len(d)
                if gifts > 1:
                    str2 = '(and total donations of ${0:,.2f} ' \
                            'from {1:,d} gifts)\n            '.format(
                            sum(d), gifts)
                
                return str.format(donor_name, amt, str2)

if __name__ == "__main__":
    manage_donors()
