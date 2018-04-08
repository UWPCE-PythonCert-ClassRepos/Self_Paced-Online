#!/usr/bin/env python3

#Lesson 03: Mailroom
#Natalie Rodriguez
#3.18.2018

#list of donors and the amounts donated
donors = [['Luke Rodriguez', 12.75, 50.31, 42.59], ['Emma Burgess', 390.87, 30.00], ['Greg Cayetano', 875.60, 1120.00],
          ['Hannah Watson', 20.58, 1120.14], ['Emily Connor', 10.00], ['Catherine Davis', 400.00],
          ['River Tails', 63.56, 1200.00, 300.65], ['Virginia Ferdinand', 350.35, 5000.00], ['Joseph Kibson', 3498.00, 5.50],]

def thank_you():
    print("\nPlease enter the name of the donor you would like to thank,\nenter a new name, or enter 'list' for current donors.\nEnter '3' to return to the MAILROOM MENU.")
    answer = input()

    if answer == "list":
        for donor_total in donors:
            print(donor_total[0])
        thank_you()

    elif answer == '3':
        return
    else:
        print("Enter the amount donated:")
        amount = input()

        cur = [answer, float(amount)]
        for donor_total in donors:
            if cur[0] == donor_total[0]:
                donor_total.append(cur[1])
                break
        else:
            donors.append(cur)
        thank_you_note = "\nDear {name},\nThank you for your donation of ${amount:.2f}. This will go a long way in helping with land restoration activities.".format(name=cur[0], amount=cur[1])

        print(thank_you_note)
        print("We are extremely appreciative of your contribution and your dedication to saving the environment.")
        print("Sincerely,\nThe Nature Conservancy"'\n')


def get_total(donor_data):
    return donor_data[1]


def create_report():
    info = str()
    info += "    Donor Name     |   Total Given   | Number of Gifts |   Average Gift   "
    info += "\n"
    info += "_________________________________________________________________________"
    info += "\n"
    
    
    donor_list = list()
    for donor_data in donors:
        gift_amount = [donor_data[0], 0, 0, 0]
        for donation in donor_data[1:]:
            gift_amount[1] += donation
            gift_amount[2] += 1
        gift_amount[3] = gift_amount[1] / gift_amount[2]
        donor_list.append(gift_amount)

    # Sort the list by total amount given
    donor_list.sort(key=get_total, reverse=True)

    # Define the formatter
    line_format = "{name:<18}  |   {total:>10.2f}    | {num:>8d}        | {avg:>10.2f}\n".format
    for d in donor_list:
        info += line_format(name=d[0], total=d[1], num=d[2], avg=d[3])

    print("\n", info)


if __name__ == "__main__":
    # this will only run if run as a script.
    response = 0
    while response != "3":
        print("------MAILROOM MENU------\nWhat would you like to do?\nWrite a Thank You Note(1), Create a Report(2) or Quit(3)?"'\n')
        response = input()
        if response == "1":
            thank_you()
        if response == "2":
            create_report()