#!/usr/bin/env python3

# donors = [['Andy', [10.00]], ['Bill', [15.00, 25.00]], ['Chuck', [20.00, 30.00, 40.00]]]

donors = {'Andy': [10.00], 'Bill': [15.00, 25.00], 'Chuck': [20.00, 30.00, 40.00]}


def donor_list():
    for name in donors:
        print(name)
    thank_you()


def thank_you():
    print('Please enter the donor name\n (Type "list" for a list of current donor names)\n '
          'Press "q" to return to console')
    new_donor = input(':')

    if new_donor.lower() == 'list':
        donor_list()

    elif new_donor.lower() == 'q':
        return

    else:

        amount = float(input('Please enter the donation amount:'))

        if new_donor in donors:
            donors[new_donor].append(amount)

        else:
            donors[new_donor] = [amount]

        print('Thank you {} for your generous donation of ${:.2f}'.format(new_donor, amount))


def donor_report():
    print('Here is a list of donors and contributions')
    print('Name                 Total                Donations            Average')
    for data in donors:
        total_donation = int(sum(donors[data]))
        avg_donation = len(donors[data])
        print('|{:<20}|{:>20}|{:>20}|{:>20}|'.format(data, total_donation, avg_donation, total_donation / avg_donation))
        # print(f'{data[0]:<20}'+f'${sum(data[1]):20}'+f'{len(data[1]):20}'+f'${sum(data[1])/len(data[1]):<20}')


def batch_file():
    for data in donors:
        filename = data.replace(" ", "_") + ".txt"
        total_donation = sum(donors[data])
        letter = ('Thank you {} for you generous contributions totalling {:.2f}!'.format(data, total_donation))
        open(filename, 'w').write(letter)
        print(f"{data}'s letter has been saved to " + filename)


def console():
    quit_console = False
    while not quit_console:

        print('Welcome to the Donor Tracking System')
        print('Please press a number to make a selection')
        print('1.) Send a thank you note')
        print('2.) Create a Report')
        print('3.) Send letters to everyone! ')
        print('4.) Quit(press "q")')

        cmd = input('>')

        if cmd == '1':
            thank_you()

        elif cmd == '2':
            donor_report()

        elif cmd == '3':
            batch_file()

        elif cmd in ('4', 'q', 'qqq'):
            quit_console = True

        # elif cmd.lower()=='qqq':
            # quit_console=True

        else:
            print('Please try again')
    

console()
