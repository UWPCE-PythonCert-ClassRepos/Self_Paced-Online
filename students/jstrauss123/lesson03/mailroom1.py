#!/usr/bin/env python3

# function - send thank you
def fun_sendty(donorl):
    name_list = list()
    local_donor_list = donorl
    for donor in local_donor_list:
            str1 = ""
            for elem in donor[0]:
                str1 = str1 + elem
            name_list.append(str1)
    full_name = input("Please provide full name of donor: ")
    while full_name == "list":
        name_list = list()
        for donor in local_donor_list:
            str1 = ""
            for elem in donor[0]:
                str1 = str1 + elem
            name_list.append(str1)
        print(name_list)
        full_name = input("Please provide full name of donor: ")
        
    if full_name in name_list:
        # donor exists - send thank you email
        print("Dear {}, Thank you so much for your generous contribution".format(full_name))
        print("")
    else:   # new user : add and prompt for contribution. create new list and add to donor list
        contrib_amt = input("Enter donation amount for new donor: ")
        new_donor_list = [[full_name, contrib_amt]]
        print("new list contains: ", new_donor_list)
        local_donor_list = local_donor_list+new_donor_list
        print("updated donor list: ", local_donor_list)
        print("Dear {}, Thank you so much for your generous contribution".format(full_name))
        print("")
    return local_donor_list
        
# function - create report
def fun_report():
    sum = 0
    donor_len = len(donor_list)
    print("donor_len = ", donor_len)
    count1 = 0
    print("")
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
        

# main
if __name__ == "__main__":
    donor_list = [["Mickey Mouse", "100", "150", "100"], ["Minnie Mouse", "50", "50"], ["Ron Jones", "100"],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]
    response = ""
    while response != "q":
        response = input("Please select:\n 1 to Send a Thank you \n 2 to Create a report \n or q to quit : ")
        if response == "1":
            updated_list = fun_sendty(donor_list)
            donor_list = updated_list
        elif response == "2":
            fun_report()
        elif response == "q":
            print("q selected - Good-bye")
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            

