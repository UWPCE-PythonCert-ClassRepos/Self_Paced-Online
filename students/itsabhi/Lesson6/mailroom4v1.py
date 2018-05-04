#! /usr/bin/env python3


def list_of_donors(donor_hist):
    donor_list = []
    for k in donor_hist:
        donor_list.append(k)
    return (donor_list)


def sending_thanksv2(donor_hist):
    # If already exists, add donation amt to history, else update records as a new donor & then print thank you letter.
    donor = input("Type the Full Name of the donor here or type List to display current donors : ")
    if donor == "list":
                for k in donor_hist:
                    print(k)
                donor = input("Type the Full Name of the donor here: ")
    if donor in donor_hist.keys():
        while True:
            amount = input("Enter Donation value: ")
            donation_hist = donor_hist.get(donor)
            try:
                donor_hist[donor] = (donation_hist + [int(amount)])
            except ValueError:
                print("Invalid donation entered..")
            else:
                break
    else:
        while True:
            amount = input("Enter Donation value: ")
            try:
                donor_hist.update({donor: [int(amount)]})  #Convert donation value from string to integer
            except ValueError:
                print("Invalid donation entered..")
            else:
                break
    send_to = {"name": donor, "charity": int(amount)}
    print("Hello {name}, Just wanted to drop a note of thanks for your recent donation of ${charity}.".format(**send_to))
    return True


def second_integer(donor_summary_list):
    return donor_summary_list[1]

def create_donor_summary_list(donors_dict):
    donors_summary_list = [[k, sum(donors_dict[k]), len(donors_dict[k]), sum(donors_dict[k]) / len(donors_dict[k])]
    for k in donors_dict]
    donors_summary_list.sort(key=second_integer, reverse=True)
    return donors_summary_list

def create_report_w_comprehensions(donors_dict):
    # Create report using dict comprehensions
    print("{:20s} | {:10s} | {:10s} | {:10s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    donors_summary_list = create_donor_summary_list(donors_dict)
    print(donors_summary_list)
    for item in donors_summary_list:
        print("{:20s} $ {:>10d}   {:>10d} $ {:>.2f}".format(item[0], item[1], item[2], item[3]))
    return True


def sending_letters(donor_hist):
    for k in donor_hist:
        fh = open(k + ".txt", "w")
        fh.write("Hello {}, \nJust wanted to drop a note of thanks for your recent donation of ${}.\n".format(k, donor_hist[k][-1]))  #Includes the last donation amount, which is the last element of list of each dict value
        fh.writelines(["It will be put to very good use.\n\n", "Sincerely,\n\n", "The Team\n"])  # Example of writelines
        fh.close()
    return True


def quitting(donors):
    print("Quitting...")
    return False


def main():
    donors_dict = {
                    'Bill Gates': [100000, 60000, 200000],
                    'Jeff Bezos': [20000, 40000],
                    'Paul Allen': [5000],
                    'Mark Zuckerberg': [1000000],
                    'Howard Schultz': [25000]
                    }

    switch_func_dict = {'1': sending_thanksv2,
                        '2': create_report_w_comprehensions,
                        '3': sending_letters,
                        '4': quitting
                        }
    while True:
        option = input("Enter 1 to Send a Thank You!, 2 to Create a Report or 3 to Send TY Letters or 4 to Quit: ")
        try:
            if not switch_func_dict.get(option)(donors_dict):
                break
        except TypeError:
            print("Error: Invalid option selected...")


if __name__ == '__main__':
    main()
