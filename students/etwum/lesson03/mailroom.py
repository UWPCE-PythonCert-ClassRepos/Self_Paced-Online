#!/usr/bin/env python3

if __name__ == "__main__":
    print()

lstHeader = [["Donor Name", "| Total Donation(s)", "| # of Donations", "| Avg Donation"]]
lstDonors = [["Lionel Messi", 1000000.00, 5, 20000.00],["Thierry Henry", 500, 1, 500], ["Michael Jordan", 45000, 3, 15000],
        ["Kobe Bryant", 8000, 2, 4000]]

def send_thank_you():

    return print("works")

def sort_list(lstDonors):
    # used to sort the donor list by the total donations column
    return lstDonors[1]

def create_report():
    # creates a report of the the donors
    for x in lstHeader:
        print('{:<25}{:<20}{:<17}{:<15}'.format(*x))
    print("----------------------------------------------------------------------------")
    for x in sorted(lstDonors,key=(sort_list), reverse= True):
        print('{:<25} $ {:<20}{:^14} $ {:<15}'.format(*x))


print("Welcome to the Mail Room")
print("------------------------------------------------------------------------")
# ****Input/Output****
while True:
    print("""
    Menu of Options
    1) Send Thank You Note
    2) Create Report
    3) Exit Program
    """)
    strChoice = None
    try:
        strChoice = int(input("Which option would you like to perform? Input a number [1 to 3] "))
        if strChoice == 1 or strChoice == 2 or strChoice == 3:
            print()
        else:
            raise Exception
    except Exception:
        print("Please input a valid option: 1, 2, or 3")

    if (strChoice == 1):
        send_thank_you()
        continue

    elif (strChoice == 2):
        create_report()
        continue
    elif (strChoice == 3):
        break


