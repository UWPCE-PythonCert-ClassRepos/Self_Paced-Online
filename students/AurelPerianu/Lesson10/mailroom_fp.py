#!/usr/bin/env python3

from copy import deepcopy
from functools import reduce


class Donor:

    def __init__(self, name, donations=None):
        if ' ' in name:
            self._first, self._last = name.split(' ')
        else:
            self._first = ''
            self._last = name
        self._name = name
        self._donations = donations if donations else []

    @property
    def name(self):
        return self._name

    @property
    def first_name(self):
        return self._first

    @property
    def last_name(self):
        return self._last

    @property
    def donations(self):
        return self._donations

    @property
    def full_name(self):
        return f"{self._first} {self._last}"

    def __str__(self):
        return f"{self._first} {self._last} {self._donations}"

    def __repr__(self):
        return f'Donor(\'{str(self._name)}\', {self._donations})'

    def add_donations(self, amount):
        return self._donations.append(amount)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def len_donations(self):
        return len(self._donations)

    @property
    def avg_donations(self):
        try:
            return self.total_donations / self.len_donations
        except (ValueError, ZeroDivisionError) as e:
            return self._donations

    def letter(self, amount):
        txt = """\n
            To:       {0:s}
            Subject:  Your donation of ${1:,.2f}
            Dear {0:s},\n

            Thank you for your donation of ${1:,.2f}.\n
            """
        print(txt.format(self._name, amount))

    @property
    def donor_summary(self):
        return [self._name, self.total_donations,
                self.len_donations, self.avg_donations]


class DonorsAll:
    def __init__(self, donors=None):
        self._donors = donors if donors else []

    def add_donor(self, donor):
        self._donors.append(donor)

    def _get_donor_names(self):
        return [donor.name for donor in self._donors]

    def _donation_summary(self):
        sort_rep = []
        for donor in self._donors:
            sort_rep.append(donor.donor_summary)
            sort_rep.sort(key=lambda elem: elem[1], reverse=True)
        return sort_rep

    def donor_list(self):
        for donor in self._donors:
            print(donor.name)

    def add_donation(self, x, d):
        if x not in self._get_donor_names():
            self.add_donor(Donor(x, []))
        donor = self._donors[self._get_donor_names().index(x)]
        donor.add_donations(d)
        donor.letter(d)

    def report(self):
        print("\n")
        print('Donor Name' + ' ' * 16 + '|' + ' ' * 9 + 'Total Given' + ' |'
              + ' ' * 7 + 'Num Gifts' + ' |'+' '*8+'Average Gift')
        print('-' * 26 + '|' + '-' * 21 + '|' + '-' * 17 +
              '|' + '-' * 20 + '|')
        for donor in self._donation_summary():
            print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                                 donor[0], donor[1], donor[2], donor[3]))
        print('\n')

    def report_small(self):
        print('Donor Name' + ' ' * 16 + '|' + ' ' * 9 + 'Total Given' + ' |')
        print('-'*26+'|'+'-'*21+'|')
        for donor in self._donors:
            print('{:<25s} | ${:>18,.2f} |'.format(
                             donor.name, donor.total_donations))
        print('\n')

    def write(self):
        txt = """\n
            Dear {0:s},

            Thank you for your very kind donation of ${1:,.2f}.
            It will be put to very good use.

                        Sincerely,
                            -The Team
            """
        for donor in self._donation_summary():
            file_name = donor[0] + ".txt"
            with open(file_name, 'w') as f:
                try:
                    f.write(txt.format(donor[0], donor[1]))
                    print("Generated letter for {:s}!\n".format(donor[0]))
                except(OSError, FileExistsError, IsADirectoryError,
                        PermissionError) as x:
                    print('Error trying to write', file_name, ':', x)

    def multi_amount(self, amount=0, min=0, max=999999999999):
        new_list = []
        s = 0
        for donor in self._donors:
            new_donations = list(map(lambda x: x * amount,
                                 list(filter(lambda x: x > min,
                                      list(filter(lambda x: x < max,
                                           donor.donations))))))
            new_list.append(Donor(donor.name, new_donations))
            s += sum(new_donations)
        return s, DonorsAll(new_list)


db = DonorsAll([Donor('Donor A', [3580, 34124.31, 7654]),
                Donor('Donor B', [110.55, 3500]),
                Donor('Donor C', [11000]),
                Donor('Donor D', [2233.1, 6543.74, 4567.35]),
                Donor('Donor E', [546123, 99.10, 23555, 19]),
                Donor('Donor F', [78.75, 21.75])])


challengedb = DonorsAll()


def scenarios():
    scenario_dict = {}
    i = 1
    while True:
        print("\nNew scenario:\n")
        sc = challenge()
        print("\nsummary of scenarios:\n")
        print('| ' + 'Scenario Nr' + ' ' * 3 + '|' + ' ' * 1 +
              'Multiplier Amount' + ' |' + ' ' * 8 + 'Minimum' + ' |' +
              ' ' * 8 + 'Maximum' + ' |' + ' ' * 6 + 'Total Match' + ' |')
        print('|' + '-' * 15 + '|' + '-' * 19 + '|' + '-' * 16 + '|' +
              '-' * 16 + '|' + '-' * 18 + '|')
        scenario_dict.setdefault(i, []).append(sc)
        for k, v in scenario_dict.items():
            print('|{:>14d} | ${:>16,.2f} | ${:>13,.2f} | ${:>13,.2f} |'
                  ' ${:>16,.2f}|'.format(
                   k, v[0][0], v[0][1], v[0][2], v[0][3]))
        n = str(input("\nEnter \"n\" to exit scenarios: "))
        if n.lower() != "n":
            i += 1
        else:
            break


def challenge():
    db.report_small()
    print('Multiplier value')
    d = enter_amount()
    print('\nMinimum donation value')
    min = enter_amount()
    print('\nMaximum donation value')
    max = enter_amount()
    print('\n')
    challenge_total, challengedb = db.multi_amount(d, min, max)
    challengedb.report_small()
    print('\nTotal donation after match: ${:>18,.2f} '.format(challenge_total))
    return (d, min, max, challenge_total)


def enter_amount():
    while True:
        try:
            d = float(input("\nPlease enter a numeric value: "))
            if d < 0.0:
                raise ValueError()
            else:
                break
        except ValueError:
            print("Error: Not a number, or a negative number")
    return d


def add_d():
    print('add_donation')
    while True:
        try:
            x = str(input("\nEnter a donor name: "))
            if not all(a.isalpha() or a.isspace() for a in x) or x.isspace():
                raise ValueError()
            else:
                break
        except ValueError:
            print("Error: Donor names must contain letters and spaces")
    d = enter_amount()
    db.add_donation(x, d)


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt).lower()
        try:
            if dispatch_dict[response]() == 'exit menu':
                return True
                break
        except KeyError:
            print("Error: Value not an option, try again.")
            continue


def thank_you():
    menu_selection(thank_you_prompt, thank_you_dispatch)


def quit():
    print('Good Bye!')
    return "exit menu"


main_dispatch = {
    "1": thank_you,
    "2": db.report,
    "3": db.write,
    "4": challenge,
    "5": scenarios,
    "q": quit}


thank_you_dispatch = {
    "1": add_d,
    "2": db.donor_list,
    "q": quit}


main_prompt = ("\nMain Menu\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Set a challenge\n"
               "5 - Run scenarios\n"
               "q - Quit\n")


thank_you_prompt = ("\nThank you menu:\n"
                    "1 - Add donation and send message\n"
                    "2 - Display list of current donors\n"
                    "q - Quit\n")


if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
