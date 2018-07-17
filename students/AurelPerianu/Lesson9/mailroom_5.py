#!/usr/bin/env python3


class Donor:

    def __init__(self, name, donations=None):
        if ' ' in name:
            self._first, self._last = name.split(' ')
        else:
            self._first = ''
            self._last = name
        self._name = name
        if donations:
            self._donations = donations
        else:
            self._donations = []

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
        except ValueError:
            return self._donations

    def letter(self, amount):
        txt = """\n
            To:       {0:s}
            Subject:  Your donation of ${1:,.2f}
            Dear {0:s},\n

            Thank you for your donation of ${1:,.2f}.\n
            """
        print(txt.format(self._name, amount))


class Donors_All:
    def __init__(self, donors=None):
        if donors:
            self._donors = donors
        else:
            self._donors = []

    def add_donor(self, donor):
        self._donors.append(donor)

    def _get_donor_names(self):
        return [donor.name for donor in self._donors]

    def _donation_summary(self):
        sort_rep = []
        for donor in self._donors:
            sort_rep.append([donor.name, donor.total_donations,
                             donor.len_donations, donor.avg_donations])
            sort_rep.sort(key=lambda elem: elem[1], reverse=True)
        return sort_rep

    def donor_list(self):
        """Return all donors name."""
        for donor in self._donors:
            print(donor.name)

    def add_donation(self, x, d):
        if x not in self._get_donor_names():
            self.add_donor(Donor(x, []))
        donor = self._donors[self._get_donor_names().index(x)]
        donor.add_donations(d)
        donor.letter(d)

    def report(self):
        """
        Generate the statistics for the donor list.
        """
        print("\n")
        print('Donor Name' + ' ' * 16 + '|' + ' ' * 9 + 'Total Given' + ' |'
              + ' ' * 7 + 'Num Gifts' + ' |'+' '*8+'Average Gift')
        print('-'*26+'|'+'-'*21+'|'+'-'*17+'|'+'-'*20+'|')
        for donor in self._donation_summary():
            print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                                 donor[0], donor[1], donor[2], donor[3]))
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


db = Donors_All([Donor('Donor A', [3580, 34124.31, 7654]),
                 Donor('Donor B', [110.55, 3500]),
                 Donor('Donor C', [11000]),
                 Donor('Donor D', [2233.1, 6543.74, 4567.35]),
                 Donor('Donor E', [546123, 99.10, 23555, 19]),
                 Donor('Donor F', [78.75, 21.75])])


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

    while True:
        try:
            d = float(input("\nPlease enter a donation amount: "))
            if d < 0.01:
                raise ValueError()
            else:
                break
        except ValueError:
            print("Error: Not a number, negative number, or number too small")
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
    "q": quit}


thank_you_dispatch = {
    "1": add_d,
    "2": db.donor_list,
    "q": quit}


main_prompt = ("\nMain Menu\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "q  Quit\n")


thank_you_prompt = ("\nThank you menu:\n"
                    "1 - Add donation and send message\n"
                    "2 - Display list of current donors\n"
                    "q - Quit\n")


if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
