#!/usr/bin/env python3

# function - create report
def fun_report():
    yum = ''

# function - send thank you
def fun_sendty():
    yum1 = ''



# main
if __name__ == "__main__":
    donor_list = [["Mickey Mouse", 100, 150, 100], ["Minnie Mouse", 50, 50], ["Ron Jones", 100]]

    response = input("Please select: 1 to Send a Thank you, 2 to Create a report or q to quit : ")
    print(response)
    while response != "q":
        if response == "1":
            print("running thank you")
            break
        elif response == "2":
            print("running report")
            break
        else:
            print("exiting mailroom")
            break
        

