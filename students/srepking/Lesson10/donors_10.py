

class Group:

    def __init__(self, *args):

        self._donor_raw = {d.name: d for d in args}

    def search(self, donor):
        return self._donor_raw.get(donor)

    def add(self, donor, donation):
        if self._donor_raw.get(donor):
            self._donor_raw[donor].add_donation(donation)
        else:
            self._donor_raw[donor] = Individual(donor, [donation])

    def print_donors(self):
        # This prints the list of donors
        for x in self._donor_raw:
            print(x)

    def summary(self):
        """Create a new dictionary with Total, number of donations,
        and average donation amount"""

        donors_f = {some_name: [donor_obj.sum_donations(),
                                donor_obj.number_donations(),
                                donor_obj.avg_donations()]
                    for some_name, donor_obj in self._donor_raw.items()}
        return donors_f

    def total_donations(self):
        "Add up all of the donations made to date."
        donation_total = 0
        for some_name, donor_obj in self._donor_raw.items():
            donation_total += sum(donor_obj.donations)
        return donation_total

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
        list_sorted = sorted(donor_summary,
                             key=donor_summary.__getitem__, reverse=True)
        return list_sorted

    def report(self):
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

    def letters(self):
        for donor, donor_obj in self._donor_raw.items():
            letter = f'Dear {donor}, thank you so much for your ' \
                     f'last contribution of ${donor_obj.last_donation():.2f}! ' \
                     f'You have contributed a total of $' \
                     f'{donor_obj.sum_donations():.2f}, ' \
                     f'and we appreciate your support!'
            # Write the letter to a destination
            with open(donor + '.txt', 'w') as to_file:
                to_file.write(letter)

    def challenge(self, factor=1, min_donation = None, max_donation = None):
        """Return a list of the matching donors donations."""
        # Put together a list of all the donations in the class instance.
        donors_donations = []
        for some_name, donor_obj in self._donor_raw.items():
            donors_donations += donor_obj.donations

        # Filter out the list with min and max donation parameters.
        if min_donation is not None and max_donation is not None:
            donors_filtered = list(filter(lambda x: int(max_donation) >= x >= int(min_donation),
                                                  donors_donations))
        elif min_donation is not None:
            donors_filtered = list(filter(lambda x: x >= min_donation, donors_donations))

        elif max_donation is not None:
            donors_filtered = list(filter(lambda x: x <= int(max_donation), donors_donations))

        else:
            donors_filtered = donors_donations

        # Return the total matching donation amount.
        match_total = sum(list(map(lambda x : x*(factor-1), donors_filtered)))

        return match_total


class Individual:
    def __init__(self, name, donations):
        self.name = name
        self.donations = donations

    def add_donation(self, donation):
        self.donations.append(donation)

    def number_donations(self):
        return int(len(self.donations))

    def sum_donations(self):
        return sum(self.donations)

    def avg_donations(self):
        return self.sum_donations() / \
               self.number_donations()

    def last_donation(self):
        return self.donations[-1]

    @property
    def thank_you(self):
        """Add a donation to a donors records and print a report."""
        return ('Thank you so much for the generous gift of ${0:.2f}, {1}!'
                .format(self.donations[-1], self.name))


