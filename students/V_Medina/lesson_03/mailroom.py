#!/usr/bin/env python3
"""
Victor Medina
1/12/2019
Lesson 3: String Formatting
"""


def send_thank_you(Donors):
    print(Donors)
    name = input("What's the name? ")
    if name == 'list':
        for donor in Donors:
            print(donor[0])
        name = input("What's the name? ")
    if any(name in donor_info for donor_info in Donors):
        donor = name
    else:
        Donors.append([name])
        donor = name

    donation_amount = int(input('Donation Amount? '))
    for index, person in enumerate(Donors):
        if person[0] == donor:
            Donors[index].append(donation_amount)
    print(Donors)
    print('Thank you {} for your generous donation of {} dollars!'.format(donor, donation_amount))
    return Donors


def create_report(Donors):
    donor_report = []
    for donor in Donors:
        donor_total = 0
        amount_count = 0
        for amount in donor:
            if type(amount) == str:
                pass
            else:
                donor_total += int(amount)
                amount_count += 1
        avg_donation = donor_total / amount_count
        donor_report.append([donor[0], donor_total, amount_count, avg_donation])
    print('Donor Name      | Total Given |   Num Gifts  | Average Gift')
    print('------------------------------------------------------------')
    for donor in donor_report:
        print('{:<15} ${:>13} {:>14} ${:>13,.2f}'.format(*donor))
    return None


if __name__ == "__main__":
    Donors = [
        ['Victor', 100, 20, 30],
        ['John', 12],
        ['Kevin', 91, 32],
        ['Kelly', 5, 21],
        ['Matt', 75, 20],
        ['Josh', 31, 3],
        ['Micah', 120]]
    # initial request
    response = input('Do you want to: "Send a Thank you", "Create a Report" or "quit"? ')
    while response.lower() != 'quit':
        # while loop to allow for multiple inquiries
        if response.lower() == 'send a thank you':
            send_thank_you(Donors)
        elif response.lower() == 'create a report':
            create_report(Donors)
        else:
            print('Wrong input')
        response = input('Do you want to: Send a Thank you, Create a Report or quit? ')
