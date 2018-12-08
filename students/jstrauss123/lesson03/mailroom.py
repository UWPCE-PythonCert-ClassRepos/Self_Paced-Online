#!/usr/bin/env python3

# function - send thank you
def fun_sendty():
    response_ty = input("Please provide full name of donor: ")
    while response_ty == "list":
        print(donor_list)
        response_ty = input("Please provide full name of donor: ")
    if response_ty in donor_list:
        # send thank you email
        print("donor in list, creating a ty email with last contrib amt")
    # if user not in donor_list add new donor
    else: 
        print("new donor, adding to donor_list")
        don_amt = input("Enter donation amount for new donor: ")
        amt1 = float(don_amt)
        print(amt1)
        
    #if response_ty == "list"
    #    print(donor_list)
    #if response_ty in donor_list:

# function - create report
def fun_report():
    yum = ''
    
        

# main
if __name__ == "__main__":
    donor_list = [["Mickey Mouse", 100, 150, 100], ["Minnie Mouse", 50, 50], ["Ron Jones", 100],["Donald Duck", "25"], ["Busy Bear", "10", "10", "10"]]

    response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
    print(response)
    while response != "q":
        if response == "1":
            fun_sendty()
            break
        elif response == "2":
            print("running report")
            break
        else:
            response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
            #print("exiting mailroom")
            #break
    print("Quit selected - Good-bye")

