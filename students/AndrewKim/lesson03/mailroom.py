
donors = ["Andrew Kim", "Jamie Park", "Caroline Yeung", "Billy Yan"]
totalAmt = [5.0, 4.0, 3.0, 2.0]
numGifts = [1, 1, 1, 1]

def thankYou():
    #prompt for a Full Name
    name = input("Type the donor's full name: ")
    #if user types 'list'
    while name == "list":
        for item in donors:
            print(item)
        name = input("Type the donor's full name: ")

    #set flag
    found = False
    #find if the name is in the list
    for i in range(len(donors)):
        if donors[i] == name:
            donationAmt(i)
            found = True
     #if name not in the list
    if found == False:
        donors.append(name)
        totalAmt.append(0.0)
        numGifts.append(0)
        donationAmt(len(donors)-1)
    #print thank you
    print(f'Thank you {name}, for your generous donation!') 
            
def donationAmt(i):
    userInput = input("Please enter the donation amount: ")
    amtFloat = float(userInput)
    #'${:,.2f}'.format(amtFloat)
    totalAmt[i] = totalAmt[i] + amtFloat
    numGifts[i] = numGifts[i] + 1
    
def report():
    print('{:<20}|{:^15}|{:^12}|{}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    for i in range(len(donors)):
        print('{:<20} ${:<15,.2f}{:^12} ${:,.2f}'.format(donors[i], totalAmt[i], numGifts[i], totalAmt[i]/numGifts[i]))
    
    
    
while True:
    choice = input("Please choose from a menu of 3 actions: 'Send a Thank You', 'Create a Report' or 'quit': ")
    if choice == "Send a Thank You":
        thankYou()
    elif choice == "Create a Report":
        report()
    elif choice == "quit":
        break