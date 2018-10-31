# Mailroom_pt3.py Exercise by tfbanks

# !/usr/bin/env python3


# Donor Database containing names and donations
donor_names = {
    'Tim Cooker': [1500.50, 25050.50, 15680.75],
    'Elon Musket': [5250.25, 26500],
    'Frank Petersmankempt': [550.60],
    'Megan Morgan': [650.40, 1600, 20625.40],
    'Marlene Wheeler': [820, 1222.80]}


def thank_you():  # Code for selecting Donor and writing a Thank You Note
    ty_donor = input('Enter the Full Name of a donor (for list of previous donors type list): ').title()
    letter = ('''\n\nDear {},\n
Thank you for your generous donation of ${:,.2f}, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n
Joesef Edword Bringingham\n\n''')
    if ty_donor == 'List':  # If List, Prints Donor List and restarts the function
        for donor in donor_names.keys():
            print(donor)
        print('\n')
        ty_donor = input('Enter the Full Name of a donor (for list of previous donors type list): ').title()

    while True:
        try:
            amount = float(input('Please enter the donation amount: '))
        except ValueError:
            print('Please enter a valid donation amount')
            continue
        break

    if ty_donor in donor_names:  # Actions if donor is already in donor_names
        donor_names[ty_donor].append(amount)  # Appends donation amount to donators donation values
    else:
        donor_names[ty_donor] = [amount]

    print(letter.format(ty_donor, amount))


def report():  # Defines parameters of the report of donors, creates a new list of summarized details per donor, sorts, and prints it.
    print('\nDonor Name            |  Total Given | Num Gifts |  Average Gift')
    print('------------------------------------------------------------------')
    donor_rpt = [[donor, sum(donations), len(donations), sum(donations)/len(donations)] for donor, donations in donor_names.items()]
    sorted_rpt = sorted(donor_rpt, key=lambda x: x[1], reverse=True)
    for donor_rpt in sorted_rpt:
        print('{:24s} ${:11,.2f} {:^12} ${:12,.2f}'.format(donor_rpt[0], donor_rpt[1], donor_rpt[2], donor_rpt[3]))
    print('\n')


def mass_mail():
    mm_letter = ('''\n\nDear {},\n
Thank you for your generous donations totaling ${:,.2f}, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n 
Joesef Edword Bringingham\n\n''')
    for donor, donations in donor_names.items():
        letter = mm_letter.format(donor, sum(donations))
        letter_output = donor + '.txt'
        with open(letter_output, 'w') as op:
            for line in letter:
                op.write(line)
    print('\nLetters are located in your working directory folder\n\n')


if __name__ == '__main__':
    while True:
        answer = input('''Please choose an action from the following options:
 1 - Send a Thank You
 2 - Create a Report
 3 - Send letters to everyone
 4 - Quit\n''')

        try:
            answer = int(answer)
        except ValueError:
            print('''Enter the actions's associated number''')
        if answer == 1:
            thank_you()
        elif answer == 2:
            report()
        elif answer == 3:
            mass_mail()
        elif answer == 4:
            print('Have a nice day')
            break
