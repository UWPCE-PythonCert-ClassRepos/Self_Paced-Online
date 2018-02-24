#!/usr/bin/env python3

# Data
# refactoring: can change to a dictionary and use OrderedDict from
# 'collections' ('from collections import OrderedDict')
donors_amts = {'Gates': [('Mr.', ), 150000, 3], 'Brin': [('Mr.', ), 150000, 3], 
'Cerf': [('Mr.', ), 50000, 2], 'Musk': [('Mr.', ), 100000, 1], 
'Berners-Lee': [('Mr.', ), 50000, 2], 
'Wojcicki': [('Ms.', ), 125000, 1], 'Avey': [('Ms.', ), 200000, 2]}


# Processing
def send_ty():
    global donors_amts
    title = ''
    print()
    response = input('Enter full last name of Donor,'
    + '\n"list" for List of Donors'
    + ',\nor "e" to Exit back to Main Menu: ')
    print()
    # if response == 'e':
    #    program_run()
    if response.isalpha():
        if response == 'list':
            print('Here is the list of Donors: ')
            # donors_amts.sort()
            for donor in donors_amts:
                print(donor)
            print()
        else:
            response = response.capitalize()
            if response in donors_amts:
                print('Donor found:', response)
                new_response = int(input('Enter a Donation amount' +
                ' (in USD): '))
                donors_amts[response][1] += new_response
                donors_amts[response][2] += 1
                print('Added to', response, '\'s Donations:',
                    new_response, '\n')
            elif response not in donors_amts:
                title = input('Title: "Ms." or "Mr."?: ')
                new_response = int(input('Enter a Donation amount' +
                    ' (in USD): '))
                print('Added to list of Donors:', title,
                    response, new_response)
                donors_amts[response] = ([(title, ), new_response, 1])
            title = str(donors_amts.get(response)[0])
            title = title.strip('(').strip(')').strip(',')
            title = title.strip('\'')
            form_st = 'Dear {} {}, Thank you for your generous donation in the amount of {} USD.'
            print(form_st.format(title,
                response, new_response))
            print()
    program_run()


def get_report():
# print('Here is the full List:')
# donors_amts.sort()
# for donor in donors_amts:
# print(donor, '\n')
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
