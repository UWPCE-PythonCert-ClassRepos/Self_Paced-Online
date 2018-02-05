#!/usr/bin/env python3

# List of sample donors and donations
donors = {
    "Bill Gates": [234.22, 45645.24, 43953.09, 98823],
    'Jeff Bezo': [4564.23],
    'Mike Dell': [299.09, 26273.67],
    'Harry Potter': [8234.09, 83948.04, 7834.23],
    'Ben Williams': [29283.00, 1334.34],
    'Guy James': [93.00, 34.34]
    }

options = {
    'THANK_YOU_OPT': 1,
    'REPORT_OPT': 2,
    'SEND_LETTER_OPT': 3,
    'QUIT_OPT': 4
    }

menu = {
    'op1': "Send a Thank You",
    'op2': "Create a Report",
    'op3': "Send Letters To Everyone",
    'op4': "Quit"
    }


def prompt():
    return int(input("Please choose the following options:\n1) {op1}.\n2) {op2}.\n3) {op3}.\n4) {op4}\n".format(**menu)))


def donor_name_prompt():
    return input("Send a Thank You - Please enter a full name or type \"list\""
        "to list the current donors:\n")


def get_all_donor_names():
    all_names = []
    for d in donors.keys():
        all_names.append(d)
    return all_names


def list_all_donor_names():
    for each_name in sorted(get_all_donor_names()):
        print("{}".format(each_name))


def main():
    op = 0
    while op != options['QUIT_OPT']:
        op = prompt()

        if op == options['THANK_YOU_OPT']:  # Append or list donors
            donor_name = None
            while not donor_name:
                donor_name = donor_name_prompt()
                if donor_name.lower() == "list":
                    donor_name = None
                    list_all_donor_names()
            # print(donor_name)
            donation = float(input("Please enter the donation amount:\n"))
            # If the donnor doesn't exist in the donor dictionary - add his info
            if donor_name not in get_all_donor_names():
                # print(donors)
                donors[donor_name] = [donation]
            # else append the donation into the existing donors
            else:
                donors[donor_name].append(donation)
            print("Thank You Email:  Thansk for the donation!\n\n")

        elif op == options['REPORT_OPT']:  # Create report
            print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
            print("---------------------------------------------------------------\n")
            report = []  # initialize report

            # for each_name in get_all_donor_names(donors):
            for each_donor in donors.keys():
                report.append([each_donor, sum(donors[each_donor]), len(donors[each_donor])])

            # sorting the report based on donations
            r_sorted = sorted(report, key=lambda r: r[1], reverse=True)

            # Create the report
            for d in range(len(r_sorted)):
                print("{:23}${:12.2f}{:10}   ${:12.2f}".format(r_sorted[d][0],
                    r_sorted[d][1],
                    r_sorted[d][2],
                    r_sorted[d][1]/r_sorted[d][2]))

            print("\n")

        elif op == options['SEND_LETTER_OPT']:
            print("This is option3.")

        elif op == options['QUIT_OPT']:   # To quit the script
            print("Thanks for using my script! Bye!")


# start the script
if __name__ == "__main__":
    main()
