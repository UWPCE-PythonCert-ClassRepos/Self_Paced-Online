"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    November 29th 2018
"""

"""
    There are quite a bit of prints that were used during testing. This
    can be deleted if need be. Keeping them there in case of bug fixes
    needed with this assignment. With the list of lists I felt it important.
    """

#Initial Donor list with donations and then print for checking.
donors = [['Adam Alvarez', 1.25],['Beth Bonnor', 2.73]]
donors.append(['Cate Campbell', 3.33, 4.44])
donors.append(['Dave Don', 5550.33, 1.41])
donors.append(['Eric Ebron', 12.02, 5.25, 4.25])
#print(donors)

#Display the Thank you note to the screen
def display_thank_you(donor, amount): #Create an email with name an donation.
    email = (
             donor + ", \n\n    Thank you for your generous donation of $" +
             amount + "\n\nSincerely,\nDonation Center\n(555) 555-5555"
             )
    print("\n\n" + email)
    print("\n\n\nReturning to the main menu.....")
    start_up() #After email is displayed - start over.

#Send a Thank You note function
def thank_you():
    print("\n(You can type \"list\" to display current donors)")
    name = input("What is the First and Last name of the recipient? ")
    #print(name) #Display the name input for testing (before checks)
    if name.lower() == 'q': #Return to start if q is typed
        start_up()
    while name.lower() == 'list': #loop until a name other than list is given.
        for i in range(len(donors)): #Display all current donors (name only)
            print(donors[i][0], end=', ')
        print() #New line after list is printed.
        name = input("Type a full name from the list or provide a new one? ")
        if name.lower() == 'q': #Return to start if q is typed
            start_up()
    donation = input("How much is the donation? ")
    if donation.lower() == 'q':#Return to start if q is typed
        start_up()
    found = False #Trigger to see if a name is found in current list
    for item in donors:
        if name in item:
            item.append(float(donation))
            #print("*Existing Donor Found: Donation Added*")
            #print(donors) #Verification that a donation was added to donor.
            found = True #Donor was found - do not add.
    if not found: #If no donor was found - add to list.
        donors.append([name, float(donation)])
        #print("*New Donor Added*")
        #print(donors) #Verification that a new donor and donation was added.
    display_thank_you(name, donation) #Pass the name a donation for display

#Display the donor table - nicely formatted.
def display_report(donor_table):
    donor_table.sort(key = lambda x: x[1], reverse = True)
    #print(donor_table)
    #Header row for Name, Total Donation, Donation Count, Donation Average
    header = (
              f"{'Donor Name':<18}{'| Total Given':>13}"
              f"{' | Num Gifts ':>12}{' | Average Gift':>12}"
              )
    print("\n\n\n" + header)
    print("-" * 59)
    #Space padding for each (12 for name, 3 age, 14 cost) (name left aligned)
    for donor in donor_table:
        print('{:<18}${:>12}{:>8}      ${:>13}'.format(*donor))
    print("\n\n")
    start_up()

#Create a report
def create_report():
    donor_table = [] #Empty donor table to hold new information.
    for donor in donors:
        count = len(donor) - 1 #The first item is a name not an amount.
        donation_sum = 0.00
        for item in donor:
            if type(item) is not str: #If the item is an amount - add it.
                donation_sum += item
        d_sum = f"{donation_sum:.2f}" #Format and account for rounding.
        avg = float(d_sum) / count
        avg2 = f"{avg:.2f}" #Format and account for rounding.
        donor_table.append([donor[0], float(d_sum), count, float(avg2)])
    #print(donor_table)
    display_report(donor_table)

#Prompt for an action (Thank you note, Report, Quit)
def start_up():
    print("\n\nWhat would you like to do? (Enter a Number or \'q\' to quit)")
    print("TIP: \'q\' - anywhere else brings you back to this menu.")
    action = input("\n1:Send a Thank you | 2:Create a Report | or quit?  ")
    if action.lower() == 'q':
        exit()
    elif action == '1':
        thank_you()
    elif action == '2':
        create_report()
    else:
        print("Invalid Choice - Start Over")
        start_up()

#Main function to kick off the script by calling the start up function.
if __name__ == "__main__":
    start_up()
