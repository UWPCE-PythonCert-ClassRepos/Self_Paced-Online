class Donor:

    def __init__(self, name, donations):
        self.name = name
        self.donations = donations

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def num_of_gifts(self):
        return len(self.donations)

    def add_donation(self, val):
        self.donations.append(val)


class Mailroom:

    def __init__(self, donors):
        self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def get_donor(self, given_donor):
        for donor in self.donors:
            if donor.name == given_donor:
                return donor

    def send_thankyou(self, donor_name):
        donor = self.get_donor(donor_name)
        return 'Thank you {} for your generous donation of {}'.format(
            donor.name, donor.total_donations
        )

    def all_donors(self):
        return [x.name for x in self.donors]

    def list_donors(self):
        return "\n".join(self.all_donors())

    def create_report(self):
        print('{:20} | {:15} | {:10} | {:15}'.format(
            'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
        print('-'*70)
        for donor in self.donors:
            print('{:20} | {:15} | {:10} | {:15}'.format(
                donor.name, donor.total_donations,
                donor.num_of_gifts,
                donor.total_donations / donor.num_of_gifts))

    def save_report(self):
        for donor in self.donors:
            with open(donor.name+'.txt', 'w') as donorfh:
                donorfh.write(self.send_thankyou(donor.name))
