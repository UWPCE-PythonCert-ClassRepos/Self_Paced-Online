#!/usr/bin/env python3

# function - send thank you
def fun_sendty():
    full_name = input("Please provide full name of donor: ")
    while full_name == "list":
        print(donor_list)
        full_name = input("Please provide full name of donor: ")
    if full_name in donor_list:
        print("full name entered is: ", full_name)
        idx_num = donor_list.index(full_name)
        print("index is: ", idx_num)
        str1 = "donamt_" + str(idx_num)
        print(str1)
        # send thank you email
        print("donor in list, creating a ty email with last contrib amt")
        print("Dear {}, Thank you so much for your contribution in the amount of ${}".format(donor_list[idx_num], str1[-1]))
        #{list5[0][:-1]} is {list5[1]} and the weight of a {list5[2][:-1]} is {list5[3]}")
    # if user not in donor_list add new donor
    else: 
        print("new donor, adding to donor_list")
        don_amt = input("Enter donation amount for new donor: ")
        amt1 = float(don_amt)
        print("amt is: ", amt1)
    print("response is: ", response)    
    #if response_ty == "list"
    #    print(donor_list)
    #if response_ty in donor_list:

# function - create report
def fun_report():
    yum = ''
    
        

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
            print("running report")
            #break
        elif response == "q":
            print("q selected - Good-bye")
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            #print("exiting mailroom")
            #break
    #print("Quit selected - Good-bye")

