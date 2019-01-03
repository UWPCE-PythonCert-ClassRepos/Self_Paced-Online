"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 2nd 2019
"""

"""
Update to the mailroom program. Several changes have been made from either
feedback received or refactoring during testing.
"""

#Initial Donor list with a list of their donations.
donors = {'Adam Alvarez':[1.25],'Beth Bonnor':[2.73],'Cate Campbell':[3.33,4.44],
          'Dave Don':[5550.33,141],'Eric Ebron':[12.02,5.25,4.25]}

#Display the thank you note or write a letter.
def thank_you_specific(donor, amount, form):
    if form == 'letter':
        body = (f"{donor}, \n\n    Your donations of ${float(amount):.2f}"
             + " have gone a long way and we value your continued support."
             + "\n\nSincerely,\nDonation Center\n(555) 555-5555")
    elif form == 'note':
        body = (f"\n{donor}, \n\n    Your donation of ${float(amount):.2f} "
                + "was received and we are forever grateful for your support."
                + "\n\nSincerely,\nDonation Center\n(555) 555-5555")
    return body

#Get the donation amount. - then used the thank_you_specific function.
def donation_amount(name):
    while True:
        donation = input("How much is the donation? ")
        if donation.lower() == 'q':#Return to start if q is typed
            return
        try: #Try catch block to make sure we get a numeric for donations.
            donation = float(donation)
            #Unsure of feedback received for this block (line 53)
            if donors.get(name):
                donors[name].append(donation)
            else:
                donors[name] = [donation]
            #display_thank_you(name, donation) #Pass the name a donation for display
            print(thank_you_specific(name, donation, 'note'))
            return
        except ValueError:
            print('Non Numeric Value Entered')

#Send a Thank You note function - will use donation_amount function.
def thank_you():
    print("\n(You can type \"list\" to display current donors)")
    name = input("What is the First and Last name of the recipient? ")
    if name.lower() == 'q': #Return to start if q is typed
        return
    while name.lower() == 'list': #loop until a name other than list is given.
        print()
        print([key for key in donors])
        print()
        name = input("Type a full name from the list or provide a new one? ")
        if name.lower() == 'q': #Return to start if q is typed
            return
    donation_amount(name)

#Display the donor table - nicely formatted.
def create_report(donor_table):
    donor_table.sort(key = lambda x: x[1], reverse = True)
    #Header row for Name, Total Donation, Donation Count, Donation Average
    report = (
              f"\n\n\n{'Donor Name':<18}{'| Total Given':>13}"
              f"{' | Num Gifts ':>12}{' | Average Gift':>12}\n" + ("-" * 59)
              )
    #Space padding for each (12 for name, 3 age, 14 cost) (name left aligned)
    #Utlize compression.
    for donor in donor_table: #Update from feedback - returning to a loop.
        report = report + ('\n{:<18}${:>12.2f}{:>8}      ${:>13.2f}'.format(*donor))
    report = report + ("\n")
    return report

#Create a report
def display_report():
    donor_table = [] #Empty donor table to hold new information.
    for key in donors:
        count = len(donors[key])
        d_sum = f"{sum(donors[key]):.2f}" #Format and account for rounding.
        avg = f"{float(d_sum) / count:.2f}" #Format and account for rounding.
        donor_table.append([key, float(d_sum), count, float(avg)])
    print(create_report(donor_table))

#Get the current donors and their total donation to date"
def get_donors_info():
    #Update per feedback - use of compression I didn't consider as possible.
    return {k: float(f"{sum(v):.2f}") for k, v in donors.items()}

#Letters to everyone
def letters():
    all_donors = get_donors_info()
    for donor in all_donors:
        name = donor
        donations = str(all_donors[donor])
        #email = draft_letter(donor, donations)
        with open(donor + '.txt', 'w') as out_file:
            out_file.write(thank_you_specific(donor, donations, 'letter'))
    print("Your thank you letters have been written to your relative folder.")

#Start up fuction as a dictionary
def start_up():
    #Update per feedback. Define the dict outside of the loop
    choices = {'q':exit, '1':thank_you, '2':display_report,'3':letters}
    while True:
        print("\n\nWhat would you like to do? (Enter a Number or \'q\' to quit)")
        print("TIP: \'q\' - anywhere else brings you back to this menu.")
        action = input("\n1:Send a Thank you | 2:Create a Report | "
                       "3:Send letters to everyone | or quit?  ")
        choice = action.lower()
        try: #Update per feedback to catch KeyError instead of manual.
            choice = choices[choice]
            choice()
        except KeyError:
            print("Invalid Choice - Please choose again.")

#Main function to kick off the script by calling the start up function.
if __name__ == "__main__":
    start_up()
