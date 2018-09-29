

class Group:

    def __init__(self):

        self._donor_raw = {}

    def get_donors(self):
        return self._donor_raw

    donors = property(get_donors)

    def search(self, donor):
        if self._donor_raw.get(donor) is None:
            return
        else:
            return donor

    def add(self, donor, donation):
        if self.search(donor) is None:
            self._donor_raw[donor] = [donation]
        else:
            self._donor_raw[donor].append(donation)

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

    @staticmethod
    def column_name_width(donor_summary):
        name_list = list(donor_summary.keys())  # creates a list of keys
        name_wi = 11  # Establish minimum column width
        for i in name_list:
            if len(i) > name_wi:
                name_wi = (len(i))  # width of name column
        return name_wi

    @staticmethod
    def column_total_width(donor_summary):
        tot_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[0])) > tot_wi:
                # width of total column
                tot_wi = (len(str(summary[0]))) + 3
                # width of number of donations column
        return tot_wi

    @staticmethod
    def column_average_width(donor_summary):
        ave_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[2])) > ave_wi:
                # width of total column
                ave_wi = (len(str(summary[2]))) + 3
                # width of number of donations column
        return ave_wi

    @staticmethod
    def column_number_width(donor_summary):
        num_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[1])) > num_wi:
                # width of total column
                num_wi = (len(str(summary[1]))) + 3
                # width of number of donations column
        return num_wi

    @staticmethod
    def sort_list(donor_summary):
        list_sorted = sorted(donor_summary, key=donor_summary.__getitem__, reverse=True)
        return list_sorted

    def make_report(self):
        """Return a report on all the donors"""
        donor_summary = self.summary()
        name_wi = Group.column_name_width(donor_summary)
        tot_wi = Group.column_total_width(donor_summary)
        num_wi = Group.column_number_width(donor_summary)
        ave_wi = Group.column_average_width(donor_summary)

        list_sorted = Group.sort_list(donor_summary)

        rows = ['\n''A summary of your donors donations:',
                f"{'Donor Name':{name_wi}}| {'Total Given':^{tot_wi}}| "
                f"{'Num Gifts':^{num_wi}}| {'Average Gift':^{ave_wi}}",
                f"{'-':-^{(name_wi+tot_wi+ave_wi+num_wi+8)}}"]

        for key in list_sorted:
            temp = donor_summary[key]
            rows.append(f"{key:{name_wi}}${temp[0]:{tot_wi}.2f}"
                        f"{temp[1]:^{num_wi}}   "
                        f"${temp[2]:>{ave_wi}.2f}")

        return '\n'.join(rows)

    report = property(make_report)

    def letters(self):
        donors_f = self.summary()

        for donor, donation in self._donor_raw.items():
            donation_summary = donors_f[donor]
            letter = f'Dear {donor}, thank you so much for your ' \
                     f'last contribution of ${donation[-1]:.2f}! ' \
                     f'You have contributed a total of $' \
                     f'{donation_summary[0]:.2f}, ' \
                     f'and we appreciate your support!'
            # Write the letter to a destination
            with open(donor + '.txt', 'w') as to_file:
                to_file.write(letter)


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