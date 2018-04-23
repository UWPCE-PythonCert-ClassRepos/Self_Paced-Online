#!/usr/bin/env python3

# Lesson 06: Mailroom: Part 4, With Unit Testing
# Natalie Rodriguez
# April 22, 2018

import os


# Initial donor list and the amounts they have donated
donors = {'Luke Rodriguez':[12.75, 50.31, 42.59],'Emma Burgess':[390.87, 30.00],'Greg Cayetano':[875.60, 1120.00],
'Hannah Watson':[20.58, 1120.14],'Emily Connor':[10.00],'Catherine Davis':[400.00],
'River Tails':[63.56, 1200.00, 300.65],'Virginia Ferdinand':[350.35, 5000.00],'Joseph Kibson':[3498.00, 5.50]}


def donor_dashboard():
    # dict of menu options
    options = {'1': ("Send a thank you note.", thank_you),
               '2': ("Create a report.", create_report),
               '3': ("Send thank yous to all donors.", thank_all),
               '4': ("Exit the donor dashboard.", exit)}

    response = ''
    while response != '4':
        print()
        for i in options:
            print(i, options[i][0])

        # Get user's selection
        response = ''
        while not response in options:
            response = input("Type your selection: ").strip()

        options[response][1]()  # Call helper function


def exit_dash():

    print("\nExiting the donor dashboard. Goodbye! \n")
    return


def thank_you():
    """
    Add new donations for new or existing donors, and send a thank-you
    letter.
    :return:  None.
    """
    # Get the donor name, show all donors, or quit
    response = input(
        "\nType the full donor name (Enter 'list' to show all donors or enter 'exit'): "
    ).strip()

    if response.lower() in ('', 'exit'):
        exit_dash()
        return

    elif response.lower() == 'list':
        print("\nDONORS:")
        for donor in donors:
            print(donor)
        thank_you()

    else:
        while True:
            donation = input(
                f"Enter amount of donation by '{response}' (or enter 'exit'): "
            ).strip().lower()
            if donation == 'exit':
                exit_dash()
                return

            elif donation.strip('0123456789.') == '' and len(
                    donation) > 0 and donation.count('.') <= 1 and float(
                donation) > 0.0:
                break

        donation = float(donation)
        donors.setdefault(response, [])
        donors[response].append(donation)
        print(create_form_letter(response, donation))


def create_report():

    print('\n')
    print('        Donor Name        |    Total Given      | '
          + 'Number of Gifts |    Average Gift    ')
    print('--------------------------|---------------------|-'
          + '----------------|--------------------')
    for individual_donor, donations in donors.items():
        total_donation = sum(donations)
        number_of_gifts = len(donations)
        average_donation = 1.0 * total_donation / number_of_gifts
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
            individual_donor, total_donation,
            number_of_gifts, average_donation))


def thank_all():

    cur_dir = os.getcwd()
    print('\nThe current directory is %s' % cur_dir)
    new_dir = input('\nEnter the directory you want to save to '
                    '(Press enter to save in the current location): ').strip()
#exception handling changes here: indented all for try/except block
    try:
        if new_dir != '':
            os.mkdir(new_dir)
            os.chdir(new_dir)
            new_dir = os.getcwd()
        else:
            new_dir = cur_dir

        for k, v in donors.items():
            letter = create_form_letter(k, v[-1])
            with open('{:s}.txt'.format(k), 'w') as f:
                for line in letter:
                    f.write(line)

        print('Your thank you notes have been saved in %s:' % new_dir)
        print(os.listdir())
        os.chdir(cur_dir)
    except FileNotFoundError:
        print('\n'"We cannot find that file location. Please enter another.")
    finally:
        thank_all()


def create_form_letter(donor_name, donor_amount):

    str = """\n\n\n
            Dear {0:s},
            We want to thank you for you generous donation of ${1:,.2f}{2:s}. 
            Your contribution to the purchase of land for conservation
            and habitat restoration will make a profound difference in allowing
            the environment to recover from the detrimental impact of human
            life. With noble individuals like yourself, we can make large strides
            to allow the North American continent to exist without the stressors of 
            agriculture and other human impacts. We appreciate and look forward to
            your continued support.

            Best,
            The Nature Conservancy            

            """

    str2 = ''
    gifts = len(donors[donor_name])
    if gifts > 1:
        str2 = '(and total donations of ' \
               '{0:,.2f} from {1:,d} gifts)\n            '.format(
            sum(donors[donor_name]), gifts)

    return str.format(donor_name, donor_amount, str2)


if __name__ == "__main__":
    print("Welcome to the Nature Conservancy Donor Dashboard")
    donor_dashboard()