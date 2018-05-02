donor_db = [["John Smith", 18774.48, 8264.47, 7558.71], ["Jane Doe", 281918.99, 8242.13],
            ["Alan Smithee", 181.97, 955.16], ["Tom D.A. Harry", 67.10, 500.98], ["Joe Shmoe", 200.01]]


def thank_you():
    print('Enter a donor\'s full name, or type \'list\' for a full list. '
          'Type \'e\' to exit and return to the main menu.')
    user_input = input("> ").title()
    if user_input.lower() == 'list':
        for ind_donor in donor_db:
            print(ind_donor[0])
        thank_you()
    elif user_input.lower() == 'e':
        mailroom()
    else:
        donation = float(input("Please enter a donation amount: "))
        new_donor = [user_input, donation]
        donor_list = []
        for ind_donor in donor_db:
            donor_list.append(ind_donor[0])
        if new_donor[0] in donor_list:
            for ind_donor in donor_db:
                if ind_donor[0] == new_donor[0]:
                    ind_donor.append(donation)
                    print("Appending the amount of {0} to {1}'s file...".format(donation, new_donor[0]))
                    print("Printing thank you email...")
                    print("---------------------------")
                    print("Dear {0}:".format(ind_donor[0]))
                    print("\nThank you for your donation of ${0}, and for your continuing support!".format(donation))
                    print("Your generous contributions are essential for our charity to continue operating.")
                    print("\nSincerely,\nJonathan Mauk")
                    print("---------------------------")
                    print("Returning to menu...")
                    thank_you()
        else:
            donor_db.append(new_donor)
            print("New donor detected. Creating record for {0}...".format(user_input))
            print("Printing thank you email...")
            print("---------------------------")
            print("Dear {0}:".format(user_input))
            print("\nThank you for your donation of ${0}.".format(donation))
            print("Your generous contribution is essential for our charity to continue operating.")
            print("\nSincerely,\nJonathan Mauk")
            print("---------------------------")
            print("Returning to menu...")
            thank_you()


def report():
    print('Donor Name' + ' ' * 16 + '| Total Given | Num Gifts | Average Gift')
    print('-' * 66)
    for ind_donor in donor_db:
        donor_name = ind_donor[0]
        num_gifts = len(ind_donor[1:])
        total_given = sum(ind_donor[1:])
        average_gifts = total_given / num_gifts
        print(f'{donor_name: <26}| ${total_given:>10.2f} |{num_gifts:^11}| ${average_gifts:>11.2f}')
    print('\nReturning to main menu...')
    mailroom()


def mailroom():
    print('''
    MAILROOM v0.1
    ------------------------
    Choose an option:
    1) Send a thank you
    2) Create a report
    3) Quit
    ''')
    selection = input("> ")
    if selection == '1':
        thank_you()
    elif selection == '2':
        report()
    elif selection == '3':
        exit("Exiting program. Goodbye!")
    else:
        print("Invalid value. Enter a number from 1-3.")
        mailroom()

mailroom()

if __name__ == "__main__":
    mailroom()
