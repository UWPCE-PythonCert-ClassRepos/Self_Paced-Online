

class Group:

    def __init__(self):

        self._donor_raw = {'Joe': [3, 3, 3], 'Jack': [4, 5]}

    def get_donors(self):
        return self._donor_raw

    def search(self, donor):
        if self._donor_raw.get(donor) is None:
            return
        else:
            return donor

    def add(self, donor, donation):
        self._donor_raw[donor] = [donation]


    donors = property(get_donors)

    def create_list(self):
        # This prints the list of donors
        for x in self._donor_raw:
            print(x)

    def summary(self):
        """Create a new dictionary with Total, number of donations,
        and average donation amount"""

        donors_f = {some_name: [sum(donations), int(len(donations)),
                                sum(donations) / int(len(donations))]
                    for some_name, donations in self._donor_raw.items()}
        return donors_f


class Individual:
    def __init__(self):
        pass
    @staticmethod
    def thank_you(donor, donation):
        """Add a donation to a donors records and print a report."""
        return ('Thank you so much for the generous gift of ${0:.2f}, {1}!'
              .format(float(donation), donor))

# Method to add a new donor

# Method to search for a given donor


# Generate reports about multiple donors