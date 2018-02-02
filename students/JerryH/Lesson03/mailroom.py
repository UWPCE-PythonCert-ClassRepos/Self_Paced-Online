#!/usr/bin/env python3

# List of sample donors and donations
donors = [
    ['Bill Gates', [234.22, 45645.24, 43953.09, 98823]],
    ['Jeff Bezo', [4564.23]],
    ['Mike Dell', [299.09, 26273.67]],
    ['Harry Potter', [8234.09, 83948.04, 7834.23]],
    ['Ben Williams', [29283.00, 1334.34]],
    ['Guy James', [93.00, 34.34]]
    ]

THANK_YOU_OPT, REPORT_OPT, QUIT_OPT = (1, 2, 3)


def prompt():
    return int(input("Please choose the following options:"
        "\n1) Send a Thank You.\n2) Create a Report.\n3) Quit.\n"))


def donor_name_prompt():
    return input("Send a Thank You - Please enter a full name or type \"list\""
        "to list the current donors:\n")


def get_all_donor_names(donor_list):
    all_names = []
    for i in range(len(donor_list)):
        all_names.append(donor_list[i][0])
    return all_names


def list_all_donor_names(donor_list):
    for each_name in sorted(get_all_donor_names(donor_list)):
        print("{}".format(each_name))


def main(op=0):
    while op > 3 or op < 1:
        op = prompt()

        if op == THANK_YOU_OPT:  # Append or list donors
            donor_name = None
            while not donor_name:
                donor_name = donor_name_prompt()
                if donor_name.lower() == "list":
                    donor_name = None
                    list_all_donor_names(donors)
            # print(donor_name)
            donation = float(input("Please enter the donation amount:\n"))
            # donors.append([donor_name, donation])
            if donor_name not in get_all_donor_names(donors):
                # print(donors)
                donors.append([donor_name, [donation]])
            else:
                # print(get_all_donor_names(donors).index(donor_name))
                donors[get_all_donor_names(donors).index(donor_name)][1].append(donation)
            print("Thank You Email:  Thansk for the donation!\n\n")
            main()
        elif op == REPORT_OPT:  # Create report
            print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
            print("---------------------------------------------------------------\n")
            report = []  # initialize report

            # for each_name in get_all_donor_names(donors):
            for each_donor in donors:
                total_donation = 0  # initialize total donation from the same donor
                # Get total donation from each donor
                for i in range(len(each_donor[1])):
                    total_donation += each_donor[1][i]
                report.append([each_donor[0], total_donation, len(each_donor[1])])

            # sorting the report based on donations
            r_sorted = sorted(report, key=lambda r: r[1], reverse=True)

            # Create the report
            for d in range(len(r_sorted)):
                print("{:23}${:12.2f}{:10}   ${:12.2f}".format(r_sorted[d][0],
                    r_sorted[d][1],
                    r_sorted[d][2],
                    r_sorted[d][1]/r_sorted[d][2]))

            print("\n")
            main()

        elif op == QUIT_OPT:   # To quit the script
            print("Thanks for using my script! Bye!")


# start the script
if __name__ == "__main__":
    main()
