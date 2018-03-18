#!/usr/bin/env python3

donors = [
    'Anne Hathaway', 'Geronimo Jackson', 'Dingo Dogson',
    'Leo Kottke', 'Flask McCreole', 'Piglet Norquist',
    [[4000, 6250], [150, 400, 1250], [150, 300, 100],
     [75, 125], [1000], [20, 15, 30]]
]


def compose_email(donor_list, index):
    i = index
    dl = donor_list
    message = f"Dear {dl[i]}, thanks so much \
for your generous donation in the amount of: ${dl[-1][i][-1]}."
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


def set_donation(donor_list, index):
    i = index
    dl = donor_list
    while True:
        try:
            donation = int(input('Please enter a donation amount: '))
            while donation < 1:
                donation = int(input('Please provide a whole \
number greater than zero: '))
            dl[-1][i].append(donation)
        except ValueError:
            print('Please provide a whole number greater than zero.')
            set_donation(dl, i)
        break
    compose_email(dl, i)


def get_donor_name():
    donor_names = donors[:-1]
    instruction = 'Please enter a full name or type \'list\' to see donors:\n'
    name_input = input(instruction)
    if name_input == 'list':
        for donor in donor_names:
            print(donor)
        get_donor_name()
    elif name_input in donor_names:
        set_donation(donors, donors.index(name_input))
    else:
        donors[-1].append([])
        donors.insert(len(donors)-1, name_input)
        set_donation(donors, donors.index(name_input))


def show_donor_table(donor_list):
    dl = donor_list
    donor_names = dl[:-1]
    donations = donor_list[-1]
    formatted = []
    for d in donations:
        rollup = []
        total = str(sum(d))
        rollup.append(total)
        num = str(len(d))
        rollup.append(num)
        avg = format(sum(d) / len(d), '.2f')
        rollup.append(avg)
        formatted.append(rollup)

    print(donor_names, formatted)

    headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
    print('{:_<65}'.format(''))
    for dn, d in zip(donor_names, formatted):
        print('{:<20}'.format(dn), ('{:<15}' * len(d)).format(*d))


def main():
    selection = get_selection()
    if selection == 'a':
        get_donor_name()
    elif selection == 'b':
        show_donor_table(donors)
    else:
        quit()


if __name__ == "__main__":
    main()
