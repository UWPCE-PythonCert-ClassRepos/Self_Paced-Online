import os
import donors as d

mail = d.Group(d.Individual('Shane', [200]))


def more_choices():
    while True:
        name = input('\nChoose an Option: \n'
                     'e - to exit\n'
                     'list -To see a list of names, or\n'
                     'Type a name to start your thank you letter >>')
        if name == 'e':
            return
        if name == 'list':
            mail.print_donors()
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
                mail.add(name, float(amount))
                donor_obj = mail._donor_raw[name]
                print(donor_obj.thank_you)


def print_report():
    print(mail.report())


def letters_for_all():
    path_letters = os.getcwd()
    print(f"You chose to send letters for everyone. "
          f"The letters have been completed and you "
          f"can find them here: {path_letters}")
    mail.letters()


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
