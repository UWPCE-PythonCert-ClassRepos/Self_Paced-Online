import os
import donors as d

mail = d.Group()


def more_choices():
    while True:
        name = input('\nChoose an Option: \n'
                     'e - to exit\n'
                     'list -To see a list of names, or\n'
                     'Type a name to start your thank you letter >>')
        if name == 'e':
            return
        if name == 'list':
            mail.create_list()
        else:
            print('\n''Ok, you want to write a letter for {}, '
                  'lets see what we can do.'.format(name))

            if mail.search(name) is None:
                yes_no = input('The name you entered is not in the database.'
                               'Would you like to add this name? y or n >>')
                if yes_no == 'n':
                    return

            amount = input('\n''What is the donation amount? or '
                           '\'e\' to exit >')
            if amount == 'e':
                return
            try:
                if int(amount) <= 0:
                    print('\nYou entered an invalid amount!!\n')
                    return
            except ValueError:
                print('\nYou entered an invalid amount!!\n')
                return ValueError
            else:
                print (d.Individual.thank_you(name, amount))
                mail.add(name, amount)



def column_name_width(donors_f):
    name_list = list(donors_f.keys())  # creates a list of keys
    name_wi = 11  # Establish minimum column width
    for i in name_list:
        if len(i) > name_wi:
            name_wi = (len(i))  # width of name column
    return name_wi


def column_total_width(donors_f):
    tot_wi = 12
    for name, summary in donors_f.items():
        if len(str(summary[0])) > tot_wi:
            # width of total column
            tot_wi = (len(str(summary[0]))) + 3
            # width of number of donations column
    return tot_wi


def column_average_width(donors_f):
    ave_wi = 12
    for name, summary in donors_f.items():
        if len(str(summary[2])) > ave_wi:
            # width of total column
            ave_wi = (len(str(summary[2]))) + 3
            # width of number of donations column
    return ave_wi


def column_number_width(donors_f):
    num_wi = 12
    for name, summary in donors_f.items():
        if len(str(summary[1])) > num_wi:
            # width of total column
            num_wi = (len(str(summary[1]))) + 3
            # width of number of donations column
    return num_wi


def sort_list(donors_f):
    list_sorted = sorted(donors_f, key=donors_f.__getitem__, reverse=True)
    return list_sorted


def report():
    """Return a report on all the donors"""
    donors_f = mail.summary()

    name_wi = column_name_width(donors_f)
    tot_wi = column_total_width(donors_f)
    num_wi = column_number_width(donors_f)
    ave_wi = column_average_width(donors_f)

    list_sorted = sort_list(donors_f)

    rows = []
    for key in list_sorted:
        temp = donors_f[key]
        rows.append(f"{key:{name_wi}}${temp[0]:{tot_wi}.2f}"
                    f"{temp[1]:^{num_wi}}   "
                    f"${temp[2]:>{ave_wi}.2f}")

    return rows


def print_report():
    print('\n''A summary of your donors donations:')
    donors_f = mail.summary()
    name_wi = column_name_width(donors_f)
    tot_wi = column_total_width(donors_f)
    num_wi = column_number_width(donors_f)
    ave_wi = column_average_width(donors_f)
    print(f"{'Donor Name':{name_wi}}| {'Total Given':^{tot_wi}}| "
          f"{'Num Gifts':^{num_wi}}| {'Average Gift':^{ave_wi}}")
    print(f"{'-':-^{(name_wi+tot_wi+ave_wi+num_wi+8)}}")
    rows = report()
    print('\n'.join(rows))


def letters_for_all():
    path_letters = os.getcwd()
    print(f"You chose to send letters for everyone. "
          f"The letters have been completed and you "
          f"can find them here: {path_letters}")
    donors_f = mail.summary()

    for donor, donation in donors.items():
        donation_summary = donors_f[donor]
        letter = f'Dear {donor}, thank you so much for your ' \
                 f'last contribution of ${donation[-1]:.2f}! ' \
                 f'You have contributed a total of $' \
                 f'{donation_summary[0]:.2f}, ' \
                 f'and we appreciate your support!'
        # Write the letter to a destination
        with open(donor + '.txt', 'w') as to_file:
            to_file.write(letter)


def wrong_choice():
    pass


def quit_program():
    exit()


if __name__ == '__main__':

    switch_dict = {'1': more_choices,
                   '2': print_report,
                   '3': letters_for_all,
                   '4': quit_program}
    while True:
        response = input(
            '\nChoose an Action:\n'
            '1 - Send a Thank You\n'
            '2 - Create a Report\n'

            '3 - Send letters to everyone\n'
            '4 - Quit\n'
            '>>')

        switch_dict.get(response, wrong_choice)()
