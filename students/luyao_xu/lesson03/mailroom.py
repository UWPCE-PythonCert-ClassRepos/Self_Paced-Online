#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
"""The script that prompr the user to choose from a menu of 3 actions: "Send a Thank you",
"Create a Report" or "Quit". """

don_1 = ['Amy Walker', 18900.90, 4500]
don_2 = ['Peter Thomson', 9999.99, 500, 6000.88]
don_3 = ['July Jensen', 5300.00, 200]
don_4 = ['Paul Allen', 320.57]
don_5 = ['Jenny Palmer', 66.89]
donations = [don_1, don_2, don_3, don_4, don_5]


def donate(donor):
    # Once a name has been selected, prompt for a donation amount
    donation_amount = float(input('Enter the amount you want to donate: $'))
    donor.append(donation_amount)
    while True:
        more = input('Is there another gift amount you want to enter?(y/n) ')
        if more[0].lower() == 'y':
            donation_amount = float(input('That\'s so nice of you! Enter the amount you want to donate: $'))
            # Once an amount has been given, add that amount to the donation history of the selected user
            donor.append(donation_amount)
        # Use string formatting to compose an email thanking the donor for their generous donation.
        else:
            print('Dear {}, we want to thank you for your total donation amount of ${}. Have a nice day!'.format(donor[0], sum(donor[1:])))
            break
    return donor


def send_thank():
    while True:
        # If the user types ‘list’, show them a list of the donor names and re-prompt

        user_input = input('Please enter a full name, type "list" to see the list of donors, type "back" to go back: ')
        if user_input.lower() == 'list':
            for name in donations:
                print(f'{name[0]}')
            continue

        elif user_input.lower() == 'back':
            # back to the main menu
            return
        # If the user types a name in the list, use it.
        elif user_input.lower() in [d[0].lower() for d in donations]:
            for d in donations:
                if d[0] == user_input:
                    donate(d)
                    # exit for loop on name match
                    break
        else:
            # If the user types a name not in the list, add that name to the data structure and use it
            d = [user_input]
            donations.append(donate(d))
            break




def sort_total_given(k):
    return sum(k[1:])



def create_report():
    donations.sort(key=sort_total_given, reverse=True)
    #  print a list of your donors, sorted by total historical donation amount
    head = '{:<26} | {:^11} | {:^8} | {:>12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

    print(head)
    print('-' * len(head))
    for i in donations:
        name = i[0]
        total_donation = sum(i[1:])
        gift_number = len(i[1:])
        average_donation = total_donation / gift_number

        print('{:<27} ${:>11.2f} {:>12} ${:>13.2f}'.format(name, total_donation, gift_number, average_donation))




def create_menu():
    while True:
        print(
            'Please choose one of the actions in menu :\n' + '1. Send a Thank you.\n' + '2. Create a report.\n' + '3. Quit.')
        response = int(input('Enter the number of the action you want to make: '))
        if response == 1:
            send_thank()
        elif response == 2:
            create_report()
        elif response == 3:
            print('Bye.')
            break


if __name__ == '__main__':
    create_menu()
