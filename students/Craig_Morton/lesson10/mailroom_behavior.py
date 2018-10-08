# ------------------------------------------------- #
# Title: Lesson 9, mail room 5.2 behavior
# Dev:   Craig Morton
# Date:  9/29/2018
# Change Log: CraigM, 9/29/2018, mail room 5.2 behavior
# ------------------------------------------------- #

import mailroom_data


def send_thank_you(db, firstname, lastname, amount):
    """Generates thank you letter"""
    db.add_donation(firstname, lastname, amount)
    return "Thank you {fn} {ln} for your generous donation of ${amount:.2f}".format(
        fn=firstname, ln=lastname, amount=amount)


def create_report(db):
    """Generates a report of all donors"""

    def get_total(donor_data):
        """Donor total"""
        return donor_data[1]

    def create_row(donor):
        """Create new row"""
        fullname = donor.get_name()
        total = sum(donor.get_donations())
        num = len(donor.get_donations())
        avg = total / num
        return [fullname, total, num, avg]
    report = list()
    report.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
    report.append("--------------------------------------------------------")
    data_list = [create_row(donor) for donor in db.get_donors()]
    data_list.sort(key=get_total, reverse=True)
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format
    for d in data_list:
        report.append(line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3]))
    return '\n'.join(report)


def send_letters(db, template_in):
    """Generates letters for all donors"""
    donor_template = template_in
    donor_template = donor_template.replace('{amount}', '{amount:.2f}')
    donor_template = donor_template.replace('{total}', '{total:.2f}')
    letters = list()
    for donor in db.get_donors():
        donations = donor.get_donations()
        last = donations[-1]
        total = sum(donations)
        try:
            letters.append(
                (donor.get_name(),
                 donor_template.format(name=donor.get_name(), amount=last, total=total)))
        except KeyError as kerr:
            print("Key Error:", kerr, "is not a valid key.",
                  "The only valid keys are: ",
                  "{name}, {amount}, and {total}")
            return "Error!"
    return letters


def challenge_project(db, above=0, below=0, multiplier=1):
    """Donation multiplier"""
    new_db = mailroom_data.DonorCapture()
    for donor in db.get_donors():
        if above > 0:
            donations_list = filter(lambda d: d > above, donor.get_donations())
        elif below > 0:
            donations_list = filter(lambda d: d < below, donor.get_donations())
        else:
            donations_list = donor.get_donations()
        for donation in map(lambda d: d * multiplier, donations_list):
            name = donor.get_key()
            new_db.add_donation(name[0], name[1], donation)
    return_list = list()
    return_list.append("\nPrevious donor list:")
    return_list.append(create_report(db))
    return_list.append("\nProjected donor list:")
    return_list.append(create_report(new_db))
    return_list.append('\n')
    return '\n'.join(return_list)
