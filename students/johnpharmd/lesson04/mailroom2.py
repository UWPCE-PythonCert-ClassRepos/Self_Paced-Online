#!/usr/bin/env python3

# Data
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
                if not new_response.isnumeric():
                    send_ty()
                else:
                    new_response = int(new_response)
                    donors_amts[response][1] += new_response
                    donors_amts[response][2] += 1
                    print('Added to', response, '\'s Donations:',
                    new_response, '\n')
            elif response not in donors_amts:
                title = input('Title: "Ms." or "Mr."?: ')
                new_response = input('Enter a Donation amount' +
                    ' (in USD): ')
                if not new_response.isnumeric():
                    send_ty()
                else:
                    new_response = int(new_response)
                    print('Added to list of Donors:', title,
                        response, new_response)
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
    for donor in donors_amts:
        d1 = donors_amts[donor][1]
        d2 = donors_amts[donor][2]
        print('{:<15}{}{:>10}{:>12}{}{:>11}'.format(donor, '  $',
            d1, d2, '  $', d1 // d2))
    print()
    program_run()


def quit_program():
    print('Program execution completed.')
    return


def program_run():
    print('Main Menu:')
    response = input('Choose from the following:\n"1" - Send a "Thank You",'
        + '\n"2" - Create a Report, or\n"q" to Quit: ')
    menu_dict = {'1': send_ty, '2': get_report, 'q': quit_program}

    if response in menu_dict:
        menu_dict.get(response)()
    else:
        response = input('Choose "1", "2", or "q": ')
        if response == '1' or response == '2' or response == 'q':
            menu_dict.get(response)()
        else:
            print('That is not an option. Closing program.')
            return


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')
