#!/usr/bin/env python3
import datetime

# Data
# refactor from tuple to no tuple (see Natasha's comments on
# mailroom2 assignment)
donors_amts = {'Gates': [('Mr.', ), 150000, 3], 'Brin': [('Mr.', ), 150000, 3], 
'Cerf': [('Mr.', ), 50000, 2], 'Musk': [('Mr.', ), 100000, 1], 
'Berners-Lee': [('Mr.', ), 50000, 2], 
'Wojcicki': [('Ms.', ), 125000, 1], 'Avey': [('Ms.', ), 200000, 2]}


# Processing
def send_ty():
    global donors_amts
    new_response = 0
    title = ''
    donor_dict = {'title': '', 'last_name': '', 'donation': 0}
    print()
    response = input('Enter full last name of Donor,'
    + '\n"list" for List of Donors'
    + ',\nor "e" to Exit back to Main Menu: ')
    print()
    # add try-except catch block(s)
    if response.isalpha():
        if response == 'list':
            print('Here is the list of Donors: ')
            for donor in donors_amts:
                print(donor)
            print()
        else:
            response = response.capitalize()
            if response in donors_amts:
                print('Donor found:', response)
                new_response = input('Enter a Donation amount' +
                ' (in USD): ')
                # add try-except catch block(s)
                if not new_response.isnumeric():
                    send_ty()
                else:
                    new_response = int(new_response)
                    # add comprehension(s) here?
                    donors_amts[response][1] += new_response
                    donors_amts[response][2] += 1
                    print('Added to', response, '\'s Donations:',
                    new_response, '\n')
            elif response not in donors_amts:
                title = input('Title: "Ms." or "Mr."?: ')
                new_response = input('Enter a Donation amount' +
                    ' (in USD): ')
                # add try-except catch block here
                if not new_response.isnumeric():
                    send_ty()
                else:
                    new_response = int(new_response)
                    print('Added to list of Donors:', title,
                        response, new_response)
                    # add comprehension(s) here?
                    donors_amts[response] = ([(title, ), new_response, 1])
            title = str(donors_amts.get(response)[0])
            title = title.strip('(').strip(')').strip(',')
            title = title.strip('\'')
            donor_dict = {'title': title,
                    'last_name': response, 'donation': new_response}
            print('Dear {title} {last_name}, Thank you for your generous donation in the amount of {donation} USD.'.format(**donor_dict))
            print()
    program_run()


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
        '| Average Gift']
    print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
        psv[2], psv[3]))
    for i in range(55):
        print('-', end='')
    print()
    # add comprehension here
    for donor in donors_amts:
        d1 = donors_amts[donor][1]
        d2 = donors_amts[donor][2]
        print('{:<15}{}{:>10}{:>12}{}{:>11}'.format(donor, '  $',
            d1, d2, '  $', d1 // d2))
    print()
    program_run()


def send_letters():
    global donors_amts
    d_a = donors_amts
    now = datetime.datetime.now()
    for donor in donors_amts:
        title = str(d_a.get(donor)[0])
        title = title.strip('(').strip(')').strip(',').strip('\'')
        with open(donor + str(now.year) + str(now.month) +
            str(now.day) + '.txt', 'w') as of:
            donor_dict = {'title': title,
                    'last_name': donor, 'donations': d_a.get(donor)[1]}
            of.write(
                'Dear {title} {last_name},\nThank you for your generous previous giving in the amount of {donations} USD.'.format(**donor_dict))
            of.write('\nAttached is our most recent independent,'
                + ' third party audit.\n')
            of.write('\nWe hope you agree that we have been good'
                + ' stewards of our donors\' funds,\nand that'
                + ' you will consider donating'
                + ' again to our project.\n')
            of.write('\nBest wishes for continued success,')
            of.write('\n[Signature]')
            of.close()


def quit_program():
    print('Program execution completed.')
    return


def program_run():
    print('Main Menu:')
    # add try-catch block here
    response = input('Choose from the following:\n"1" - Send a "Thank You",'
        + '\n"2" - Create a Report,'
        + '\n"3" - Send Letters to All Donors, or\n"q" to Quit: ')
    menu_dict = {'1': send_ty, '2': get_report,
        '3': send_letters, 'q': quit_program}
    # add try-catch block here
    if response in menu_dict:
        menu_dict.get(response)()
    else:
        response = input('Choose "1", "2", "3", or "q": ')
        # add try-catch block here
        if response in menu_dict:
            menu_dict.get(response)()
        else:
            print('That is not an option. Closing program.')
            return


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')
