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
    options = ("Send a thank you", "Create a report", 
               "Send letters to everyone", "Quit")
    funcs = (send_thank_you, create_a_report, send_all_letters, exit_screen)
    choices = {str(x):y for x, y in zip(range(1, 5),
            [(a, b) for a, b in zip(options, funcs)])}
    
    while True:
        # Print the menu list (with numbered choices)
        print("\nMENU:")
        [print(i, choices[i][0]) for i in choices]
        try:  # Get the selection number and call helper function
            response = input("Type a menu selection number: ").strip()
            choices[response][1]()
        except KeyError:
            print("\nInvalid response - try again.")
        else:
            if response == '4':
                return

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
    response = input(
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()

    if response.lower() in ('', 'quit'):
        exit_screen()
        return
    elif response.lower() == 'list':
        print_donor_list()
        send_thank_you()  # Try getting a donor name again
    else:
        while True:  # Get the donation amount
            donation = input(
                    f"Type amount donated by '{response}' (or type 'quit'): "
                    ).strip().lower()
            if donation == 'quit':
                exit_screen()
                return

            try:  # Add donation to master donor history + print letter
                donation = float(donation)
            except ValueError:
                print('\nNot a valid number - try again.\n')
            else:
                if donation > 0.0:
                    donor_history.setdefault(response, [])
                    donor_history[response].append(donation)
                    print(create_form_letter(response, donation))
                    return
                else:
                    print(
                    '\nNegative/zero donation amounts disallowed - try again.')

def print_donor_list():
    """
    Print the full list of donors.

    :return:  None.
    """
    print("\nLIST OF DONORS:")
    [print(donor) for donor in donor_history]

def create_a_report():
    """
    Print out statistics for the entire donor list.

    :return:  None.
    """
    print('\n')
    print('Donor name                |         Total given | '
            + 'Number of gifts |        Average gift')
    print('--------------------------|---------------------|-'
            + '----------------|--------------------')
    for individual_donor, donations in donor_history.items():
        total_donation = sum(donations)
        number_of_gifts = len(donations)
        average_donation = 1.0 * total_donation / number_of_gifts
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                individual_donor, total_donation,
                number_of_gifts, average_donation))

def send_all_letters():
    """
    Save all donor thank-you letters to disk.

    :return:  None.
    """
    # Ask for the directory to save the letters to
    cur_dir = os.getcwd()
    print('\nThe current directory is %s' % cur_dir)
    new_dir = input('\nType the directory to save the letters in: ').strip()
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
        for k, v in donor_history.items():
            letter = create_form_letter(k, v[-1])
            with open('_{:s}.txt'.format(k), 'w') as f:
                for line in letter:
                    f.write(line)
        
        # Print the names of the saved letters and return to the original directory
        print('New letters saved in %s:' % new_dir)
        print(os.listdir())
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
                '{0:,.2f} from {1:,d} gifts)\n            '.format(
                sum(donor_history[donor_name]), gifts)
    
    return str.format(donor_name, donor_amount, str2)

if __name__ == "__main__":
    manage_donors()
