import sys


class Donor:

    def __init__(self, name, donations=None):
        self._name = name
        self._donations = donations if donations else []

    @property
    def name(self):
        return self._name

    @property
    def num_of_donations(self):
        return len(self._donations)

    @property
    def donation_total(self):
        donation_total = 0
        for donation in self._donations:
            donation_total += donation
        return donation_total

    @property
    def donations(self):
        return self._donations

    def add_donation(self, val):
        self._donations.append(val)

    @property
    def avg_donations(self):
        return self.donation_total / self.num_of_donations


class Donor_Records:
    donor_list = None

    def __init__(self, *args):
        self.donor_list = []
        for donor in args:
            self.donor_list.append(donor)

    def add_new_donor(self, donor):
        self.donor_list.append(donor)

    @property
    def list_donors(self):
        return [donor.name for donor in self.donor_list]

    def create_report(self):
        print("Donor Name      | Total Given |   Num Gifts  | Average Gift")
        print("------------------------------------------------------------")

        for donor in self.donor_list:
            print("{:<15} ${:>13} {:>14} ${:>13,.2f}".format(donor.name, donor.donation_total,
                                                             donor.num_of_donations,
                                                             donor.avg_donations))

    def send_letters_to_donors(self):
        for donor in self.donor_list:
            with open(str(donor.name) + '.txt', 'w') as file:
                file.write('Dear {},\n\nThank you for your very kind donation of ${}!\n\nSincerely,\n -The Team'.
                           format(donor.name, donor.donations[-1]))

if __name__ == '__main__':
    donor1 = Donor('Victor', [100, 20, 30])
    donor2 = Donor('John', [12])
    donor3 = Donor('Kevin', [91, 32])
    donor4 = Donor('Kelly', [5, 21])
    donor5 = Donor('Matt', [75, 20])
    donor6 = Donor('Josh', [31, 3])
    donor7 = Donor('Micah', [120])
    donor_list = Donor_Records(donor1, donor2, donor3, donor4, donor5, donor6, donor7)
    # initial request
    response = input('Do you want to: "Create a Report", "Send letters to everyone" or "quit"? ')

    response_func_dict = {'create a report': donor_list.create_report(),
                          'send letters to everyone': donor_list.send_letters_to_donors(),
                          'quit': sys.exit}
    while response != 'quit':
        try:
            response_func_dict[response]
        except KeyError:
            print('please input a valid response')
        response = input('Do you want to: "Send a Thank you",'
                         ' "Create a Report", "Send letters to everyone" or "quit"? ')
    else:
        response_func_dict.get(response)()
