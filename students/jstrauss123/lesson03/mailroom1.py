#!/usr/bin/env python3

# function - send thank you
def send_thankyou(donorl):
    print("")
    # create donor_name_list
    donor_name_list = [k for k,v in donorl]
    # prompt for donor name
    full_name = input("Please provide full name of donor: ")
    print("")
    while full_name == "list":
        # print donor names
        #print(donor_name_list)
        for i,j in donorl:
            print(i)
        #prompt for donor name
        print("")
        full_name = input("Please provide full name of donor: ")
    if full_name not in donor_name_list:
        #name does not exist, add to sequence
        donorl.append((full_name, []))
    # prompt for contribution amount and add to sequence on matching name
    contrib_amt = float(input("Enter donation amount for donor: "))
    for i,j in donorl:
        if i == full_name:
            j.append(contrib_amt)
            print(donorl)
    # send thank you email
    print("Dear {}, Thank you so much for your generous contribution of ${}.".format(full_name, contrib_amt))
    print("")
    return donorl

# function - create report
def create_report():
    print("")
    sum = 0
    donor_len = len(donor_list)
    #print("donor_len = ", donor_len)
    count = 0
    while count < donor_len:
        totamt = 0
        contrib_amts = donor_list[count][1]
        count += 1
        for amt in contrib_amts:
            totamt = totamt + amt
            
        report_detail = report_detail +
    #report_detail = (donor, totamt, num_of_donations)    
    report_detail = (donor, totamt)    
    print(report_detail)
    
    #while count < len_dnr:
    #print("count is: ", count)
    #value_dnr = dnr[count][1]
    #print(type(value_dnr))
    #print(value_dnr)
    #count += 1
    #for i in value_dnr:
    #    print(type(i))
    #    print(i)
    #    sum = sum + i
    #    print(sum)    
    
    """
    # print header line
    print("{:15} |{:>15} |{:>2} |{:>15}".format("Donor Name","Total Given","Num Gifts","Average Gifts" ))
    # loop through donors and contributions and print detail line
    for donor in donor_list:
        sum = 0
        num_of_donations = 0
        #str1 = ""
        num_of_donations = len(donor)-1
        contrib_amts = donor[1:]
        for elem in contrib_amts:
            sum = sum + int(elem)
        avg_contribution_amt = sum / num_of_donations
        print("{:15} ${:>15.2f} {:>2} ${:>15.2f}".format(donor[0], sum, num_of_donations, avg_contribution_amt))
    print("")
    """    

# main
if __name__ == "__main__":
    #donor_list = [["Mickey Mouse", "100", "150", "100"], ["Minnie Mouse", "50", "50"], ["Ron Jones", "100"],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]
    # trying to use the structure described in mailroom tutorial
    donor_list = [("Mickey Mouse", [100.00, 150.00, 100.00]), ("Minnie Mouse", [50.00, 50.00]), ("Ron Jones", [100.00]), ("Donald Duck", [25.00]), ("Busy Bear", [10.00, 10.00, 10.00])]
    response = ""
    while response != "q":
        #print(donor_list)
        response = input("Please select:\n 1 to Send a Thank you \n 2 to Create a report \n or q to quit : ")
        if response == "1":
            donor_list = send_thankyou(donor_list)
            #donor_list = updated_list
        elif response == "2":
            create_report()
        elif response == "q":
            print("q selected - Good-bye")
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            

