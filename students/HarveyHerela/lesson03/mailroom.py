#!/usr/bin/env python3

donors = [["Chase", 25], ["Marshall", 30, 60], ["Skye", 100, 100, 100]]

def send_thank_you():
    print("\nType a name (type 'list' for a list of names in the database, 'q' to go back)")
    ty_cmd = input(":")
    
    if ty_cmd.lower() == "list":
        for donor_data in donors:
            print(donor_data[0])
        send_thank_you()
    
    elif ty_cmd.lower() == 'q':
        return
    else:
        print("Donation amount, or 'q' to go to main menu:")
        amount = input(":")
        if amount.isalpha() and amount.lower() == 'q':
            return
        cur = [ty_cmd, int(amount)]
        for donor_data in donors:
            if cur[0] == donor_data[0]:
                donor_data.append(cur[1])
                break
        else:
            donors.append(cur)
        thank_you_msg = "Thank you {name} for your generous donation of ${amount:.2f}".format(name=cur[0], amount=cur[1])
        print(thank_you_msg)

def get_total(donor_data):
    return donor_data[1]

def create_report():
    report = str()
    report += "Donor Name    | Total Given   | Num Gifts | Average Gift"
    report += "\n"
    report += "--------------------------------------------------------" 
    report += "\n"
    # Create a list with the data to be printed
    data_list = list()
    for donor_data in donors:
        gift_data = [donor_data[0], 0, 0, 0]
        for donation in donor_data[1:]:
            gift_data[1] += donation
            gift_data[2] += 1
        gift_data[3] = gift_data[1] / gift_data[2]
        data_list.append(gift_data)
    
    # Sort the list by total amount given
    data_list.sort(key=get_total, reverse=True)
    
    # Define the formatter
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for d in data_list:
        report += line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3])
    
    print("\n", report)
    
if __name__ == "__main__":
    response = 0
    while response != "3":
        print("\n\nPick an action by number:")
        print("1: Send a 'thank you' note")
        print("2: Create a report")
        print("3: Quit")
        response = input(":")
        if response == "1":
            send_thank_you()
        if response == "2":
            create_report()


    