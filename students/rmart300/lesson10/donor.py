

class Donor(object):

    def __init__(self, name, amount_list = (500, 100, 1000, 20)):

        try:
            name.split()[1]
        except IndexError as e:
            print('The first and last name of donor must be provided\n')
            raise
        else:
            self.first_name = name.split()[0]
            self.last_name = name.split()[1]

        self.amount_list = list(amount_list)

    @property
    def donation_total(self):
        return sum(int(v) for v in self.amount_list)

    @property
    def donation_count(self):
        return len(self.amount_list)

    @property
    def donation_average(self):
        return round(self.donation_total/self.donation_count,2)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

