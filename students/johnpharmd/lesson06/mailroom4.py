#!/usr/bin/env python3
import datetime
import mailroomtest
import sys

# Data
donors_amts = {'Gates': {'title': 'Mr.', 'donations': 150000,
                         'num_of_donations': 3},
               'Brin': {'title': 'Mr.', 'donations': 150000,
                        'num_of_donations': 3},
               'Cerf': {'title': 'Mr.', 'donations': 50000,
                        'num_of_donations': 2},
               'Musk': {'title': 'Mr.', 'donations': 100000,
                        'num_of_donations': 1},
               'Berners-Lee': {'title': 'Mr.', 'donations':
                               50000, 'num_of_donations': 2},
               'Wojcicki': {'title': 'Ms.', 'donations': 125000,
                            'num_of_donations': 1},
               'Avey': {'title': 'Ms.', 'donations': 200000,
                        'num_of_donations': 2}}


# Processing
def get_donor_list():
    donor_list = list(donors_amts)
    print(donor_list)


def prompt_title():
    title_tup = ('Prof.', 'Dr.', 'Ms.', 'Mr.')
    title = input('Title: "Prof.", "Dr.", "Ms." or "Mr."?: ')
    while True:
        try:
            title_tup.index(title)
            return title
        except ValueError:
            print('Not a valid title.\n')


def prompt_donation():
    # donation = 0
    while True:
        try:
            donation = input('Enter a Donation amount' +
                             ' (in USD): ')
            donation = int(donation)
            return donation
        except ValueError:
            print('Numeric value only, please.')


def add_donor(donor_name):
    # title_tup = ('Prof.', 'Dr.', 'Ms.', 'Mr.')
    # title = input('Title: "Prof.", "Dr.", "Ms." or "Mr."?: ')
    while True:
        try:
            # title_tup.index(title)
            prompt_title()
        except ValueError:
            print('Not a valid title.\n')
        try:
            # new_response = input('Enter a Donation amount' +
            #                      ' (in USD): ')
            # new_response = int(new_response)
            prompt_donation()
        except ValueError:
            print('Numeric value only, please.')
        print('Added to list of Donors:', title,
              donor_name, new_response)
        donors_amts[donor_name] = {'title': title,
                                   'donations':
                                   donation,
                                   'num_of_donations': 1}
        # title = donors_amts[donor_name]['title']
        send_ty(title, donor_name, donation)
        break


def prepare_ty():
    new_response = 0
    response_text = '\n'.join((
        'Enter full last name of Donor,',
        '"list" for List of Donors,',
        'or "e" to Exit back to Main Menu: '
      ))
    while True:
        response = input(response_text)
        if response in ('e', 'q') or not response.isalpha():
            if not response.isalpha():
                print('Not a name.')
            break
        if response == 'list':
            get_donor_list()
            print()
        else:
            response = response.capitalize()
            is_new = False
            if response not in donors_amts:
                print('This is a new donor.')
                title = prompt_title()
                is_new = True
            else:
                print('Donor found:', response)
                title = donors_amts[response]['title']
            donation_amt = prompt_donation()

            add_donation_amt(title, response, is_new, donation_amt)

            send_ty(title, response, donation_amt)
            print()


def send_ty(title, name, donation_amt):
    title = title.strip('\'')
    donor_dict = {'title': title,
                  'last_name': name,
                  'donation': donation_amt}
    ty_text = """
                Dear {title} {last_name},
                Thank you for your generous donation in the
                amount of {donation} USD.
              """
    print(ty_text.format(**donor_dict))


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
           '| Average Gift']
    print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
          psv[2], psv[3]))
    for i in range(55):
        print('-', end='')
    print()
    new_dict = {donor: [donors_amts[donor]['donations'],
                donors_amts[donor]['num_of_donations']] for
                donor in donors_amts}
    for donor in donors_amts:
        print('{:<15}'.format(donor)
              + '{}{:>10}'.format(' $', new_dict[donor][0])
              + '{:>12}'.format(new_dict[donor][1])
              + '{}{:>11}'.format(' $',
              new_dict[donor][0] // new_dict[donor][1]))
    print()


def send_letters():
    d_a = donors_amts
    title = ''
    now = datetime.datetime.now()
    for donor in d_a:
        title = d_a[donor]['title'].strip('\'')
        with open(donor + now.strftime('%Y%m%d')
                  + '.txt', 'w') as of:
            donor_dict = {'title': title,
                          'last_name': donor,
                          'donations': d_a[donor]['donations']}
            letter_text = """
            Dear {title} {last_name},
            Thank you for your generous previous giving
            in the amount of {donations} USD. Attached
            is our most recent independent, third
            party audit.

            We hope you agree that we have been good
            stewards of our donors' funds, and that
            you will consider donating again to our
            project.

            Best wishes for continued success,
            [Signature]
            """
            of.write(letter_text.format(**donor_dict))
            # of.write(
            #     'Dear {title} {last_name},\n'.format(**donor_dict)
            #     + 'Thank you for your generous previous giving'
            #     + ' in the amount of {donations} USD.'.format(**donor_dict))
            # of.write('\nAttached is our most recent independent,'
            #          + ' third party audit.\n')
            # of.write('\nWe hope you agree that we have been good'
            #          + ' stewards of our donors\' funds,\nand that'
            #          + ' you will consider donating'
            #          + ' again to our project.\n')
            # of.write('\nBest wishes for continued success,')
            # of.write('\n[Signature]')
    print('Generated a letter, just now, for each of the donors in the db.\n')


def test():
    pass


def program_run():
    menu_dict = {'1': prepare_ty, '2': get_report,
                 '3': send_letters, '4': test, 'q': sys.exit}
    main_text = '\n'.join((
        'Choose from the following:',
        '"1" - Send a "Thank You",',
        '"2" - Create a Report,',
        '"3" - Send Letters to All Donors,',
        '"4" - Test this program, or',
        '"q" to Quit: '
      ))
    while True:
        print('\nMain Menu:')
        response = input(main_text)
        print()
        try:
            if response == 'q':
                print('Program execution completed.')
            menu_dict[response]()
        except KeyError:
            print('KeyError occurred.')
            print('\nThat selection is invalid. Please try again.')


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')
