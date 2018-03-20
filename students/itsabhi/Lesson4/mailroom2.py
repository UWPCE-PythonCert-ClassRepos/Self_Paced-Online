#! /usr/bin/env python3

def sending_thanksv2(donor_hist):

    donor = input("Type the Full Name of the donor here or type List to display current donors : ")
    if donor == "list":
                for k in donor_hist:
                    print(k)
                donor = input("Type the Full Name of the donor here: ")
    if donor in donor_hist.keys():
        amount = input("Enter Donation value: ")
        donation_hist = donor_hist.get(donor)
        donor_hist[donor] = (donation_hist + [int(amount)])
    else:
        amount = input("Enter Donation value: ")
        donor_hist.update({donor: [int(amount)]}) #Convert donation value from string to integer
    send_to = {"name": donor, "charity": int(amount)}
    print("Hello {name}, Just wanted to drop a note of thanks for your recent donation of ${charity}.".format(**send_to))
    return True

def second_integer(donor_summary_list):
    return donor_summary_list[1]


def create_report(donor_hist):
    donor_summary = []
    print("{:20s} | {:10s} | {:10s} | {:10s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for entry in donor_hist:
        count = len(donor_hist[entry])
        donor = entry
        total = sum(donor_hist[entry])
        average = total/count
        donor_single = [donor, total, count, average]
        donor_summary = donor_summary + [donor_single]

    donor_summary.sort(key=second_integer, reverse=True)  #Sort key based on 2nd element of the list in descending order
    for item in donor_summary:
        print("{:20s} $ {:>10d}   {:>10d} $ {:>.2f}".format(item[0], item[1], item[2], item[3]))
    return True


def sending_letters(donor_hist):
    for k in donor_hist:
        fh = open(k + ".txt", "w")
        fh.write("Hello {}, \nJust wanted to drop a note of thanks for your recent donation of ${}.\n".format(k, donor_hist[k][-1])) #Includes the last donation amount, which is the last element of list of each dict value
        fh.writelines(["It will be put to very good use.\n\n", "Sincerely,\n\n", "The Team\n"]) # Example of writelines
        fh.close()
    return True


def quitting(donors):
    print("Quitting...")
    return False

def main():
    donors_dict = {'Bill Gates': [100000, 60000, 200000], 'Jeff Bezos': [20000, 40000], 'Paul Allen': [5000], 'Mark Zuckerberg': [1000000], 'Howard Schultz': [25000]}

    switch_func_dict = {'1': sending_thanksv2,
                        '2': create_report,
                        '3': sending_letters,
                        '4': quitting
                        }
    while True:
        option = input("Enter 1 to Send a Thank You!, 2 to Create a Report or 3 to Send TY Letters or 4 to Quit: ")
        if not switch_func_dict.get(option)(donors_dict): #if this doesn't return True then break out of while loop
            break

if __name__ == '__main__':
    main()
