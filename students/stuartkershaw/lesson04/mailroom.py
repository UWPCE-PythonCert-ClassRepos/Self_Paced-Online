#!/usr/bin/env python3

import pathlib
pth = pathlib.Path('./')

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
    message_obj = {
        'donor_name': donor,
        'donation': donors[donor]['donations'][-1]
    }
    message = 'Dear {donor_name}, thanks so much '\
              'for your generous donation in the amount of: '\
              '${donation}.'.format(**message_obj)
    return message


def apply_selection(selection):
    arg_dict = {
        '1': get_donor_name,
        '2': show_donor_table,
        '3': generate_letters,
        '4': quit
    }
    arg_dict.get(selection)()


def get_selection():
    options = 'Please select 1, 2, 3, or 4:\n'\
              '1) send a thank you\n'\
              '2) create a report\n'\
              '3) send letters to everyone\n'\
              '4) quit\n'
    while True:
        try:
            selection = input(options)
            while selection not in ['1', '2', '3', '4']:
                selection = input(options)
            apply_selection(selection)
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
    print(compose_email(donor))
    get_selection()


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


def generate_rollup():
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


def show_donor_table():
    generate_rollup()
    headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
    print('{:_<65}'.format(''))
    for donor in donors:
        cur_donor = donors[donor]
        print('{:<20}'.format(donor), ('{:<15}' * len(cur_donor['rollup']))
              .format(*cur_donor['rollup'].values()))
    get_selection()


def generate_letters():
    generate_rollup()
    for donor in donors:
        with open(donor.replace(' ', '_') + '.txt', 'w') as outfile:
            outfile.write(compose_email(donor))
    print('Letters generated: ')
    for f in pth.iterdir():
        if '.txt' in str(f):
            print(f)


def main():
    get_selection()


if __name__ == "__main__":
    main()
