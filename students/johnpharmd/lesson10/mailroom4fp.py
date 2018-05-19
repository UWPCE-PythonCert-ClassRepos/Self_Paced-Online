#!/usr/bin/env python3
import datetime
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
def get_donors_amts():
    return donors_amts


def get_donor_list():
    if __name__ == '__main__':
        print(list(donors_amts))
    else:
        return list(donors_amts)


def prompt_title():
    title_tup = ('Prof.', 'Dr.', 'Ms.', 'Mr.')
    while True:
        title = input('Title: "Prof.", "Dr.", "Ms." or "Mr."?: ')
        try:
            title_tup.index(title)
            return title
        except ValueError:
            print('Not a valid title.\n')


def prompt_donation():
    while True:
        try:
            donation = int(input('Enter a Donation amount' +
                                 ' (in USD): '))
            return donation
        except ValueError:
            print('Numeric value only, please.')


def add_donor(donor_name, title):
    if __name__ == '__main__':
        print('Added to list of Donors:', title, donor_name)
    donors_amts[donor_name] = {'title': title,
                               'donations': 0,
                               'num_of_donations': 0}


def add_donation_amt(name, title, new_donor, donation_amt):
    if new_donor:
        add_donor(name, title)
    donors_amts[name]['donations'] += donation_amt
    donors_amts[name]['num_of_donations'] += 1


def prepare_ty():
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
            new_donor = False
            if response not in donors_amts:
                new_donor = True
                print('\nThis is a new donor.')
                title = prompt_title()
            else:
                print('Donor found:', response)
                title = donors_amts[response]['title']
            donation_amt = prompt_donation()

            add_donation_amt(response, title, new_donor, donation_amt)

            send_ty(title, response, donation_amt)
            break


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
    if __name__ == '__main__':
        print(ty_text.format(**donor_dict))
    else:
        return ty_text.format(**donor_dict)


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
           '| Average Gift']
    if __name__ == '__main__':
        print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
              psv[2], psv[3]))
        for i in range(55):
            print('-', end='')
        print()
    new_list = [[donors_amts[donor]['donations'], donor,
                donors_amts[donor]['num_of_donations']] for
                donor in donors_amts]
    new_list.sort(reverse=True)
    for donor_list in new_list:
        formatted_donor = ('{:<15}'.format(donor_list[1])
                           + '{}{:>10}'.format(' $', donor_list[0])
                           + '{:>12}'.format(donor_list[2])
                           + '{}{:>11}'.format(' $',
                           donor_list[0] // donor_list[2]))
        if __name__ == '__main__':
            print(formatted_donor)


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
    if __name__ == '__main__':
        print('Generated a letter, just now, for each donor in the db.\n')


def filter_donations(donations, min_donation, max_donation):
    return min_donation > donations or donations > max_donation


def challenge(donations, factor):
    return donations * factor


def challenge_map(factor, **donation_min_and_max):
    donors_list = []
    donations_list = []
    factor_list = []
    for donor, donor_dict in donors_amts.items():
        donors_list.append(donor)
        donations_list.append(donor_dict['donations'])
        factor_list.append(factor)
    if donation_min_and_max:
        # fixme: adding this 'for' loop on 5/19 crashed both test_challenge_map and
        # test_challenge_filter. Previously, test_challenge_map passed.
        for donations_amt in donations_list[:]:
            filter(filter_donations(donations_amt, **donation_min_and_max),
                   donations_list)

        #                     filter(filter_donations(**donation_min_and_max),
        #                            donations_list))
        # donations_list = list(filter(donation_range(donations,
        #  **donation_min_and_max), donations_list))
        print('donations list after filtering:', donations_list)
    donations_map = map(challenge, donations_list, factor_list)
    new_donors_amts_zip = zip(donors_list, donations_map)
    for donor_tuple in new_donors_amts_zip:
        donors_amts[donor_tuple[0]]['donations'] = donor_tuple[1]
    # print(donors_amts)
    return donors_amts


def program_run():
    menu_dict = {'1': prepare_ty, '2': get_report,
                 '3': send_letters, 'q': sys.exit}
    main_text = '\n'.join((
        'Choose from the following:',
        '"1" - Send a "Thank You",',
        '"2" - Create a Report,',
        '"3" - Send Letters to All Donors, or',
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
            print('\nThat selection is invalid. Please try again.')


# I/O
if __name__ == '__main__':
    program_run()
