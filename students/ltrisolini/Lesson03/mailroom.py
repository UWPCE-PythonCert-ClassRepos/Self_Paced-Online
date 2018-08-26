#!/usr/bin/env python3

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
    print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------------------\n")
    report = []  # initialize report

    # for each_name in get_all_donor_names(donors):
    for each_donor in donors:
            total_donation = 0  # initialize total donation from the same donor
            # Get total donation from each donor
            for i in range(len(each_donor[1])):
                    total_donation += each_donor[1][i]
            report.append([each_donor[0], total_donation, len(each_donor[1])])

    # sorting the report based on donations
    r_sorted = sorted(report, key=lambda r: r[1], reverse=True)

    # Create the report
    for d in range(len(r_sorted)):
            print("{:23}${:12.2f}{:10}   ${:12.2f}".format(r_sorted[d][0],
                    r_sorted[d][1],
                    r_sorted[d][2],
                    r_sorted[d][1]/r_sorted[d][2]))

    print("\n")
    #main()

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

if __name__ == "__main__":
   menu()