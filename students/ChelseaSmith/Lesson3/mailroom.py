record = [["James Smith", 85, 100, 75],
          ["Alex Jones", 25, 25, 25],
          ["Kate Smith", 100],
          ["Kate Jones", 175, 50],
          ["Alex Smith", 200, 200, 200]]  # creates initial donor record

choose = 0  # creates variable for selecting from main menu

def report(listin):  # prints a report of all donors
    print(f"Donor name" + " " * 17 + " | Total Given | Num Gifts | Average Gift\n")
    for row in listin:
        sum = 0
        num = 0
        name = row[0]
        for item in row[1:]:
            sum = sum + int(item)
            num = num + 1
        print(f"{name:<28}${sum:12.2f}{num:10}   ${(sum / num):13.2f}")


def checknew(listin, name):  # returns true if name is not already in list input
    new = True
    for row in listin:
        if name == row[0]:
            new = False
    return new


def getrow(listin, name):  # returns the index value for a particular donor in input given name
    value = -1
    for idx, row in enumerate(listin):
        if name == row[0]:
            value = idx
    if value == -1:
        print("Error! Donor not found.")  # Trips if donor not found, which shouldn't happen, since this is called after new donors created.
    else:
        return value


while choose != 3:
    choose = int(input("Please enter 1 to send a thank you, 2 to generate a report, or 3 to quit."))
    if choose == 3:  # says goodbye. after this, loop will close and script will end
        print("Goodbye!")
    elif choose == 1:  # gets information for sending a thank you
        name = input("Please enter the donor's full name or list for a list of donors.")
        while name == "list":  # provide list of donors for as many times as user asks
            for item in record:
                print(item[0])
            name = input("Please enter the donor's full name or list for a list of donors.")
        if checknew(record, name):  # checks if new donor
            record.append([name])  # adds new donor to database
        donation = int((input("Enter donation amount")))  # gets donation amount
        record[getrow(record,name)].append(donation)  # uses getrow function to find correct index in record and appends a donation to the end of the list at that index
        print(f"Dear {name},\nThank you for your generous donation of ${donation}.\n"   # makes a nice letter
              f"Sincerely,\n Generic Charities")
    elif choose == 2:  # prints report
        report(record)
