class Donor (object):
    """Donor level class where 'don_seq' is a list of donation amounts"""
    def __init__(self, name, don_seq):
        self._donor_name = name
        self._donations = don_seq

    def __repr__(self):
        return "Donor ({},{})".format(self._donor_name, self._donations)

    @property
    def name(self):
        return self._donor_name

    @property
    def donations(self):
        return self._donations

    @property
    def total(self):
        return sum(self._donations)

    @property
    def cnt(self):
        return len(self._donations)

    @property
    def avg(self):
        return sum(self._donations)/len(self._donations)

    def __lt__(self, other):
        return self.total < other.total


class Donor_collect (object):
    """Class for a collection of Donors;'donor_list' is list of Donor objects"""
    def __init__(self, donor_list):
        self.donor_dict = {}
        for i in donor_list:
            if type(i) is not Donor:
                raise TypeError("Expected a list of 'Donor' objects")
            self.donor_dict[i.name] = i

    def new_donor(self, new_name, don_amt):
        don_seq = [don_amt]
        self.donor_dict[new_name] = Donor(new_name, don_seq)

    def update_donor(self, donor, don_amt):
        self.donor_dict[donor]._donations.append(don_amt)

    def search_donor(self, donor):
        return donor in self.donor_dict

    def get_donors(self):
        for donor in self.donor_dict:
            print(donor)

    def get_msg_vars(self, donor):
        """return donor's name, donation count, and total donation"""
        return (self.donor_dict[donor].name, self.donor_dict[donor].cnt,
                self.donor_dict[donor].total)

    def print_rpt(self):
        print('{:<20}| {:^15}| {:^10}| {:>12}'
              .format('Donor Name', 'Total Gifted', 'Num Gifts', 'Avg Gift'))
        print('-'*63)
        s = '{:<20} ${:>15}  {:^10} ${:>12.2f}'
        self.dl = []
        for i in (self.donor_dict):
            self.dl.append(self.donor_dict[i])
        sorted_dl = sorted(self.dl, reverse=True)
        for i in range(len(sorted_dl)):
            print(s.format(sorted_dl[i].name, sorted_dl[i].total,
                  sorted_dl[i].cnt, sorted_dl[i].avg))
