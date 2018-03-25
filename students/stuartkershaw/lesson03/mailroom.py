#!/usr/bin/env python3

donors = [
    ['Anne Hathaway', [4000, 6250]],
    ['Geronimo Jackson', [150, 400, 1250]],
    ['Dingo Dogson', [150, 300, 100]],
    ['Leo Kottke', [75, 125]],
    ['Flask McCreole', [1000]],
    ['Piglet Norquist', [20, 15, 30]]
]


def compose_email(index):
    message = f"Dear {donors[index][0]}, thanks so much \
for your generous donation in the amount of: ${donors[index][1][-1]}."
    print(message)


def get_selection():
    options = 'Please select a, b, or c:\n\
a) send a thank you\nb) create a report\nc) quit\n'
    while True:
        try:
            selection = input(options)
            while selection not in ['a', 'b', 'c']:
                selection = input(options)
            return selection
        except ValueError:
            print(options)


def set_donation(index):
    while True:
        try:
            donation = int(input('Please enter a donation amount: '))
            while donation < 1:
                donation = int(input('Please provide a whole \
number greater than zero: '))
            donors[index][1].append(donation)
        except ValueError:
            print('Please provide a whole number greater than zero.')
            set_donation(index)
        break
    compose_email(index)


def get_donor_name():
    donor_names = []
    for donor in donors:
        donor_names.append(donor[0])
    instruction = 'Please enter a full name or type \'list\' to see donors:\n'
    name_input = input(instruction)
    if name_input == 'list':
        for name in donor_names:
            print(name)
        get_donor_name()
    elif name_input in donor_names:
        set_donation(donor_names.index(name_input))
    else:
        donors.append([name_input, []])
        donor_names.append(name_input)
        set_donation(donor_names.index(name_input))


def show_donor_table():
    for donor in donors:
        num = str(len(donor[1]))
        total = str(sum(donor[1]))
        avg = format(sum(donor[1]) / len(donor[1]), '.2f')
        donor.append([total, num, avg])

    print(donors)

    headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
    print('{:_<65}'.format(''))
    for donor in donors:
        print('{:<20}'.format(donor[0]),
                             ('{:<15}' * len(donor[2])).format(*donor[2]))


def main():
    selection = get_selection()
    if selection == 'a':
        get_donor_name()
    elif selection == 'b':
        show_donor_table()
    else:
        quit()


if __name__ == "__main__":
    main()
