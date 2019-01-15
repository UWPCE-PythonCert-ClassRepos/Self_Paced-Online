#!/usr/bin/env python3
"""
Victor Medina
1/12/2019
Lesson 3: String Formatting
"""
Donors = [
    ['Victor', 100, 20, 30],
    ['John', 12],
    ['Kevin', 91, 32],
    ['Kelly', 5, 21],
    ['Matt', 75, 20],
    ['Josh', 31, 3],
    ['Micah', 120]
]

response = input('Do you want to: Send a Thank you, Create a Report or quit? ')

# If response is send a thank you
if response == 'send a thank you':
    name = input("What's the name? ")
    if name == 'list':
        for donor in Donors:
            print(donor[0])
        name = input("What's the name? ")
    if any(name not in donor for donor in Donors):
        Donors.append([name])
        donor = name
    else:
        donor = name
    donation_amount = int(input('Donation Amount? '))
    for index, person in enumerate(Donors):
        if person[0] == donor:
            Donors[index].append(donation_amount)
    print(Donors)
    print('Thank you {} for your generous donation of {} dollars!'.format(donor,donation_amount))
elif response == 'create a report':
    print(Donors)