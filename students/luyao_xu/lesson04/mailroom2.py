#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
don_1 = {'name': 'Amy Walker', 'donation amount': [18900.90, 4500]}
don_2 = {'name': 'Peter Thomson', 'donation amount': [9999.99, 500, 6000.88]}
don_3 = {'name': 'July Jensen', 'donation amount': [5300.00, 200]}
don_4 = {'name': 'Paul Allen', 'donation amount': [320.57]}
don_5 = {'name': 'Jenny Palmer', 'donation amount': [66.89]}
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
            print('Dear {}, we want to thank you for your total donation amount of ${}. Have a nice day!'
                  .format(donor[0], sum(donor[1:])))
            break
    return donor


def send_thank():
    while True:
        # If the user types ‘list’, show them a list of the donor names and re-prompt

        user_input = input('Please enter a full name, type "list" to see the list of donors, type "back" to go back: ')
        if user_input.lower() == 'list':
            for name in donations:
                print(name['name'])
            continue

        elif user_input.lower() == 'back':
            # back to the main menu
            return
        # If the user types a name in the list, use it.
        elif user_input.lower() in [d['name'].lower() for d in donations]:
            for d in donations:
                if d['name'] == user_input:
                    donate(d)
                    # exit for loop on name match
                    break
        else:
            # If the user types a name not in the list, add that name to the data structure and use it
            d = [user_input]
            donations.append(donate(d))
            break


def sort_total_given(k):
    return sum(k['donation amount'])


def create_report():
    donations.sort(key=sort_total_given, reverse=True)
    #  print a list of your donors, sorted by total historical donation amount
    head = '{:<26} | {:^11} | {:^8} | {:>12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

    print(head)
    print('-' * len(head))
    for i in donations:
        name = i['name']
        total_donation = sum(i['donation amount'])
        gift_number = len(i['donation amount'])
        average_donation = total_donation / gift_number

        print('{:<27} ${:>11.2f} {:>12} ${:>13.2f}'.format(name, total_donation, gift_number, average_donation))


def send_to_everyone():
    letter = 'Dear {}, we want to thank you for your total donation amount of ${}. Have a nice day!'
    for donation in donations:
        with open(donation['name'] + '.txt', 'w') as outfile:
            outfile.write(letter.format(donation['name'], sum(donation['donation amount'])))


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        result = dispatch_dict[response]()
        if result == "exit":
            break


# quote menu function
def quit_program():
    print('Bye.')
    return "exit"


if __name__ == "__main__":
    main_prompt = ("Please choose one of the actions in menu:\n1. Send a Thank you.\n2. Create a report.\n"
                   "3. Send thank you letter to everyone.\n4. Quit.\nEnter the number of the action you want to make: ")

    main_dispatch = {'1': send_thank,
                     '2': create_report,
                     '3': send_to_everyone,
                     '4': quit_program}
    menu_selection(main_prompt, main_dispatch)
