# author/student: Roy Tate (githubtater)

def input_donation_amount():
    # helper function. Use to receive contribution amounts.
    donation_amount = input('Enter the donation amount: ')
    return float(donation_amount)


def send_thank_you(donor_list):
    # Obtain the name of the donor, the contribution amount, add the donation to the list, and generate
    # a thank you email.
    while True:
        name = input("Enter the full name of the recipient (Type 'list' to view donors. Type '1' for Main Menu):\n")
        if name.lower() == 'list':
            print('{:*^50}'.format('DONOR LIST'))
            for donor, amount in enumerate(donor_list):
                print(donor_list[donor][0])
        elif name == '1':
            break

        elif name.lower() == [donor_list[donor][0].lower() for donor, donations in enumerate(donor_list)]:
            # print('1name: ' + name.lower(), '   donor', donor_list[donor][0].lower())
            donation_amount = input_donation_amount()
            print(donor_list[donor])
            donor_list[donor].append(donation_amount)

        else : # name not found in list
            # print('2name: ' + name.lower(), '   donor', donor_list[donor][0].lower())
            donation_amount = input_donation_amount()
            donor_list.append([name.title(), [donation_amount]])


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

        break
    print(email_str.format(name.title(), donation_amount))



def create_report(donor_list):
    # generate a report of the current donor list, the total donation amounts, avg donation amt, and # of donations
    header = '{:<20}| {:<10} | {:<10} | {:>12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_len = len(header)
    dotted_line = '\n{:<20}'.format('-' * header_len)
    donor_str_all = ''
    donor_str_fmt = '{:<20} $ {:>10}{:>12}{:>15}\n'
    print(header + dotted_line)
    for donor, donations in enumerate(donor_list):
        num_gifts = len(donor_list[donor][1])
        donor = donor
        total_given = sum(donor_list[donor][1])

        avg_gift = sum(donor_list[donor][1]) / num_gifts
        donor_str_all += donor_str_fmt.format(donor_list[donor][0], '{:.2f}'.format(total_given), num_gifts,
                                                      '{:.2f}'.format(avg_gift))

    return donor_str_all


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
    donor_list = [
        ['Bill', [400, 100, 200.232, 300]],
        ['Mark', [250, 450.355]],
        ['Jeff', [1000, 300000, 2000]],
        ['Female CEO 1', [1030, 20030.171, 30, 30]],
        ['Female CEO 2', [1030, 20030.355, 30, 30]]
    ]
    while True:
        response = initial_menu()

        if response == '1':
            send_thank_you(donor_list)

        elif response == '2':
            print(create_report(donor_list))

        elif response == '3':
            print('\nExiting the Mailroom.')
            break
        else:
            print('Invalid Response.')


if __name__ == "__main__":
    main()
