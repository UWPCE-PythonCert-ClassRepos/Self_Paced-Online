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
    for donor in donors_amts:
        print(donor)


def add_donor():
    title = input('Title: "Ms." or "Mr."?: ')
    try:
        [int(char)/0 for char in title if char.isdigit()]
        # if title != 'Ms.' or 'Mr.':
        # if title[0] != 'M':
        #     print(n)  # triggers a NameError
        # elif title[1] != 's' or title[1] != 'r':
        #     pass
        # elif len(title) > 3:
        #     pass
    except ZeroDivisionError:
        print('Choose a title (no digits, please).\n')
    except NameError:
        print('Choose a title ("Ms." or "Mr.").\n')
    # finally:
    else:
        try:
            # title = input('Title: "Ms." or "Mr."?: ')
            # if title != 'Ms.' or 'Mr.':
            #     print('Invalid input. Closing program.')
            #     return
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
                print('That is not a valid input.'
                      + 'Closing program.')
                return
        else:
            print('Added to list of Donors:', title,
                  response, new_response)
            donors_amts[response] = {'title': title,
                                     'donations':
                                     new_response,
                                     'num_of_donations': 1}


def send_ty():
    new_response = 0
    title = ''
    donor_dict = {'title': '', 'last_name': '', 'donation': 0}
    while True:
        response = input('\nEnter full last name of Donor,'
                         + '\n"list" for List of Donors'
                         + ',\nor "e" to Exit back to Main Menu: ')
        if response == 'e':
            break
        else:
            if response == 'list':
                get_donor_list()
            else:
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
                                  + ' Closing program.')
                            break
                    else:
                        donors_amts[response]['donations'] += new_response
                        donors_amts[response]['num_of_donations'] += 1
                        print('Added to', response, '\'s Donations:',
                              new_response, '\n')
                elif response not in donors_amts:
                    add_donor()
                title = donors_amts[response]['title']
                title = title.strip('\'')
                donor_dict = {'title': title,
                              'last_name': response,
                              'donation': new_response}
                # if format string is separated, it breaks so that
                # title and last_name are not formatted
                print('Dear {title} {last_name},'.format(**donor_dict)
                      + ' Thank you for your generous donation in the'
                      + ' amount'
                      + ' of {donation} USD.'.format(**donor_dict))
                print()


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
           '| Average Gift']
    print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
          psv[2], psv[3]))
    for i in range(55):
        print('-', end='')
    print()
    # add comprehension here?
    for donor in donors_amts:
        d1 = donors_amts[donor]['donations']
        d2 = donors_amts[donor]['num_of_donations']
        print('{:<15}{}{:>10}{:>12}{}{:>11}'.format(donor, '  $',
              d1, d2, '  $', d1 // d2))
    print()


def send_letters():
    d_a = donors_amts
    title = ''
    # Natasha recommended datetime.datetime.now().strftime('%Y%m%d')
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
        menu_dict = {'1': send_ty, '2': get_report,
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
                menu_dict.get(response)()
            except TypeError:
                print('That is not an option. Closing program.')
                break


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')
