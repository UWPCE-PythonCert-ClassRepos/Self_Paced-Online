
donor_history = {'Andrew Kim': [5.0, 3.0], 'Jamie Park': [4.0], 'Tim Duncan': [3.0], 'Billy Yan': [2.0]}

def thank_you():
    #prompt for a Full Name
    name = input("Type the donor's full name: ")
    #if user types 'list'
    while name == "list":
        for a in donor_history,keys():
            print(a)
        name = input("Type the donor's full name: ")

    #if the name is not in the list
    if name not in donor_history.keys():
        donor_history[name] = []
    
    #add donation amount on the history
    donation_amount = input("Please enter the donation amount: ")
    try:
        donor_history[name].append(float(donation_amount))
        #print thank you
        print(thank_you_msg(name))
		
    except ValueError:
        print("Not a valid number! Please enter a valid number\n")
    
def thank_you_msg(name):
	return 'thank you {} for your generous donation of {}'.format(name, sum(donor_history[name]))
    
def report():
    print('{:20}|{:15}|{:10}|{:15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    for donor, amount in donor_history.items():
        print('{:20}|{:15}|{:10}|{:15}'.format(donor, sum(amount), len(amount), sum(amount)/len(amount)))
    
def send_all():
    for donor, amount in donor_history.items():
        with open(donor+'.txt', 'w') as donor_file:
            donor_file.write('Thank you {}, for your generous donation of {}!'.format(donor, sum(amount)))
    
while True:
    choice = input('''Please choose from a menu of 3 actions:\n
                    1 - Send a Thank You
                    2 - Create a Report
                    3 - Send letters to everyone
                    4 - Quit\n''')
    try:
        choice = int(choice)
    except ValueError:
        print("Not a valid number! Please enter a valid number\n")
        
    if choice == 1:
        thank_you()
    elif choice == 2:
        report()
    elif choice == 3:
        send_all()
    elif choice == 4:
        break