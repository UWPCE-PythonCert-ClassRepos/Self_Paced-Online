import os

class Mailroom(object):
    esteemed_donors_headers = ["Donor Name", "Total Donation", "Number of Donations", "Ave Donation"]
    esteemed_donors_dict = {"john jacob astor": [10.0, 100.0, 1000.0, 10000.0],
                            "alan rufus, 1st lord of richmond": [10.0],
                            "henry ford": [10.0, 100.0, 1000.0],
                            "cornelius vanderbilt": [10.0],
                            "jakob fugger": [10.0, 100.0],
                            "t": [25.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0]}

    def __init__(self):
        pass


    def donor_letters(letter_type="existing_donor", donor="", donation_amt=0.0, total_amt_donated=0.0):
        total_donation = "${0:,.2f}".format(int(total_amt_donated))
        letter = ""
        if letter_type == "all_donors":
            letter = f"{donor}, warm seasons greetings,\n" \
                      f"Once again our society looks back upon this year's generousity from our many donors.\n" \
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
                      f"Your initial contribution of {donation_amt} illustrates an exceedingly benevolent nature.\n" \
                      f"\n" \
                      f"Kind regards,\n" \
                      f"The Minimalist Society\n" \
                      f"[End]"
        elif letter_type == "existing_donor":
            letter = f"[Subject]: Once again, thank you for your generous donation\n" \
                      f"\n" \
                      f"[Body]: {donor},\n" \
                      f"Thank you for your generous donation. Your beneficent contribution of {donation_amt} will go " \
                      f"towards administering our clients with our services.\n" \
                      f"Our records show to date your generosity " \
                      f"of {total_donation} illustrates an exceedingly benevolent nature.\n" \
                      f"\n" \
                      f"Kind regards,\n" \
                      f"The Minimalist Society\n" \
                      f"[End]"
        return letter

class Donor(Mailroom):
    def __init__(self):
        pass

    @property  # donor_name getter
    def donor_name(self):
        return self.usr_name

    @donor_name.setter
    def donor_name(self, value):
        self.usr_name = value

    @property  # donation_amt getter
    def donation_amt(self):
        return self.usr_donation

    @donation_amt.setter
    def donation_amt(self, value):
        self.usr_donation = value

    def donor_total(self, donor_name):
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in Mailroom.esteemed_donors_dict.items()}
        total = float(esteemed_donors_dict_summed[donor_name])
        return total

    def add_donation(self, donor_name, donation_amt):
        Mailroom.esteemed_donors_dict.setdefault(donor_name, []).append(float(donation_amt))


    # ---- NEW FUNCTIONALITY ADDED FOR LESSON10 ----
    @property  # donations_summmed getter
    def donations_summmed(self):
        return self.sum_total

    @donations_summmed.setter
    def donations_summmed(self, value):
        self.sum_total = value

    def challenge(self, factor, donor, max_donation=0, min_donation=0):
        for k, v in Mailroom.esteemed_donors_dict.items():

            #filter for under a maximum prior contribution
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


class Donors(Mailroom):
    def __init__(self):
        pass

    @property  # first_name getter
    def tmp_directory(self):
        return self.usr_directory

    @tmp_directory.setter
    def tmp_directory(self, value):
        self.usr_directory = value

    def sum_donors(self):
        summed_donor_list = []
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in Mailroom.esteemed_donors_dict.items()}
        esteemed_donors_dict_donation_cnt = {k: len(v) for (k, v) in Mailroom.esteemed_donors_dict.items()}
        for k, v in list(Mailroom.esteemed_donors_dict.items()):
            donor_sum = float(esteemed_donors_dict_summed[k])
            donation_cnt = esteemed_donors_dict_donation_cnt[k]
            donor_ave = donor_sum / donation_cnt
            summed_donor_list.append([k, donor_sum, donation_cnt, donor_ave])
        return summed_donor_list

    def print_letters(self, tmp_dir):
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in Mailroom.esteemed_donors_dict.items()}
        os.makedirs(tmp_dir, exist_ok=True)
        for k, v in esteemed_donors_dict_summed.items():
            sum_amt = float(v)
            tmp_dest_file = f"{tmp_dir}/{k}_Thank_You_Letter.txt"
            with open(tmp_dest_file, 'w') as wf:
                wf.write(Mailroom.donor_letters("all_donors", k, 0.0, sum_amt))




