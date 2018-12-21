#!/usr/bin/env python3

# function - send thank you
#def send_thankyou(donorl):
def send_thankyou():
    print("")
    # create donor_name_list
    donor_name_list = [k for k,v in donor_list]
    # prompt for donor name
    full_name = input("Please provide full name of donor or enter list to see all donors: ")
    print("")
    while full_name == "list":
        # print donor names
        for donor_name, _ in donor_list:
            print(donor_name)
        #prompt for donor name
        print("")
        full_name = input("Please provide full name of donor: ")
    if full_name not in donor_name_list:
        #name does not exist, add to sequence
        donor_list.append((full_name, []))
    # prompt for contribution amount and add to sequence on matching name
    contrib_amt = float(input("Enter donation amount for donor: "))
    for i,j in donor_list:
        if i == full_name:
            j.append(contrib_amt)
    # send thank you email
    print("Dear {}, Thank you so much for your generous contribution of ${}.".format(full_name, contrib_amt))
    print("")
    

# function - create report
def create_report():
    print("")
    sum = 0
    report_detail = []
    count = 0
    while count < len(donor_list):
        totamt = 0
        contrib_amts = donor_list[count][1]
        num_of_contributions = len(contrib_amts)
        for amt in contrib_amts:
            totamt = totamt + amt
        donor_name = donor_list[count][0]
        avg_contribution_amt = totamt // num_of_contributions
        donor_detail = (donor_name, totamt, num_of_contributions, avg_contribution_amt)
        report_detail.append(donor_detail)
        count += 1
    # sort by donor with largest contribution    
    def sort_key(print_detail):
        return print_detail[1]
    report_detail = sorted(report_detail, key=sort_key, reverse=True)
    #print report header
    print("{:15} |{:>15} |{:>2} |{:>15}".format("Donor Name","Total Given","Num Gifts","Average Gifts" ))
    # loop through donors and print detail lines
    i = 0
    while i < len(report_detail):
        print("{:15} ${:>15.2f} {:>2} ${:>15.2f}".format(report_detail[i][0], report_detail[i][1], report_detail[i][2], report_detail[i][3]))
        i += 1
    print("")
# main
if __name__ == "__main__":
    #donor_list = [["Mickey Mouse", "100", "150", "100"], ["Minnie Mouse", "50", "50"], ["Ron Jones", "100"],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]
    # trying to use the structure described in mailroom tutorial
    donor_list = [("Mickey Mouse", [100.00, 150.00, 100.00]), ("Minnie Mouse", [50.00, 50.00]), ("Ron Jones", [100.00]), ("Donald Duck", [25.00]), ("Busy Bear", [250.00, 10.00, 10.00])]
    response = ""
    while response != "q":
        #print(donor_list)
        response = input("Please select:\n 1 to Send a Thank you \n 2 to Create a report \n or q to quit : ")
        if response == "1":
            #donor_list = send_thankyou(donor_list)
            send_thankyou()
            #donor_list = updated_list
        elif response == "2":
            create_report()
        elif response == "q":
            print("q selected - Good-bye")
       
            

