#! /usr/bin/env python3


def sending_thanks(d):
    donor_hist = d
    unique_donors = []
    for entry in donor_hist:
        name = entry[0]
        if name not in unique_donors:
            unique_donors.append(name)

    donor = input("Type the Full Name of the donor here: ")
    if donor == "list":
        print(unique_donors)
        donor = input("Type the Full Name of the donor here: ")
    if donor not in unique_donors:
        donor_hist.append([donor])
        amount = input("Enter Donation value: ")
        donor_hist[-1].append([amount])
#        print(donor_hist)

    else:                       #donor appears in list of donors
        for entry in donor_hist:
            if donor == entry[0]:
                amount = input("Enter Donation value: ")
                entry[1].append(int(amount))
                continue
    #       print(donor_hist)
    print("Hello {}, Just wanted to drop a note of thanks for your recent donation of ${}.".format(donor, amount))
    return 1


def second_integer(list):
    return list[1]


def create_report(donors):
    donor_hist = donors
    donor_summary = []
    print("{:20s} | {:10s} | {:10s} | {:10s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for entry in donor_hist:
        count = len(entry[1])
        donor = entry[0]
        total = sum(entry[1])
        average = total/count
#        print("{:20s} $ {:<10d}   {:<10d} $ {:<.2f}".format(donor, total, count, average))
        donor_single = [donor, total, count, average]
        donor_summary = donor_summary + [donor_single]

    donor_summary.sort(key=second_integer, reverse=True)  #Sort key based on 2nd element of the list in descending order
#    print(donor_summary)
    for item in donor_summary:
        print("{:20s} $ {:>10d}   {:>10d} $ {:>.2f}".format(item[0], item[1], item[2], item[3]))
    return 2


def main():
    donors = [['Bill Gates', [100000, 60000, 200000]], ['Jeff Bezos', [20000, 40000]], ['Paul Allen', [50000]],
              ['Mark Zuckerberg', [1000000]], ['Howard Schultz', [25000]]]
    option = 0
    while option != 3:
        option = input("Enter 1 to Send a Thank You!, 2 to Create a Report or 3 to Quit: ")
        if option == "1":
            sending_thanks(donors)
        elif option == "2":
            create_report(donors)
        elif option == "3":
            print("Quitting...")
            break


if __name__ == '__main__':
    main()
