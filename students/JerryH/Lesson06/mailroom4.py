#!/usr/bin/env python3
from collections import defaultdict

# List of sample donors and donations
donors = defaultdict(list, {
    "Bill Gates": [234.22, 45645.24, 43953.09, 98823],
    'Jeff Bezo': [4564.23],
    'Mike Dell': [299.09, 26273.67],
    'Harry Potter': [8234.09, 83948.04, 7834.23],
    'Ben Williams': [29283.00, 1334.34],
    'Guy James': [93.00, 34.34]
    })

menu = {
    'op1': "Send a Thank You",
    'op2': "Create a Report",
    'op3': "Send Letters To Everyone",
    'op4': "Quit"
    }

QUIT_OPT = '4'

def prompt():
    return input("Please choose the following options:\n1) {op1}.\n2) {op2}.\n3)"
        " {op3}.\n4) {op4}\n".format(**menu))


def donor_name_prompt():
    return input("Send a Thank You - Please enter a full name or type \"list\""
        "to list the current donors:\n")


def get_all_donor_names():
    return list(donors)


def donation_prompt():
    return float(input("Please enter the donation amount:\n"))


def list_all_donor_names():
    for each_name in sorted(get_all_donor_names()):
        print("{}".format(each_name))


def send_thank_you():
    donor_name = None
    while not donor_name:
        donor_name = donor_name_prompt()
        if donor_name.lower() == "list":
            donor_name = None
            list_all_donor_names()

    donation = None
    while not donation:
        try:
            donation = donation_prompt()
        except:
            print("Not a valid number! Please enter a valid number:\n")

    # If the donnor doesn't exist in the donor dictionary - add his info
    # Using defaultdict
    donors[donor_name].append(donation)
    print("Thank You Email:  Thansk for the donation!\n\n")


def create_report():
    print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------------------\n")
    report = []  # initialize report

    # for each_name in get_all_donor_names(donors):
    #for each_donor in donors.keys():
    #    report.append([each_donor, sum(donors[each_donor]), len(donors[each_donor])])
    report = [[dk, sum(dv), len(dv)] for dk, dv in donors.items()]

    # sorting the report based on donations
    r_sorted = sorted(report, key=lambda r: r[1], reverse=True)

    # Create the report
    for donor_report in r_sorted:
        print("{:23}${:12.2f}{:10}   ${:12.2f}".format(donor_report[0],
            donor_report[1],
            donor_report[2],
            donor_report[1] / donor_report[2]))
    print("\n")


def send_letters():
    for name in donors:
        file_name = name.lower().replace(' ', '_', 3) + '.txt'
        with open(file_name, "w") as fh: # fh: file handle
            fh.write("Dear {},\n\tThank you for your very kind donations: {}\n\tIt will "
                    "be put to very good use.\n\t\tSincerely,\n\t\t\t-The Team".format(name, donors[name]))


def quit_program():
	print("Thanks for using my script! Bye!")


selection_map = {
    "1": send_thank_you,
    "2": create_report,
    "3": send_letters,
    "4": quit_program
	}


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
