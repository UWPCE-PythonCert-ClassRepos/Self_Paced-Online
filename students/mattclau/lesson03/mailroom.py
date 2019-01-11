#Mailroom script that creates canned responses for donations and prints a report of all donations
from operator import itemgetter

#Formatting characters
horz = '-'
vert = '|'

#List of existing donors and their donations
donors = [["John Smith",1000]
          ,["Bruce Lee",9876.55]
          ,["Charles Barkley",999999.99]
          ,["Charles Barkley",55555.55]
          ,["Charles Barkley",7777.77]
          ,["Scottie Pippen",1]
          ,["Scottie Pippen",5]
          ,["Ursula K Le Guin", 1234567.89]
         ]


def thank_you():
    """Adds donation for name user enters, displays list of names if needed"""
    name = input('\nEnter a donor name or type list to see all current donors: ')

    #display list of names if requested
    if name.upper() == 'LIST':
        for donor in donors:
            print(donor[0])
        thank_you()

    #otherwise get donation amount for name
    else:
        donation = ''
        while not donation.replace('.','',1).isdecimal():
            donation = input('\nEnter donation amount: ')
            if donation.replace('.','',1).isdecimal():
                donors.append([name, float(donation)])
            else:
                print('\n***Error! Use only numbers for the donation amount.***')
        print(f'\nDear {donors[-1][0]},\n')
        print(f'\tThank you for your donation of ${donors[-1][1]:,.2f} to the foundation.  ')
        print('\tYour generous gift will make a tremendous difference in the coming years.\n\n')
        print('Sincerely,\n\tDirector of the Foundation\n')


def report():
    """Gets the aggregate donations sorted by descending aggregate donations and formats them into a report"""
    report_formatter(sorted(aggregate_donations(), key=itemgetter(1), reverse=True))

def aggregate_donations():
    """Aggregates the donations from the donors and returns them in a list"""
    donor_totals = []

    #parse donor list and aggregate them into totals for each donor
    for donor in donors:
        #Add first instance of each donor
        if not any(donor[0] in donors for donors in donor_totals):
            donor_totals.append([donor[0],donor[1],1,donor[1]])
        #Increment values for repeat donors
        else:
            for i in range(len(donor_totals)):
                if donor[0] == donor_totals[i][0]:
                    donor_totals[i][1] += donor[1]
                    donor_totals[i][2] += 1
                    donor_totals[i][3] = donor_totals[i][1] / donor_totals[i][2]

    return donor_totals


def report_formatter(report):
    """Formats the passed in aggregate donations into a report"""
    #print header
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print(f'\n{header[0]:<20}|{header[1]:^15}|{header[2]:^11}|{header[3]:^16}')
    print(horz*(20+15+13+16+2))

    #print donor rows
    for row in report:
        print(f'{row[0]:<20}  ${row[1]:<15,.2f}{row[2]:<11} ${row[3]:<16,.2f}')
    print('\n')


def main():
    """Main program flow for getting user input and performing actions"""
    quit = False

    #prompt user for action
    while not quit:
        print("1. Send a Thank You","\n2. Create a Report", "\n3. Quit")
        action = input("Enter the number for the action you require: ")

        #Send thankyou action
        if action.isdigit() and int(action) == 1:
            thank_you()

        #Create Report
        elif action.isdigit() and int(action) == 2:
            report()

        #Quit program
        elif action.isdigit() and int(action) == 3:
            print('Exiting the program.')
            quit = True

        #Re-prompt if invalid selection
        else:
            print("\n***Error! Please enter a number from 1 to 3***\n")

#Main program
if __name__ == '__main__':
    main()



