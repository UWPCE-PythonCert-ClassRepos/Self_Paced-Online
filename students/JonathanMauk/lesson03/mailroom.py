donor_db = [["John Smith", 18000, 8200, 7500], ["Jane Doe", 281000, 8200],
              ["Alan Smithee", 180, 950], ["Tom D.A. Harry", 60, 500], ["Joe Shmoe", 200]]


def thank_you():
    print('Enter a donor\'s full name, or type \'list\' for a full list. '
          'Type \'e\' to exit and return to the main menu.')
    user_input = input("> ").title()
    if user_input.lower() == 'list':
        for ind_donor in donor_db:
            print(ind_donor[0])
        thank_you()
    elif user_input.lower() == 'e':
        return
    else:
        donation = int(input("Please enter a donation amount: "))
        for ind_donor in donor_db:
            if ind_donor[0] == user_input:
                ind_donor.append(donation)
                print("Appending the amount of {0} to {1}'s file...".format(donation, ind_donor[0]))
                print("Printing thank you email...")
                print("Dear {0}:".format(ind_donor[0]))
                print("\nThank you for your donation of {0}, and thank you for your continuing support!".format(donation))
                print("Your generous contributions are essential for our charity to continue operating.")
                print("\nRegards\nJonathan Mauk")


def report():
    print('l')


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
