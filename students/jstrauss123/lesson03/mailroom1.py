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
    donor_len = len(donor_list)
    print("donor_len = ", donor_len)
    count1 = 0
    print("")
    print("{:15} |{:>15} |{:>2} |{:>15}".format("Donor Name","Total Given","Num Gifts","Average Gifts" ))
    while count1 < donor_len:
        print("")
        #print("{:15} ${:>15} {:>2} ${:>15}".format(donor_list[count1], 25000, 2, 12000))
        count1 += 1
    print("")
        

# main
if __name__ == "__main__":
    donor_list = [["Mickey Mouse", "100", "150", "100"], ["Minnie Mouse", "50", "50"], ["Ron Jones", "100"],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]
    response = ""
    while response != "q":
        response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
        if response == "1":
            updated_list = fun_sendty(donor_list)
            donor_list = updated_list
        elif response == "2":
            fun_report()
        elif response == "q":
            print("q selected - Good-bye")
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            

