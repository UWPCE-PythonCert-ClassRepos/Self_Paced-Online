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
        for i in choices:
            print(i, choices[i]['option'])
        response = prompt_user("Type a menu selection number: ").strip()

        try:  # Get the selection number and call helper function
            choices[response]['function']()
        except KeyError:
            print("\nInvalid response - try again.")
        else:
            if response == '4':  # Exit if "Quit" is chosen
                return

def prompt_user(str):
    """
    Prompt the user for input.

    When you perform unit tests, reassign the function name to another
    function that provides automated input.

    :str:  The string prompt to the user.

    :return:  The user's response.
    """
    result = input(str)
    return result

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
    # Get the donor name, show all donors, or quit
    response = prompt_user(
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()

    alt_choices = {  # Dict of functions to show donor list or to quit
            '': exit_screen,
            'quit': exit_screen,
            'list': print_donor_list
    }
    try:  # Respond to the quit or list option
        alt_choices[response.lower()]()
    except KeyError:  # Key exception means a donor name was specified
        get_donation_amount(response)
    else:
        if response.lower() == 'list':
            send_thank_you()  # Still want to get a donor to thank

def get_donation_amount(donor):
    """
    Ask user for a donation amount and add for the specified user.

    :donor:  The donor name for which to add a donation amount.

    :return:  The donation amount, or `None` if not specified.
    """
    donation = prompt_user(
            f"Type amount donated by '{donor}' (or type 'quit'): "
            ).strip().lower()
    if donation in ('', 'quit'):
        exit_screen()
        return None

    try:  # Add donation to master donor history + print letter
        donation = float(donation)
    except ValueError:
        print('\nNot a valid number.\n')
    else:
        if donation > 0.0:
            donor_history.setdefault(donor, [])
            donor_history[donor].append(donation)
            text = create_form_letter(donor, donation)
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
              that donor.
    """
    d = donor_history[donor]
    donations = sum(d)
    gifts = len(d)
    average = 1.0 * donations / gifts
    return {'name': donor, 'donations': donations,
            'gifts': gifts, 'average': average}

def send_all_letters():
    """
    Save all donor thank-you letters to disk.

    :return:  None.
    """
    # Ask for the directory to save the letters to
    cur_dir = os.getcwd()
    print('\nThe current directory is %s' % cur_dir)
    new_dir = prompt_user(
            '\nType the directory to save the letters in: ').strip()
    try:
        os.mkdir(new_dir)
    except FileNotFoundError:
        print(f'\nCannot find or create directory "{new_dir}".')
        print('Will use the current directory instead.\n')
        new_dir = cur_dir
    except FileExistsError:
        print(f'\nFound directory "{new_dir}".\n')
    finally:  # Save each letter, with the donor name in each file name
        os.chdir(new_dir)
        new_dir = os.getcwd()
        print(f'Saving to directory {new_dir}')

        # Create dict of letter names and letter texts, then write files
        letters = {f'_{k}.txt': create_form_letter(k, v[-1])
                  for k, v in donor_history.items()}
        for letter in letters:
            with open(letter, 'w') as f:
                for line in letters[letter]:
                    f.write(line)

        # Print names of saved letters and return to original directory
        print('The following new letters have been saved in '
                f'{new_dir}:\n\t{tuple(letters.keys())}')
        os.chdir(cur_dir)

def create_form_letter(donor_name, donor_amount):
    """
    Create the form letter using the donor name and amount.

    :donor_name:  The name of the donor.

    :donor_amount:  The amount given by the donor this time.

    :return:  A string containing the filled-in form letter.
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
    
    # If a donor has given before, add a parenthetical clause stating the
    # total donation amount and the number of donations
    str2 = ''
    gifts = len(donor_history[donor_name])
    if gifts > 1:
        str2 = '(and total donations of ' \
                '${0:,.2f} from {1:,d} gifts)\n            '.format(
                sum(donor_history[donor_name]), gifts)
    
    return str.format(donor_name, donor_amount, str2)

if __name__ == "__main__":
    manage_donors()
