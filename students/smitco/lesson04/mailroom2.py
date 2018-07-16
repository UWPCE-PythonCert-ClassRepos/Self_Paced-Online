#lesson 04 mailroom pt 2
#!/usr/bin/env python3

#starting list of 5+ donors and 1-3 donations each
donors = {"John Travolta" : [5000, 7500], 
"Jane Fonda" :[10000, 8000, 6500], 
"Judy Blume" : [3000, 3000], 
"Joey Tribbiani" : [9000], 
"Jenny Gump" : [10300, 13750, 12500]}

#menu: prompt user for actions: send a thank you, create a report, send letters, quit
#thanks: ask for name, add to list if needed, ask for amount, add to list
#report: print report of each donor with total donated, number of donations, average donation
#letters: send letters to all donors
#quit: exit

def menu():
    ask = input("Please choose an action: \n1) Send a new thank you \n2) Create a report \n3) Send letters to all donors \n4) Quit \n>>")
    options = {"1" : thanks, "2" : report, "3" : letters, "4" : quit}
    if ask in options:
        options.get(ask)()
    else:
        print("\nThere was an error. Please try again.\n")

def donation(name):
    amount = input("\nWhat is the donation amount?\n>>")
    if amount.lower() == "exit":
        print("\nExiting.\n")
        donors.pop(name)
    elif int(amount) >= (10 ** 6):
        print("\nThe amount entered is invalid.")
        donors.pop(name)
    else:
        donors[name].append(int(amount))
        ty_temp = {"first_last" : name, "dollars" : amount}
        print("\nThank you, {first_last}, for supporting The Brave Heart Foundation. Your generous donation of ${dollars} will make a positive, life-changing impact for teens nationwide.\n".format(**ty_temp))

def thanks():
    while True:
        addressee = input("\nTo whom would you like to send a thank you? \n'List' will display current donors. \n'Exit' will return to main menu.\n>>")
        if addressee.lower() == "exit":
            print("\nExiting.\n")
            break
        elif addressee.lower() == "list":
            print(list(donors.keys()))
        elif addressee not in donors:
            donors[addressee] = []
            donation(addressee)
        else:
            donation(addressee)
            
def report():
    donor_sums = {}
    for d in donors:
        total = sum(donors[d])
        count = len(donors[d])
        average = total/count
        donor_sums[d] = [total, count, average]
        sorted_donor_sums = sorted(donor_sums.items(), key = lambda x : x[1], reverse = True)
    print("\n{:<20} {:<15} {:^12} {:<15}".format("Donor", "Total Given", "Number", "Average Given"))
    for i in range(len(sorted_donor_sums)):
        info = {"donor_name" : sorted_donor_sums[i][0], 
        "donor_total" : sorted_donor_sums[i][1][0],
        "donor_count" : sorted_donor_sums[i][1][1],
        "donor_avg" : sorted_donor_sums[i][1][2]}
        print("{donor_name:<20} ${donor_total:^15.2f} {donor_count:^12} ${donor_avg:^15.2f}".format(**info))
    print()
    
def letters():
    import os
    import datetime
    current = datetime.datetime.now()
    date = str(current.month) + "_" + str(current.day) + "_" + str(current.year)
    for d in donors:
        letter_temp = {"letter_name" : d, "letter_amount" : sum(donors[d])}
        letter = ("Dear {letter_name}, \n\nThank you for supporting The Brave Heart Foundation. \nYour donations totaling ${letter_amount} have made a positive, life-changing impact for teens nationwide.\n\nBlessings,\nBHF".format(**letter_temp))
        file_name = d + " " + date + ".txt"
        with open(file_name, "w") as file:
            file.write(letter)
    print("\nFiles completed.\n")

def quit():
    print("\nGoodbye.")
    exit()


    
if __name__ == '__main__':
    while True:
        menu()