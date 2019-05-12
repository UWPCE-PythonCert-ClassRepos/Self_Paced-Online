"""Donor and DonorCollection Classes"""

class Donor:
    """
    Class holds the information for one donor

    Attribute:
        name (str): Name of the donor.
    """

    def __init__(self, name):
        self.name = name.title()
        self.donations = []

    def __str__(self):
        return f"Name: {self.name}\nDonations: {self.donations}"

    def __repr__(self):
        return f"Donor('{self.name}')"

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def number_of_donations(self):
        return len(self.donations)

    @property
    def sum_donations(self):
        return sum(self.donations)

    def thank_you_letter(self):
        return "".join((f'\nDear {self.name},\n\n\tThank you for your ',
                        f'donation of ${self.donations[-1]}.\n\n\t\t',
                        'Sincerely,\n\t\t-The Mailroom'))


class DonorCollection:
    """
    Contains a list of donors

    Attribute:
        *args (class): Donors in class Donor
    """

    def __init__(self, *args):
        self.donors = [*args]

    def add_donor(self, new_donor):
        return self.donors.append(new_donor)

    # Seems like this get_donor method isn't the simplest or most pythonic way to accomplish this.
    # Any comments on a better way to accomplish this would be much appreciated. Thanks.
    def get_donor(self, name):
        '''
        Method to select donor by donor name.

        :param name:  donor name string
        '''
        for x in self.donors:
            if x.name == name:
                return x

    def generate_report(self):
        report_list = ["{:<26}{}{}{}".format("Donor Name",
                                             "| Total Given ",
                                             "| Num Gifts ",
                                             "| Average Gift"),
                       "-" * 66]
        for donor in sorted(self.donors, key=lambda x: x.sum_donations, reverse=True):
            report_list.append("".join((f"{donor.name:<27}$",
                                        f"{donor.sum_donations:12.2f}",
                                        f"{donor.number_of_donations:11}  $",
                                        f"{donor.sum_donations / donor.number_of_donations:12.2f}")))
        return "\n".join(report_list)

    def generate_name_list(self):
        names = []
        for donor in self.donors:
            names.append(donor.name)
        return names
