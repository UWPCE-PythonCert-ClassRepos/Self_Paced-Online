#!/usr/bin/env python3

import pathlib
pth = pathlib.Path('./')


class Donor:

    def __init__(self, name):
        self._name = name
        self._donations = []
        self._rollup = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not val:
            raise ValueError("A Donor must have a name.")
        self._name = val

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, updated):
        self._donations = updated

    def add_donation(self, val):
        if val < 1:
            raise ValueError("A positive donation value is required.")
        self.donations.append(val)

    @property
    def rollup(self):
        return self._rollup

    @rollup.setter
    def rollup(self, val):
        if not val:
            raise ValueError("Rollup values are required.")
        self._rollup = val


class DonorList:

    def __init__(self, donors=None):
        self._donors = donors if donors else {}

    @property
    def donors(self):
        return self._donors

    def add_donor(self, name):
        donor = Donor(name)
        self.donors[donor.name] = donor

    def get_donor(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name]
        else:
            return "Donor not found."

    def get_donations(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name].donations
        else:
            return "Donor not found."

    def compose_thank_you(self, donor):
        if not donor:
            raise ValueError("Please provide a donor.")

        message_obj = {
            'donor_name': donor.name,
            'donations': sum(donor.donations)
        }
        message = 'Dear {donor_name}, thanks so much '\
                  'for your generous donations in the amount of: '\
                  '${donations}.'.format(**message_obj)
        return message

    def get_donor_names(self):
        print("\n".join([donor for donor in self.donors]))

    def generate_rollup(self):
        for donor in self.donors:
            cur_donor = self.donors[donor]
            number = len(cur_donor.donations)
            total = sum(cur_donor.donations)
            average = float(
                format(
                    sum(
                        cur_donor.donations) / len(
                            cur_donor.donations
                        ), '.2f'
                    )
                )
            cur_donor.rollup = dict(zip(('number', 'total', 'average'),
                                        (number, total, average)))

    def generate_table(self):
        if not self.donors:
            print('The list of donors is empty.')
            return
        self.generate_rollup()
        headings = ('Donor Name', 'Num Gifts', 'Total Given', 'Average Gift')
        print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
        print('{:_<65}'.format(''))
        for donor in self.donors:
            cur_donor = self.donors[donor]
            print('{:<20}'.format(cur_donor.name), ('{:<15}' * len(cur_donor.rollup))
                  .format(*cur_donor.rollup.values()))

    def generate_letters(self):
        if not self.donors:
            print('The list of donors is empty.')
            return
        self.generate_rollup()
        for donor in self.donors:
            with open(donor.replace(' ', '_') + '.txt', 'w') as outfile:
                outfile.write(self.compose_thank_you(self.donors[donor]))
        print('Letters generated: ')
        for f in pth.iterdir():
            if '.txt' in str(f):
                print(f)

    def multiply_by(self, factor):
        for donor in self.donors:
            self.donors[donor].donations = list(map(lambda x: x * factor, self.donors[donor].donations))

        newDL = DonorList(self.donors)

        print('Congratulations, donations were multiplied by {}:'.format(factor))
        newDL.generate_table()

        cli = DonorCli(newDL)
        cli.get_selection()


class DonorCli:

    def __init__(self, donorCollection):
        self._donorCollection = donorCollection

    @property
    def donorCollection(self):
        return self._donorCollection

    def set_donor(self):
        while True:
            try:
                name = input('Please enter a donor name: ')
                if not name:
                    raise ValueError
            except ValueError:
                print('Oops, name is required.')
                return
            else:
                self.donorCollection.add_donor(name)
                self.set_donation(name)
                print('{} added. Current donors: '.format(name))
                self.donorCollection.get_donor_names()
                return

    def set_donation(self, donor):
        while True:
            try:
                donation = int(input('Please enter a donation amount: '))
                if not donation > 0:
                    raise ValueError
            except ValueError:
                print('Please provide a whole number greater than zero.')
            else:
                self.donorCollection.donors[donor].add_donation(donation)
                print('${} donation received.'.format(donation))
                self.get_selection()

    def set_multiplier(self):
        while True:
            try:
                factor = int(input('Please enter a factor to multiply by: '))
                if not factor > 0:
                    raise ValueError
            except ValueError:
                print('Please provide a whole number greater than zero.')
            else:
                self.donorCollection.multiply_by(factor)

    def accept_donation(self):
        if not self.donorCollection.donors:
            print('The list of donors is empty.')
            return
        instruction = 'Please enter a full name or type \'list\' to see donors:\n'
        name_input = input(instruction)
        if name_input == 'list':
            self.donorCollection.get_donor_names()
            self.accept_donation()
        elif name_input in self.donorCollection.donors:
            self.set_donation(name_input)
        else:
            print('Donor not found.')

    def apply_selection(self, selection):
        arg_dict = {
            '1': self.set_donor,
            '2': self.accept_donation,
            '3': self.set_multiplier,
            '4': self.donorCollection.generate_table,
            '5': self.donorCollection.generate_letters,
            '6': quit
        }
        try:
            if not arg_dict.get(selection):
                raise KeyError
            arg_dict.get(selection)()
        except KeyError:
            print('Oops, invalid selection.')

    def get_selection(self):
        options = 'Please select from the menu:\n'\
                  '1) add new donor\n'\
                  '2) log donation\n'\
                  '3) multiply donations\n'\
                  '4) create a report\n'\
                  '5) send letters to everyone\n'\
                  '6) quit\n'
        while True:
            selection = input(options)
            self.apply_selection(selection)
            if selection == '2':
                self.get_selection()


def main():
    dl = DonorList()
    cli = DonorCli(dl)
    cli.get_selection()


if __name__ == "__main__":
    main()
