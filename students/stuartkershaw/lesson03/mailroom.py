#!/usr/bin/env python3

donors = [
    'Anne Hathaway', 'Geronimo Jackson', 'Dingo Dogson',
    'Leo Kottke', 'Flask McCreole', 'Piglet Norquist',
    [[4000, 6250], [150, 400, 1250], [150, 300, 100],
     [75, 125], [1000], [20, 15, 30]]
]


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


def send_thank_you():
    donor_names = donors[:-1]
    instruction = 'Please enter a full name or type \'list\' to see donors:\n'
    name_input = input(instruction)
    if name_input == 'list':
        for donor in donor_names:
            print(donor)
        send_thank_you()
    elif name_input in donor_names:
        index = donor_names.index(name_input)
        print(index)
    else:
        donors[-1].append([])
        donors.insert(len(donors)-1, name_input)
    print(donors)


def main():
    selection = get_selection()
    if selection == 'a':
        send_thank_you()
    if selection == 'c':
        quit()


if __name__ == "__main__":
    main()
