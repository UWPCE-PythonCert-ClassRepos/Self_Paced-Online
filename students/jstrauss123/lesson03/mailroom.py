#!/usr/bin/env python3

# function - send thank you
def fun_sendty():
    full_name = input("Please provide full name of donor: ")
    while full_name == "list":
        print(donor_list)
        full_name = input("Please provide full name of donor: ")
    if full_name in donor_list:
        #print("full name entered is: ", full_name)
        idx_num = donor_list.index(full_name)
        #print("index is: ", idx_num)
        #str1 = "donamt_" + str(idx_num)
        #print("str1 value is: ", str1)
        #print(" list value is equal to: ", str1[-1])
        # if donor in list send thank you email
        print("Dear {}, Thank you so much for your generous contribution".format(donor_list[idx_num]))
    # if user not in donor_list add new donor and prompt for contribution amount
    else: 
        donor_list.append(full_name)
        idx_num = donor_list.index(full_name)
        new_donamt = input("Enter donation amount for new donor: ")
        newamt = float(new_donamt)
        print("Dear {}, Thank you so much for your generous contribution".format(donor_list[idx_num]))
        # code here to create new contribution list for new donor
        #donamt_<insert index here>.append(newamt)
    #print("response is: ", response)    
    #if response_ty == "list"
    #    print(donor_list)
    #if response_ty in donor_list:

# function - create report
def fun_report():
    #arr6 = [['Joey', 30, 199.99], ['Jan', 36, 29999.97], ['Bob', 55, 999999.99]] 
    donor_len = len(donor_list)
    count1 = 0
    print("")
    print("{:15} |{:>15} |{:>2} |{:>15}".format("Donor Name","Total Given","Num Gifts","Average Gifts" ))
    while count1 < donor_len:
        
        print("{:15} ${:>15} {:>2} ${:>15}".format(donor_list[count1], 25000, 2, 10000))
        count1 += 1
    print("")
        

# main
if __name__ == "__main__":
    #donor_list = [["Mickey Mouse", 100, 150, 100], ["Minnie Mouse", 50, 50], ["Ron Jones", 100],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]
    donor_list = ["Mickey Mouse", "Minnie Mouse", "Ron Jones", "Donald Duck", "Busy Beaver"]
    donamt_0 = ["100", "100", "100"]
    donamt_1 = ["50", "50", "100"]
    donamt_2 = ["100", "100", "100"]
    donamt_3 = ["10", "10", "10"]
    donamt_4 = ["5", "5"]
    
    response = ""
    while response != "q":
        response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
        if response == "1":
            fun_sendty()
            #break
        elif response == "2":
            fun_report()
            #break
        elif response == "q":
            print("q selected - Good-bye")
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            #print("exiting mailroom")
            #break
    #print("Quit selected - Good-bye")

