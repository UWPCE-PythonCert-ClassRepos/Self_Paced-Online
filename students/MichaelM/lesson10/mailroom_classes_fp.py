import os

"""
# Generating a thank you letter to a donor only requires knowledge of that one donor – so that code belongs in the Donor class
"""


class Donor:
    def __init__(self, first=None, last=None):
        self._first = first
        self._last = last
        self._name = f"{first} {last}".title()

    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, first):
        self._first = first

    @property
    def last(self):
        return self._last
    @last.setter
    def last(self, last):
        self._last = last

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def format_dollars(self, donation):
        results = "${:,.2f}".format(donation)
        return results

    def donor_letters(self, letter_type, donor, donation_amt=0.0, total_amt_donated=0.0):
        letter = ""
        total_donation = self.format_dollars(total_amt_donated)
        donation = self.format_dollars(donation_amt)
        if letter_type == "all_donors":
            letter = f"{donor}, warm seasons greetings,\n" \
                     f"Once again our society looks back upon this year's generosity from our many donors.\n" \
                     f"Our records show to date your generosity of {total_donation} has been among the most generous." \
                     f"We hope to continue our relationship into the next year and beyond.\n" \
                     f"\n" \
                     f"Kind regards,\n" \
                     f"The Minimalist Society"
        elif letter_type == "new":
            letter = f"[Subject]: Thank you for your generous donation\n" \
                     f"\n" \
                     f"[Body]: {donor},\n" \
                     f"Thank you for your generous donation. We are always grateful to greet new members of " \
                     f"our ever expanding family.\n" \
                     f"Your current and future beneficent contributions will go towards " \
                     f"administering our clients with our services.\n" \
                     f"Your initial contribution of {donation} illustrates an exceedingly benevolent nature.\n" \
                     f"\n" \
                     f"Kind regards,\n" \
                     f"The Minimalist Society\n" \
                     f"[End]"
        elif letter_type == "existing_donor":
            letter = f"[Subject]: Once again, thank you for your generous donation\n" \
                     f"\n" \
                     f"[Body]: {donor},\n" \
                     f"Thank you for your generous donation. Your beneficent contribution of {donation} will go " \
                     f"towards administering our clients with our services.\n" \
                     f"Our records show to date your generosity " \
                     f"of {total_donation} illustrates an exceedingly benevolent nature.\n" \
                     f"\n" \
                     f"Kind regards,\n" \
                     f"The Minimalist Society\n" \
                     f"[End]"
        return letter


class DonorCollection(Donor):

    def __init__(self):
        Donor.__init__(self)
        self._esteemed_donors_dict = {}
        self.esteemed_donors_headers = ["Donor Name", "Total Donation", "Number of Donations", "Ave Donation"]

        @property
        def _esteemed_donors_dict(self):
            return self._esteemed_donors_dict

    def add_donation(self, donor_name, donation_amt):
        self._esteemed_donors_dict.setdefault(donor_name, []).append(float(donation_amt))

    def distinct_donor_list(self):
        return list(self._esteemed_donors_dict.keys())

    def donor_total(self, donor_name):
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in self._esteemed_donors_dict.items()}
        total = float(esteemed_donors_dict_summed[donor_name])
        return total

    def donation_cnt(self, donor_name):
        esteemed_donors_dict_donation_cnt = {k: len(v) for (k, v) in self._esteemed_donors_dict.items()}
        total = int(esteemed_donors_dict_donation_cnt[donor_name])
        return total

    def sum_donors(self):
        summed_donor_list = []
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in self._esteemed_donors_dict.items()}
        esteemed_donors_dict_donation_cnt = {k: len(v) for (k, v) in self._esteemed_donors_dict.items()}
        for k, v in list(self._esteemed_donors_dict.items()):
            donor_sum = float(esteemed_donors_dict_summed[k])
            donation_cnt = esteemed_donors_dict_donation_cnt[k]
            donor_ave = donor_sum / donation_cnt
            summed_donor_list.append([k, donor_sum, donation_cnt, donor_ave])
        return summed_donor_list

    def print_letters(self, tmp_dir):
        d = Donor()
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in self._esteemed_donors_dict.items()}
        os.makedirs(tmp_dir, exist_ok=True)
        for k, v in esteemed_donors_dict_summed.items():
            sum_amt = float(v)
            tmp_dest_file = f"{tmp_dir}/{k}_Thank_You_Letter.txt"
            with open(tmp_dest_file, 'w') as wf:
                wf.write(d.donor_letters("all_donors", k, 0.0, sum_amt))

        # NEW FUNCTIONALITY ADDED FOR LESSON10
    def challenge(self, factor, donor, max_donation=0, min_donation=0):
        for k, v in self._esteemed_donors_dict.items():

            # filter for under a maximum prior contribution
            if k == donor and max_donation != 0:
                orig_list = list(v)
                filtered_list_using_max = list(filter(lambda x: x <= max_donation, orig_list))
                refactored_donations_max = list(map(lambda x: factor * x, filtered_list_using_max))
                return refactored_donations_max

            # filter for over a minimum prior contribution
            if k == donor and min_donation != 0:
                orig_list = list(v)
                filtered_list_using_min = list(filter(lambda x: x >= min_donation, orig_list))
                refactored_donations_min = list(map(lambda x: factor * x, filtered_list_using_min))
                return refactored_donations_min
