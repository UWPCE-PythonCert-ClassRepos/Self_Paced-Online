#!/usr/bin/env python3

donors = {
    'Anne Hathaway': {
        'donations': [
            4000,
            6250
        ],
    },
    'Geronimo Jackson': {
        'donations': [
            150,
            400,
            1250
        ]
    },
    'Dingo Dogson': {
        'donations': [
            150,
            300,
            100
        ]
    },
    'Leo Kottke': {
        'donations': [
            75,
            125
        ]
    },
    'Flask McCreole': {
        'donations': [
            1000
        ]
    },
    'Piglet Norquist': {
        'donations': [
            20,
            15,
            30
        ]
    }
}


def compose_email(donor):
    message = f"Dear {donor}, thanks so much "\
              f"for your generous donation in the amount of: "\
              f"${donors[donor]['donations'][-1]}."
    print(message)
    get_selection()


def get_selection():
    options = 'Please select a, b, or c:\n'\
              'a) send a thank you\nb) create a report\nc) quit\n'
    while True:
        try:
            selection = input(options)
            while selection not in ['a', 'b', 'c']:
                selection = input(options)
            if selection == 'a':
                get_donor_name()
            elif selection == 'b':
                show_donor_table()
            else:
                quit()
        except ValueError:
            input(options)


def set_donation(donor):
    while True:
        try:
            donation = int(input('Please enter a donation amount: '))
            while donation < 1:
                donation = int(input('Please provide a whole '
                                     'number greater than zero: '))
            if 'donations' in donors[donor]:
                donors[donor]['donations'].append(donation)
            else:
                donors[donor]['donations'] = [donation]
        except ValueError:
            print('Please provide a whole number greater than zero.')
            set_donation(donor)
        break
    compose_email(donor)


def get_donor_name():
    instruction = 'Please enter a full name or type \'list\' to see donors:\n'
    name_input = input(instruction)
    if name_input == 'list':
        for name in donors:
            print(name)
        get_donor_name()
    elif name_input in donors:
        set_donation(name_input)
    else:
        donors[name_input] = {}
        set_donation(name_input)


def show_donor_table():
    for donor in donors:
        cur_donor = donors[donor]
        if 'rollup' not in cur_donor:
            cur_donor['rollup'] = {}
        cur_rollup = cur_donor['rollup']
        cur_rollup['number'] = len(cur_donor['donations'])
        cur_rollup['total'] = sum(cur_donor['donations'])
        cur_rollup['average'] = float(
            format(
                sum(
                    cur_donor['donations']) / len(
                        cur_donor['donations']
                    ), '.2f'
                )
            )

    headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
    print('{:_<65}'.format(''))
    for donor in donors:
        cur_donor = donors[donor]
        print('{:<20}'.format(donor), ('{:<15}' * len(cur_donor['rollup']))
              .format(*cur_donor['rollup'].values()))
    get_selection()


def main():
    get_selection()


if __name__ == "__main__":
    main()
