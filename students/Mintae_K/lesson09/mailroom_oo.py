class Donor:
    """Class responsible for donor data encapsulation.
    This class will hold all the information about a single donor,
    and have attributes, properties, and methods to provide access
    to the donor-specific information that is needed."""

    def __init__(self, name, donations):
        self.name = name
        if isinstance(donations, list):
            self.donations = donations
        else:
            self.donations = [donations]

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def total(self):
        """donation total"""
        return sum(self.donations)

    @property
    def num_donations(self):
        """number of donations"""
        return len(self.donations)

    @property
    def average_don(self):
        """average of donations"""
        return (self.total / self.num_donations)

    def sending_thank(self):
        return f"\n Thank you {self.name}, for the generous donation! \n"


class DonorCollection:
    """Class responsible for donor collection data encapsulation
    This class will hold all of the donor objects, as well as methods
    to add a new donor, search for a given donor, etc.
    If you want a way to save and re-load your data,
    this class would hold that method, too."""

    def __init__(self, *args):
        """Collecting invidual donor donation data into one obj"""
        self.donors = {d.name: d for d in args}


    def add_donation(self, name, donation):
        if self.donors.get(name):
            self.donors[name].add_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)


    def create_report(self):
        s = '\n {:<20}| {:<10} | {:<10}| {:<20}'
        print(s.format('Donor Name', 'Total Given', "Num Gift",
                       "Average Gift"))
        print('-' * 60)
        rep_list = []
        for d in self.donors.values():
            rep_list.append([d.total, d.num_donations, d.name, d.average_don])
        rep_list.sort(reverse=True)
        s = '{:<20}  $ {:<10.2f}  {:^12} $ {:<20.2f}'
        for i in range(len(rep_list)):
            print(s.format(rep_list[i][2], rep_list[i][0], rep_list[i][1],
                           rep_list[i][3]))
        print(' ')


    def send_letters(self):
        for d in self.donors.values():
            s = "{}.txt".format(d.name)
            with open(s, "w+") as f:
                f.write("Dear {},".format(d.name))
                f.write("\n\n     Thank you for your very kind donation of ${:<10.2f}".format(d.total))
                f.write('\n\n     It will be put to very good use.')
                f.write('\n\n             Sincerely,')
                f.write('\n                   -The Team')


def just_quit():
        print('\n You have exited')


def handling_send_thank_user_input():
    f_name = input('Please type the Full Name or list> ')

    while f_name == 'list':
        print(' ')
        for donor_names in dc.donors.keys():
            print(donor_names)
        print(' ')
        f_name = input('Please type the Full Name or list> ')

    if dc.donors.get(f_name):
        s = 'Existing donor, please type the donation amount from {}> '
    else:
        s = 'New donor, please type the donation amount from {}> '

    while True:
        amount = input(s.format(f_name))
        try:
            checked_amount = float(amount)
            break
        except ValueError:
            print('\nValue entered is not a number. Only number allowed.\n')

    dc.add_donation(f_name, checked_amount)
    print(dc.donors[f_name].sending_thank())


def main():
    response = '0'
    # menu_prompt
    switch_func_dict = {'1': handling_send_thank_user_input,
                        '2': dc.create_report,
                        '3': dc.send_letters,
                        '4': just_quit}
    while not response == '4':
        print('Menu')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print('3. Send letters to everyone')
        print('4. Quit')
        response = input("Please type number from menu > ")
        try:
            switch_func_dict.get(response)()
        except TypeError:
            print('\n Please type a number from 1 to 4.\n')
    return response


if __name__ == "__main__":
    database = {'William Gates, III': [54842.49, 48965.25],
                'Mark Zuckerberg': [7852.25, 48652.0, 3548.0],
                'Jeff Bezos': [5486.0, 58794.02, 7412.1],
                'Paul Allen': [46872.02]}
    d1 = Donor('William Gates, III', database['William Gates, III'])
    d2 = Donor('Mark Zuckerberg', database['Mark Zuckerberg'])
    d3 = Donor('Jeff Bezos', database['Jeff Bezos'])
    d4 = Donor('Paul Allen', database['Paul Allen'])
    dc = DonorCollection(d1, d2, d3, d4)
    main()
