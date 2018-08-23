#!/usr/bin/env python3
if __name__ == "__main__":
	#this will only run if run as a script.
    print("This is inside the name:main block.")
donors = [['William Gates, III', [140.00]], ['Mark Zuckerberg', [456.00, 75.50]], ['Jeff Bezos ', [134.00, 134.00]], ['Paul Allen  ', [50.00, 5.00, 5540.00]]]


def donor_list():
    for donor in donors:
        print(donor[0])
    thank_you()


def thank_you():
    print('Please enter the donor name\n (Type "ls" for a list of current donors)\n '
          'Press "q" to return to console')
    cd = input(':')
    if cd.lower() == 'ls':
        donor_list()
    elif cd.lower == 'q':
        return
    else:
        amount = float(input('Please enter the amount:'))
        for i, k in enumerate(donors):
            if cd == k[0]:
                donors[i][1].append(amount)
                break
        else:
            donors.append([cd, [amount]])
        print('Thank you {} for your donation of ${:.2f}'.format(cd, amount))


def donor_report():
    print('Here is the list of donors and donations')
    print('Donor Name                 Total Given                Num Gifts            Average Gift')
    for data in donors:
        x = int(sum(data[1]))
        y = int(len(data[1]))
        #print("|{:<20}|{:>20}|{:>20}|{:>20}|".format(data[0], x, y, x/y))
        print("|{:>20}|{:>20}|{:>20}|{:>20}|".format(data[0], x, y, round(x / y, 2)))

def menu():
    quit_menu = False
    while not quit_menu:
        print('Welcome to the Donor Tracking')
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
            quit_menu = True
        else:
            print('Please press a number to make a selection')

    # Run the Mailroom program.
menu()