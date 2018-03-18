#!/usr/bin/env python3
import datetime

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
    donor_list = [donor for donor in donors_amts]
    print(donor_list)


def add_donor(donor_name):
    title_tup = ('Prof.', 'Dr.', 'Ms.', 'Mr.')
    title = input('Title: "Prof.", "Dr.", "Ms." or "Mr."?: ')
    while True:
        try:
            title_tup.index(title)
        except ValueError:
            print('Not a valid title.\n')
            title = input('Enter donor\'s title: ')
            try:
                title_tup.index(title)
            except ValueError:
                print('Invalid entry. Returning to main menu.')
                break
        try:
            new_response = input('Enter a Donation amount' +
                                 ' (in USD): ')
            new_response = int(new_response)
        except ValueError:
            print('Numeric value only, please.')
            new_response = input('Enter a Donation amount' +
                                 ' (in USD): ')
            try:
                new_response = int(new_response)
            except ValueError:
                print('That is not a valid input.')
                break
        print('Added to list of Donors:', title,
              donor_name, new_response)
        donors_amts[donor_name] = {'title': title,
                                   'donations':
                                   new_response,
                                   'num_of_donations': 1}
        title = donors_amts[donor_name]['title']
        send_ty(title, donor_name, new_response)
        break


def prepare_ty():
    new_response = 0
    title = ''
    donor_dict = {'title': '', 'last_name': '', 'donation': 0}
    while True:
        response = input('Enter full last name of Donor,'
                         + '\n"list" for List of Donors'
                         + ',\nor "e" to Exit back to Main Menu: ')
        if response == 'e' or response == 'q':
            break
        else:
            if response == 'list':
                get_donor_list()
                print()
            else:
                if response.isalpha():
                    response = response.capitalize()
                    if response in donors_amts:
                        print('Donor found:', response)
                        new_response = input('Enter a Donation amount' +
                                             ' (in USD): ')
                        try:
                            new_response = int(new_response)
                        except ValueError:
                            print('\nEnter a numeric value.')
                            new_response = input('Enter a Donation amount' +
                                                 ' (in USD): ')
                            try:
                                new_response = int(new_response)
                            except ValueError:
                                print('That is not a valid input.'
                                      + ' Restarting program.')
                                break
                        else:
                            donors_amts[response]['donations'] += new_response
                            donors_amts[response]['num_of_donations'] += 1
                            print('Added to', response, '\'s Donations:',
                                  new_response, '\n')
                    elif response not in donors_amts:
                        add_donor(response)
                        break
                    title = donors_amts[response]['title']
                    send_ty(title, response, new_response)
                elif not response.isalpha():
                    print('Your response has digit(s).'
                          + ' Returning to main menu.')
                    break
                print()


def send_ty(title, name, donation):
    title = title.strip('\'')
    donor_dict = {'title': title,
                  'last_name': name,
                  'donation': donation}
    print('Dear {title} {last_name},'.format(**donor_dict)
          + ' Thank you for your generous donation in the'
          + ' amount'
          + ' of {donation} USD.'.format(**donor_dict))


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
           '| Average Gift']
    print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
          psv[2], psv[3]))
    for i in range(55):
        print('-', end='')
    print()
    new_dict = {donor: [donor['donations'], donor['num_of_donations']]
                for donor in donors_amts}
    for donor in donors_amts:
        # d1 = donors_amts[donor]['donations']
        # d2 = donors_amts[donor]['num_of_donations']
        print('{:<15}'.format(**new_dict)
              + '{}{:>10}'.format(' $', **new_dict)
              + '{:>12}'.format(**new_dict)
              + '{}{:>11}'.format(' $', **new_dict)
              + new_dict[donor][0] // new_dict[donor][1])
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
            of.write(
                'Dear {title} {last_name},\n'.format(**donor_dict)
                + 'Thank you for your generous previous giving'
                + ' in the amount of {donations} USD.'.format(**donor_dict))
            of.write('\nAttached is our most recent independent,'
                     + ' third party audit.\n')
            of.write('\nWe hope you agree that we have been good'
                     + ' stewards of our donors\' funds,\nand that'
                     + ' you will consider donating'
                     + ' again to our project.\n')
            of.write('\nBest wishes for continued success,')
            of.write('\n[Signature]')
    print('A letter was generated, just now, for each of the donors in db.\n')


def program_run():
    while True:
        print('\nMain Menu:')
        response = input('Choose from the following:'
                         + '\n"1" - Send a "Thank You",'
                         + '\n"2" - Create a Report,'
                         + '\n"3" - Send Letters to All Donors,'
                         + '\nor "q" to Quit: ')
        print()
        menu_dict = {'1': prepare_ty, '2': get_report,
                     '3': send_letters}
        try:
            if response == 'q':
                print('Program execution completed.')
                break
            else:
                menu_dict.get(response)()
        except TypeError:
            print('\nThat selection is invalid. Please try again.')
            try:
                response = input('Choose "1", "2", "3", or "q": ')
                if response == 'q':
                    print('Program execution completed.')
                    break
                else:
                    menu_dict.get(response)()
            except TypeError:
                print('That is not an option. Closing program.')
                break


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')
