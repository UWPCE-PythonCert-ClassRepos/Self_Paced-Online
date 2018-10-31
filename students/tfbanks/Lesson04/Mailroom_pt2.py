# mailroom_pt2.py Exercise by tfbanks

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
    letter = ('\n\nDear {},\n'
              '\nThank you for your generous donation of ${:,.2f}, your generosity is greatly appreciated.\n'
              'These funds will help continue our efforts to teach Python to the next generation.\n'
              '\nSincerely,\n'
              '\nJoesef Edword Bringingham\n\n')
    if ty_donor == 'List':  # If List, Prints Donor List and restarts the function
        for donor in donor_names.keys():
            print(donor)
        thank_you()
    elif ty_donor in donor_names:  # Actions if donor is already in donor_names
        amount = float(input('Please enter the donation amount: '))
        donor_names[ty_donor].append(amount)  # Appends donation amount to donators donation values
        print(letter.format(ty_donor, amount))
        what_to_do()  # Takes user back to action options
    elif ty_donor not in donor_names:  # If donor is not on the list, this collects the data, adds to the donor_names dictionary, and writes a new letter.
        amount = float(input('Please enter the donation amount: '))
        donor_names[ty_donor] = [amount]
        print(letter.format(ty_donor, amount))
        what_to_do()  # Takes user back to action options


def report():  # Defines parameters of the report of donors and prints it.
    print('\nDonor Name            |  Total Given | Num Gifts |  Average Gift')
    print('------------------------------------------------------------------')
    for donor, donations in donor_names.items():
        print('{:24s}'.format(donor), '${:11,.2f}'.format(sum(donations)), '{:^12}'.format(len(donations)),
              '${:12,.2f}'.format(sum(donations)/len(donations)))
    print('\n')
    what_to_do()  # takes the user to another what to do statement that reflects they just ran a report


def mass_mail():

    mm_letter = ('\n\nDear {},\n'
              '\nThank you for your generous donations totaling ${:,.2f}, your generosity is greatly appreciated.\n'
              'These funds will help continue our efforts to teach Python to the next generation.\n'
              '\nSincerely,\n'
              '\nJoesef Edword Bringingham\n\n')
    for donor, donations in donor_names.items():
        letter = mm_letter.format(donor, sum(donations))
        letter_output = donor + '.txt'
        with open(letter_output, 'w') as op:
            for line in letter:
                op.write(line)
    print('\n\nLetters are located in your working directory folder\n\n')
    what_to_do()


def quit_option():
    print('Have a nice day')
    quit()


def what_to_do():
    answer = input('Please choose an action from the following options:\n\n'
                   '1 - Send a Thank You\n'
                   '2 - Create a Report\n'
                   '3 - Send letters to everyone\n'
                   '4 - Quit\n')
    while answer not in ['1', '2', '3', '4']:
        what_to_do()
    selection(answer)()


def selection(option):
    switch_fun_dict = {'1': thank_you, '2': report, '3': mass_mail, '4': quit_option}
    return switch_fun_dict[option]


if __name__ == '__main__':
    what_to_do()
