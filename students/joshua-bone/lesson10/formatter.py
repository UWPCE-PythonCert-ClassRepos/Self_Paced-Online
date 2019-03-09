# Joshua Bone - UW Python 210 - Lesson 10
# 03/08/2019
# Assignment: Functional Mailroom

TY_LETTER = ("Dear {full_name},\n",
             "\tThank you for your very kind donation{s} of {amounts}.\n",
             "\t{it_they} will be put to very good use.\n",
             "\t\tSincerely,",
             "\t\t\t-The Team\n")

NUM_FORMAT_WIDTH = 13


class Formatter:
    def __init__(self, donors):
        self.donors = donors

    def report_header(self, *, width=NUM_FORMAT_WIDTH):
        max_len = 5 + max((len(d) for d in self.donors.names))
        return (f"{'Donor Name': <{max_len}}|" +
                f"{'Total Given': >{width}} |" +
                f"{'Num Gifts': >{width}} |" +
                f"{'Average Gift': >{width}}")

    def dollar_string(self, amt):
        return f"${amt:.2f}"

    def sorted_report_body(self, *, width=NUM_FORMAT_WIDTH):
        max_len = 5 + max((len(d) for d in self.donors.names))
        unsorted_list = []
        for donor in self.donors.get_all():
            output = (f"{donor.name:<{max_len}}|" +
                      f"{self.dollar_string(donor.total_amt):>{width}} |" +
                      f"{str(donor.num_donations):>{width}} |" +
                      f"{self.dollar_string(donor.avg_donation):>{width}}")
            unsorted_list.append((donor.total_amt, output))
        # Sort by total donations, descending.
        return list(map(lambda t: t[1],
                    sorted(unsorted_list, key=lambda t: t[0], reverse=True)))

    def format_amts(self, amts):
        fmt = "${:.2f}"
        string = ", and ".join([fmt.format(amt) for amt in amts])
        return string.replace("and ", "", len(amts) - 2)

    def format_ty(self, name, amts, *, letter=TY_LETTER):
        d = {
            "full_name": name,
            "amounts": self.format_amts(amts),
            "it_they": "They" if len(amts) > 1 else "It",
            "s": "s" if len(amts) > 1 else ""
        }
        return [line.format(**d) for line in letter]
