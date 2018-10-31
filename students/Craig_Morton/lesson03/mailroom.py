# ------------------------------------------------- #
# Title: Lesson 3, pt 4/4, String Formatting Exercise
# Dev:   Craig Morton
# Date:  8/21/2018
# Change Log: CraigM, 8/21/2018, String Formatting Exercise
#  ------------------------------------------------ #

# !/usr/bin/env python3

donations = [["Bill", 988], ["Mark", 55, 342], ["Jeff", 120, 50, 270], ["Paul", 12, 122, 310], ["Elon", 3, 85, 100]]


def send_thank_you():
    """Thank you note and donations"""
    print("\nPlease enter a name, type 'list' for a list of donors or type 'q' to return")
    thank_you = input(":")

    if thank_you.lower() == "list":
        for donor_value in donations:
            print(donor_value[0])
        send_thank_you()
    elif thank_you.lower() == 'q':
        return
    else:
        print("Donation amount, or 'q' to return:")
        amount = input(":")
        if amount.isalpha() and amount.lower() == 'q':
            return
        amt = [thank_you, int(amount)]
        for donor_value in donations:
            if amt[0] == donor_value[0]:
                donor_value.append(amt[1])
                break
        else:
            donations.append(amt)
        thank_you_msg = "Thank you {name} for your generous donation of ${amount:.2f}".format(name=amt[0],
                                                                                              amount=amt[1])
        print(thank_you_msg)


def generate_report():
    """Donor report generation"""
    report = str()
    report += "Donor Name    | Total Given   | Num Gifts | Average Gift"
    report += "\n"
    report += "---------------------------------------------------------"
    report += "\n"
    donor_list = list()
    for donor_value in donations:
        gift_value = [donor_value[0], 0, 0, 0]
        for donation in donor_value[1:]:
            gift_value[1] += donation
            gift_value[2] += 1
            gift_value[3] = gift_value[1] / gift_value[2]
        donor_list.append(gift_value)
        donor_list.sort(key=total_value, reverse=True)
    str_format = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for i in donor_list:
        report += str_format(name=i[0], total=i[1], num=i[2], avg=i[3])
    print("\n", report)


def total_value(donor_value):
    """Total amount donated"""
    return donor_value[1]


if __name__ == "__main__":
    user_input = None
    while user_input != "3":
        print("""
Menu:
1) Send a Thank You
2) Create a Report
3) Quit""")
        user_input = input("Please choose a number:")
        if user_input == "1":
            send_thank_you()
        if user_input == "2":
            generate_report()
