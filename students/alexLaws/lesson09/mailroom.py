class Donor():

    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = []
        for donation in donations:
            self.donations.append(donation)

    def new_donation(self, amount):
        self.donations.append(amount)

    def write_note(self, curr_donation=0):
        note = ["Dear {},\n".format(self.name),
                "\nThank you for your generosity to our cause.\n",
                "You have now given a total of ${:,}.".format(self.tot_given),
                "\nWe greatly appreciate your contributions!"
                "\n\nThank you!\nAlex Laws"]
        if curr_donation > 0:
            curr = ("Your recent gift of ${:,} "
                    "is very helpful. ".format(curr_donation))
            note.insert(2, curr)
        return "".join(note)

    @property
    def tot_given(self):
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def avg_donation(self):
        return sum(self.donations) / len(self.donations)

    def __str__(self):
        return "{:17} ${:14,.2f} {:13} ${:13,.2f}".format(self.name,
                                                          self.tot_given,
                                                          self.num_donations,
                                                          self.avg_donation)

    def __repr__(self):
        return "Donor(\'{}\', {})".format(self.name, self.donations)

    def __lt__(self, other):
        return self.tot_given < other.tot_given

    def __gt__(self, other):
        return self.tot_given > other.tot_given

    def __eq__(self, other):
        return self.tot_given == other.tot_given

    def __ne__(self, other):
        return self.tot_given != other.tot_given


class Donor_list():

    def __init__(self, *args):
        self.donor_dictionary = []
        for arg in args:
            self.donor_dictionary.append(arg)

    def add_donor(self, *args):
        for arg in args:
            self.donor_dictionary.append(arg)

    def check_donor(self, name):
        donor_exists = False
        for donor in self.donor_dictionary:
            if name == donor.name:
                donor_exists = True
        return donor_exists

    def get_donor(self, name):
        for donor in self.donor_dictionary:
            if name == donor.name:
                return donor

    def sort_donors(self):
        return sorted(self.donor_dictionary, reverse=True)

    def donor_report(self):
        print("\nDonor Name       |  Total Given  |  Num Gifts  |  Average Gift")
        for donor in self.sort_donors():
            print(donor)

    def __str__(self):
        return "\n".join(donor.name for donor in self.donor_dictionary)
