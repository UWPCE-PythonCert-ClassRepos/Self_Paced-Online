#!/usr/bin/env python3

#uw python 210
#lesson 03
#max anderson

#mailroom.py


donor_list = [
              ['Andrew Jackson', 10000, 5, 2000],
              ['Benjamin Franklin', 253000, 2, 117500],
              ['John Kennedy', 20, 1, 20],
              ['Abraham Lincoln', 807, 2, 403.5],
              ['Jim Jones', 918, 1, 918]
             ]

# Index 0 - Donor Name
# Index 1 - Donation Totals
# Index 2 - Number of Donations
# Index 3 - Average Donation

def menu():
    runval = 1
    while(runval == 1):
        print('\n'
          'Welcome to Mail Room™ \n'
            '--------------------- \n'
            '1) Send a Thank You \n'
            '2) Create a Report \n'
            '3) Quit \n'
            )
        n = int(input('Enter a number: '))

        while(n not in (1, 2, 3)):
            n = int(input('Enter 1, 2, or 3): '))

        if n == 1: runval = thank_you()
        elif n == 2: runval = create_report()
        elif n == 3: runval = 0
    print('Goodbye.')
    return


def thank_you():
    print()
    name = input('Enter full name of \'Thank You\' recipient: ').title()

    while(name == 'List'):
        list_donors()
        name = input('Enter full name of \'Thank You\' recipient: ').title()

    if name in ('E', 'Exit'):
        print('Exiting...')
        return 1

    if in_list(name): enter_donation(name)
    elif not in_list(name): new_donor(name)

    format_thx(name)
    return 1


def list_donors():
    print()
    for donor in donor_list:
        print(donor[0])
    print()


def new_donor(name):
    donor_list.append([name, 0, 0, 0])
    print('New donor added. \n')
    enter_donation(name)


def enter_donation(name):
    amount = float(input('Enter donation amount: '))
    i = get_index(name)
    #add amount to donation totals
    donor_list[i][1] += amount
    #increment number of donations
    donor_list[i][2] += 1
    #adjust average donation
    donor_list[i][3] = (donor_list[i][1] / donor_list[i][2])


def in_list(name):
    for i in range(len(donor_list)):
        if name == donor_list[i][0]:
            return 1
        elif name != donor_list[i][0] and i == len(donor_list):
            return 0


#returns the index of any known donor
def get_index(name):
    for i in range(len(donor_list)):
        if name == donor_list[i][0]:
            return i


def format_thx(name):
    i = get_index(name)

    print()
    print(f'Dear {name}, \n')
    print('Thank you for your generosity. '
          'Having donated {:,} times for a total of ${:.2f}, '
          'your most recent gift enables us to continue our mission '
          'of serving vulnerable populations in your local community. '
          'We can not overstate how important contributions like this '
          'are to our organization and those we serve. \n'
          .format(donor_list[i][2], donor_list[i][1]))
    print('Sincerely, \n')
    print('Automated Form letter')


def create_report():
    print()
    print('Donor Name             | Donation Total   | Num   | Average')
    print('-----------------------------------------------------------')
    for i in range(len(donor_list)):
        print('{:<23}$ {:<17,.2f}{:<8d}$ {:<0,.2f}'.format(*donor_list[i]))
    return 1


if __name__ == "__main__":

    menu()
