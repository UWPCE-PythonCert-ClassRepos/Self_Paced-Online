#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  15-Feb-2018
# ------------------------------------------- #

# Declare variables and data structure

donor_list = [
    ['William Gates, III', 653784.49, 2, 326892.24],
    ['Mark Zuckerberg', 16396.10, 3, 5465.37],
    ['Jeff Bezos', 877.33, 1, 877.33],
    ['Paul Allen', 708.42, 3, 236.14],
    ['Tri Nguyen', 100.00, 1, 100.00]
    ]


# Declare functions


def display_menu():
    ''' this function display a menu
        of 3 actions '''
    ACTIONS = ('Send a Thank You', 'Create a Report', 'Quit')

    print(''' Select one of the actions below:

    1. {}
    2. {}
    3. {}
    '''.format(*ACTIONS))


def send_thanks():
    ''' this function composes an email thanking
        the donor for their generous donation '''

    while True:

        full_name = input('Enter a Full Name (or type "list" to get the list of donors): ')

        if full_name.lower() == 'list':
            for idx, item in enumerate(donor_list):
                print(idx + 1, '-', donor_list[idx][0])
            continue

        elif full_name.title() not in [donor_list[idx][0] for idx, item in enumerate(donor_list)]:
            donation_amount = float(input('Enter donation amount: '))
            donor_list.append([full_name.title(), donation_amount, 1, donation_amount])

        elif full_name.title() in [donor_list[idx][0] for idx, item in enumerate(donor_list)]:
            donation_amount = float(input('Enter donation amount: '))
            for idx, item in enumerate(donor_list):
                if donor_list[idx][0] == full_name.title():
                    donor_list[idx][1] = donor_list[idx][1] + donation_amount
                    donor_list[idx][2] = donor_list[idx][2] + 1
                    donor_list[idx][3] = donor_list[idx][1] / donor_list[idx][2]

        choice = input('Do you want to quit and send email?(y/n) ')

        if choice == 'y':
            email_template = '''
                Dear {0},

                Thank you for giving us ${1:,.2f}. Your money will be put to good use.
                Please come back and donate more.

                Best Regards,

                John Doe
            '''
            print(email_template.format(full_name.title(), float(donation_amount)))

            break
        else:
            continue


def create_report():
    ''' this function generate a report of donors '''

    from operator import itemgetter
    # sort donor_list by total historical donation amount.

    template = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'
    value_template = '{0:<26} ${1:12.2f} {2:11} ${3:13.2f}'

    formatted_columns = template.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

    print(formatted_columns)

    print('{}'.format('-' * len(formatted_columns)))

    print('Report of Donors is below:\n')

    donor_list.sort(key=itemgetter(1), reverse=True)

    for idx, item in enumerate(donor_list):
        print(value_template.format(donor_list[idx][0], donor_list[idx][1], donor_list[idx][2], donor_list[idx][3]))
    print()


def main():
    ''' prompt user to see the menu of 3 actions '''

    while True:
        display_menu()

        action = input('Enter the corresponding number for action [1 to 3]:  ')
        print()

        if action == '1':
            send_thanks()

        elif action == '2':
            create_report()

        elif action.lower() == '3':
            break


# End of function definition


# Presentation

if __name__ == '__main__':
    main()
