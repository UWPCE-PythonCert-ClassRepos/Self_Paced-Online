#!/usr/bin/env python3

class Donor:

    def __init__(self, first, last, donations = None):
        self.first = first
        self.last = last
        self.donations = donations

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @property
    def total_donation(self):
        return sum(self.donations)

    def add_donation(self, amount):
        return self.donations.append(amount)

    def mult_donations(self, factor, min_donation = 1000):
        filtered_min_list = filter(lambda x: x > min_donation, self.donations)
        return list(map(lambda x: x * factor, filtered_min_list))


class DonorBook:

    def __init__(self, donors = None):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        # if donor not in self.donors:
        self.donors.append(donor)

    def get_all_donor_names(self):
        return [donor.full_name for donor in self.donors]

    def list_all_donor_names_sorted(self):
        return "\n".join(sorted(self.get_all_donor_names()))

    def send_thank_you(self):
        donor_name = None
        while not donor_name:
            donor_name = donor_name_prompt()
            if donor_name.lower() == "list":
                print(self.list_all_donor_names_sorted())
                donor_name = None

        donation = None
        while not donation:
            try:
                donation = donation_prompt()
            except ValueError:
                print("Not a valid number! Please enter a valid number:\n")

        # If the donnor doesn't exist in the donor list - add his info
        if donor_name not in self.get_all_donor_names():
            try:
                first, last = donor_name.split(" ")
                self.add_donor(Donor(first, last, [donation]))
            except ValueError:
                print("Please enter both of your \"First Name\" and \"Last Name\"")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donation(donation)

        print("Thank You Email:  Thanks for the donation!\n\n")

    def group_donations(self):
        report = []  # initialize report
        for donor in self.donors:
            report.append([donor.full_name, sum(donor.donations), len(donor.donations)])

        # Sort the report based on donations
        return sorted(report, key=lambda r: r[1], reverse=True)

    def create_report(self):
        print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
        print("---------------------------------------------------------------\n")

        # Create the report
        for donor_report in self.group_donations():
            print("{:23}${:12.2f}{:10}   ${:12.2f}".format(donor_report[0],
                donor_report[1],
                donor_report[2],
                donor_report[1] / donor_report[2]))
        print("\n")

    def challenge_report(self):
        factor = challenge_prompt()
        min_donation = min_donation_prompt()
        for donor in self.donors:
            print("{}: {}".format(donor.full_name, donor.mult_donations(factor, min_donation)))

    def send_letters(self):
        for donor in self.donors:
            file_name = donor.full_name.lower().replace(' ', '_', 3) + '.txt'
            with open(file_name, "w") as fh: # fh: file handle
                fh.write("Dear {},\n\tThank you for your very kind donations: {}\n\tIt will "
                        "be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(donor.full_name, donor.donations))

    def quit_program(self):
    	print("Thanks for using my script! Bye!")

d1 = Donor("Bill", "Gates", [234.22, 45645.24, 43953.09, 98823])
d2 = Donor("Jeff", "Bezo", [4564.23])
d3 = Donor("Mike", "Dell", [299.09, 26273.67])
d4 = Donor("Harry", "Potter", [8234.09, 83948.04, 7834.23])
d5 = Donor("Ben", "Williams", [29283.00, 1334.34])
d6 = Donor("Guy", "James", [93.00, 34.34])

db = DonorBook([d1, d2, d3, d4, d5, d6])

QUIT_OPT = '4'

selection_map = {
    "1": db.send_thank_you,
    "2": db.create_report,
    "3": db.send_letters,
    "4": db.quit_program,
    "5": db.challenge_report
	}

menu = {
    'op1': "Send a Thank You",
    'op2': "Create a Report",
    'op3': "Send Letters To Everyone",
    'op4': "Quit",
    'op5': "Challenge"
    }

def prompt():
    return input("Please choose the following options:\n1) {op1}.\n2) {op2}.\n3)"
        " {op3}.\n4) {op4}.\n5) {op5}.\n".format(**menu))


def donation_prompt():
    return float(input("Please enter the donation amount:\n"))


def donor_name_prompt():
    return input("Send a Thank You - Please enter a full name or type \"list\""
        "to list the current donors:\n")

def challenge_prompt():
    return int(input("What's your challenge factor?\n"))

def min_donation_prompt():
    return int(input("What's minimum donation you want to set? (Default is $1000)\n"))

def main():
    option_value = 0
    while option_value != QUIT_OPT:
        try:
            option_value = prompt()
            selection_map[option_value]()
        except KeyError:
            print("%s is not a valid option! Please try again.\n" % option_value)


# start the script
if __name__ == "__main__":
    main()
