import os
import donors_10 as d
from functools import reduce

mail = d.Group(d.Individual('Shane', [200]), d.Individual('Joe', [1, 2, 3, 4]))


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

def run_projections():
    """Returns the matching donor's total contibution given the donation multiplier
    and optional minimum and maximum donations amounts that would be impacted by this multiplier."""
    while True:
        multiplier = input('\nStarting a new projection scenario.\n'
                           'What multiplier would you like to use \n'
                           'to match donations with? \n'
                           'e - exit\n'
                           '>>>')
        if multiplier == 'e':
            return
        try:
            if int(multiplier) < 1:
                print('\nYou entered an invalid amount!!\n')
                return
        except ValueError:
            print('\nYou entered an invalid amount!!\n')
            return ValueError

        limits = input('\nChoose an Option: \n'
                         'max - establish upper bound\n'
                         'min - establish lower bound\n'
                         'none - no max or min bounds\n'
                         'e - exit\n'
                         '>>>')
        if limits == 'e':
            return
        if limits == 'max':
            upper_bound = input('\nWhat is the maximum donation amount \n'
                                'you would like to match?\n'
                                'e - exit\n'
                                '>>>')
            if upper_bound == 'e':
                return

            else:
                donor_match = mail.challenge(int(multiplier),  max_donation= int(upper_bound))
                print(f"\nYour match contributions using a donation multiplier "
                      f"of {multiplier}\n"
                      f"will result in a total matching donation of "
                      f"${donor_match} and will result in a total donor balance of\n"
                      f"${donor_match + mail.total_donations()}")

        elif limits == 'min':
            lower_bound = input('\nWhat is the minimum donation amount \n'
                                'you would like to match?\n'
                                'e - exit\n'
                                '>>>')
            if upper_bound == 'e':
                return

            else:
                donor_match = mail.challenge(int(multiplier),  min_donation= int(lower_bound))
                print(f"\nYour match contributions using a donation multiplier "
                      f"of {multiplier}\n"
                      f"will result in a total matching donation of "
                      f"${donor_match} and will result in a total donor balance of\n"
                      f"${donor_match + mail.total_donations()}")

        elif limits == 'none':
                donor_match = mail.challenge(int(multiplier))
                print(f"\nYour match contributions using a donation multiplier "
                      f"of {multiplier}\n"
                      f"will result in your total matching donation being "
                      f"${donor_match}.\n With your help, our total donations"
                      f"will be ${donor_match + mail.total_donations()}.")

        else:
            pass




def wrong_choice():
    pass


def quit_program():
    exit()


if __name__ == '__main__':

    switch_dict = {'1': more_choices,
                   '2': print_report,
                   '3': letters_for_all,
                   '4': run_projections,
                   '5': quit_program}
    while True:
        response = input(
            '\nChoose an Action:\n'
            '1 - Send a Thank You\n'
            '2 - Create a Report\n'

            '3 - Send letters to everyone\n'
            '4 - Run Projections\n'
            '5 - Quit\n'
            '>>')

        switch_dict.get(response, wrong_choice)()
