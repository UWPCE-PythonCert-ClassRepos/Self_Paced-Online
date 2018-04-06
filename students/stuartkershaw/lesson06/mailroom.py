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
        '1': send_thank_you,
        '2': show_donor_table,
        '3': generate_letters,
        '4': quit
    }
    try:
        if not arg_dict.get(selection):
            raise KeyError
        arg_dict.get(selection)()
    except KeyError:
        print('Oops, invalid selection.')


def get_selection():
    options = 'Please select 1, 2, 3, or 4:\n'\
              '1) send a thank you\n'\
              '2) create a report\n'\
              '3) send letters to everyone\n'\
              '4) quit\n'
    while True:
        selection = input(options)
        apply_selection(selection)
        if selection == '2':
            get_selection()


def set_donation(donor):
    while True:
        try:
            donation = int(input('Please enter a donation amount: '))
            if not donation > 0:
                raise ValueError
        except ValueError:
            print('Please provide a whole number greater than zero.')
        else:
            if 'donations' in donors[donor]:
                donors[donor]['donations'].append(donation)
            else:
                donors[donor]['donations'] = [donation]
            print(compose_email(donor))
            get_selection()


def list_donors():
    for name in donors:
        print(name)


def send_thank_you():
    instruction = 'Please enter a full name or type \'list\' to see donors:\n'
    name_input = input(instruction)
    if name_input == 'list':
        list_donors()
        send_thank_you()
    elif name_input in donors:
        set_donation(name_input)
    else:
        donors[name_input] = {}
        set_donation(name_input)


def generate_rollup():
    for donor in donors:
        cur_donor = donors[donor]
        number = len(cur_donor['donations'])
        total = sum(cur_donor['donations'])
        average = float(
            format(
                sum(
                    cur_donor['donations']) / len(
                        cur_donor['donations']
                    ), '.2f'
                )
            )
        cur_donor['rollup'] = dict(zip(('number', 'total', 'average'),
                                       (number, total, average)))


def show_donor_table():
    generate_rollup()
    headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
    print('{:_<65}'.format(''))
    for donor in donors:
        cur_donor = donors[donor]
        print('{:<20}'.format(donor), ('{:<15}' * len(cur_donor['rollup']))
              .format(*cur_donor['rollup'].values()))


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
