# author/student: Roy Tate (githubtater)
donor_list = [
    ['Bill', 400.254, 100, 200.232, 300],
    ['Mark', 250, 450.355],
    ['Jeff', 1000, 300000.23, 2000],
    ['Female CEO 1', 1030, 20030.171, 30, 30],
    ['Female CEO 2', 1030, 20030.355, 30, 30],
]


def donor_names():
    names = []
    for donor in donor_list:
        names.append(donor[0])
    return names

def print_list():
    print('{:*^50}'.format('DONOR LIST'))
    for donor in donor_names():
        print(donor)


def add_donation(donor_name, new_donation):
    for index, donor in enumerate(donor_list):
        if donor[0] == donor_name:
            donor_list[index].append(new_donation)

def send_thank_you():
    # Obtain the name of the donor, the contribution amount, add the donation to the list, and generate
    # a thank you email.
    email_str = '''\n
        From:     A Worthwhile Cause
        To:       {0}
        Subject:  Thank you

        Dear {0},

        We want to thank you for your recent donation of ${1:.2f}. This was
        very generous.

        Sincerely,

        The Boss
        '''
    name = input("Enter the full name of the recipient (Type 'list' to view donors. Type '1' for Main Menu):\n")
    if name == 'list':
        print_list()

    elif name == '1':
        initial_menu()

    elif name in donor_names():
        donation_amount = float(input('EXISTING: Enter the donation amount: '))
        add_donation(name, donation_amount)
        print(email_str.format(name.title(), float(donation_amount)))
    else:  # name not found in list
        donation_amount = input('NEW: Enter the donation amount: ')
        donor_list.append([name, float(donation_amount)])
        print(email_str.format(name.title(), float(donation_amount)))


    # print(email_str.format(name.title(), donation_amount))


def create_report():
    # generate a report of the current donor list, the total donation amounts, avg donation amt, and # of donations
    header = '{:<20}|{:^15}|{:^10}|{:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_len = len(header)
    dotted_line = '\n{:<20}'.format('-' * header_len)
    print(header + dotted_line)
    donor_str_fmt = '{:<20} ${:>13.2f}{:>11}    ${:>11.2f}'

    for donor in donor_list:
        name = donor[0]
        num_gifts = len(donor) - 1
        total_given = sum(donor[1:])
        avg_gift = total_given / num_gifts
        print(donor_str_fmt.format(name, total_given, num_gifts, avg_gift))

def initial_menu():
    # Request input from the user to begin
    response = input('\nSelect an option:\n'
                     '[1] Send a Thank You\n'
                     '[2] Create a Report\n'
                     '[3] Quit\n'
                     '--> ')
    return response


def main():
    # main function contains the original donor list and calls other functions.

    while True:
        response = initial_menu()

        if response == '1':
            send_thank_you()

        elif response == '2':
            create_report()

        elif response == '3':
            print('\nExiting the Mailroom.')
            break
        else:
            print('Invalid Response.')


if __name__ == "__main__":
    main()