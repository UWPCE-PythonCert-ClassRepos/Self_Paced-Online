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
    def donor_history(self):
        return sum(self.donations)


class DonorBook:

    def __init__(self, donors = []):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        if donor not in self.donors:
            self.donors.append(donor)

    def get_all_donor_names(self):
        for donor in self.donors:
            print("-->" + donor.full_name)

    def list_all_donor_names_sorted(self):
        all_names = ""
        for each_donor_name in sorted(self.donors):
            all_names += "{}\n".format(each_donor_name)
        return(all_names)

    @staticmethod
    def donation_prompt():
        return float(input("Please enter the donation amount:\n"))

    @staticmethod
    def donor_name_prompt():
        return input("Send a Thank You - Please enter a full name or type \"list\""
            "to list the current donors:\n")

    def send_thank_you(self):
        donor_name = None
        while not donor_name:
            donor_name = DonorBook.donor_name_prompt()
            if donor_name.lower() == "list":
                print(self.get_all_donor_names())
                donor_name = None

        donation = None
        while not donation:
            try:
                donation = self.donation_prompt()
            except ValueError:
                print("Not a valid number! Please enter a valid number:\n")

        # If the donnor doesn't exist in the donor dictionary - add his info
        # Using defaultdict
        donors[donor_name].append(donation)
        print("Thank You Email:  Thansk for the donation!\n\n")


    def create_report(self):
        pass


    def send_letters(self):
        pass


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
    "1": db.send_thank_you(),
    "2": db.create_report(),
    "3": db.send_letters(),
    "4": db.quit_program()
	}

menu = {
    'op1': "Send a Thank You",
    'op2': "Create a Report",
    'op3': "Send Letters To Everyone",
    'op4': "Quit"
    }

def prompt():
    return input("Please choose the following options:\n1) {op1}.\n2) {op2}.\n3)"
        " {op3}.\n4) {op4}\n".format(**menu))

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
