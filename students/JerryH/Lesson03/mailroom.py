#!/usr/bin/env python3

#List of sample donors and donations
donors = [['Bill Gates', 1000],
['Jeff Bezo', 8976.89],
['Jane Johnson', 7662.90],
['Mike Dell', 156374.67],
['Harry Potter', 726364.23],
['Bill Gates', 2344.77],
['Jeff Bezo', 676.89],
['Jane Johnson', 102.90],
['Mike Dell', 13784.87],
['Harry Potter', 7264.09],
['Jane Johnson', 762.90],
['Mike Dell', 1374.67],
['Harry Potter', 72664.23]]

def prompt():
    return (int(input("Please choose the following options:\n1) Send a Thank you.\n2) Create a Report.\n3) Quit.\n")))

def thank_you_prompt():
    return (input("Send a Thank You - Please enter a full name or type \"list\" to list the current donors:\n"))

def get_all_donor_names(donor_list):
    all_names = []
    for i in range(len(donor_list)):
        all_names = all_names + [donors[i][0]]
    return all_names

def choice(op = 0):
    while op > 3 or op < 1:
        op = prompt()

        if op == 1: #Append or list donors
            #Add donor's name or list the exisiting donors
            d_name = thank_you_prompt()
            while d_name.lower() == "list": #provide a list of donors if "list" is entered
                #Get each unique donor's name from the list
                for each_name in (sorted(set(get_all_donor_names(donors)))):
                    print("{}".format(each_name))
                d_name = thank_you_prompt()

            #print(d_name)
            donation = float(input("Please enter the donation amount:\n"))
            donors.append([d_name, donation])
            print("Thank You Email:  Thansk for the donation!\n\n")
            choice()
        elif op == 2: #Create report
            print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
            print("---------------------------------------------------------------\n")
            report = [] #initialize report

            for each_name in (set(get_all_donor_names(donors))):
                num_donation = 0 #initialize number of donation times for each donor
                total_donation = 0 #initialize total donation from the same donor
                for i in range(len(donors)):
                    if each_name == donors[i][0]:
                        num_donation += 1
                        total_donation += donors[i][1]
                report.append([each_name, total_donation, num_donation])

            #sorting the report based on donations
            r_sorted = sorted(report, key=lambda r: r[1], reverse=True)

            #Create the report
            for d in range(len(r_sorted)):
                print("{:23}${:12.2f}{:10}   ${:12.2f}".format(r_sorted[d][0], r_sorted[d][1], r_sorted[d][2], r_sorted[d][1]/r_sorted[d][2]))

            print("\n")
            choice()

        elif op == 3:   #To quit the script
            print("Thanks for using my script! Bye!")

#start the script
if __name__ == "__main__":
    choice()
