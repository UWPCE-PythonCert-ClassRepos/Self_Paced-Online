donors = ["Tony Lee", "Andy Arko", "Michelle Lee", "Tom Ludwinski", "Kurt Lafser"]
totalDonationAmount = [100, 200, 300, 400, 500]
numGifts = [1, 1, 1, 1, 1]

def send_thankYou():
    donorName = input("Enter the donor's full name: ")
    #if user types 'list'
    while donorName == "list":
        for item in donors:
            print(item)
        donorName = input("Enter the donor's full name: ")

    if isSameDonor(donorName) is not True:
        donors.append(donorName)
        totalDonationAmount.append(0.0)
        numGifts.append(0)
        setDonation(len(donors)-1, getDonation())

    print(f'Thank you {donorName}, for your donation!')

def create_report():
    print('{:20}|{:15}|{:12}|{}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    for i in range(len(donors)):
        print('{:20} ${:10,.2f}{:^17} ${:10,.2f}'.format(donors[i], totalDonationAmount[i], numGifts[i], totalDonationAmount[i]/numGifts[i]))

def isSameDonor(donorName):
    for i in range(len(donors)):
        if donors[i] == donorName:
            setDonation(i, getDonation())
            return True
    return False

def getDonation():
    donantionAmount = float(input("Please enter the donation amount: "))
    return donantionAmount

def setDonation(donor, donorAmount):
    totalDonationAmount[donor] = totalDonationAmount[donor] + donorAmount
    numGifts[donor] = numGifts[donor] + 1

while True:
    choice = input("Please choose from a menu of 3 actions: 'Send a Thank You', 'Create a Report' or 'quit': ")
    if choice == "Send a Thank You":
        send_thankYou()
    elif choice == "Create a Report":
        create_report()
    elif choice == "quit":
        break
