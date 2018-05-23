#!/usr/bin/env python3

donors = [['Andy', [10.00]], ['Bill', [15.00, 25.00]], ['Chuck', [20.00, 30.00, 40.00]]]


def donor_list():
    for x in donors:
        print(x[0])
    thank_you()


def thank_you():
    print('Please enter the donor name\n (Type "list" for a list of current donor names)\n '
          'Press "q" to return to console')
    cd = input(':')

    if cd.lower() == 'list':
        donor_list()

    elif cd.lower == 'q':
        return

    else:

        amount = float(input('Please enter the donation amount:'))

        for j, k in enumerate(donors):
            if cd == k[0]:
                donors[j][1].append(amount)
                break
        else:
            donors.append([cd, [amount]])

        print('Thank you {} for your generous donation of ${:.2f}'.format(cd, amount))


def donor_report():
    print('Here is a list of donors and contributions')
    print('Name                 Total                Donations            Average')
    for data in donors:
        x = int(sum(data[1]))
        y = int(len(data[1]))
        print("|{:<20}|{:>20}|{:>20}|{:>20}|".format(data[0], x, y, x/y))
        # print(f'{data[0]:<20}'+f'${sum(data[1]):20}'+f'{len(data[1]):20}'+f'${sum(data[1])/len(data[1]):<20}')


def console():
    quit_console = False
    while not quit_console:

        print('Welcome to the Donor Tracking System')
        print('Please press a number to make a selection')
        print('1.) Send a thank you note')
        print('2.) Create a Report')
        print('3.) Quit(press "q")')

        cmd = input('>')

        if cmd == '1':
            thank_you()

        elif cmd == '2':
            donor_report()

        elif cmd in ('3', 'q', 'qqq'):
            quit_console = True

        # elif cmd.lower()=='qqq':
            # quit_console=True

        else:
            print('Please try again')
    

console()
