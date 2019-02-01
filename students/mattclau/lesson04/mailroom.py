#Mailroom script that creates canned responses for donations and prints a report of all donations
from operator import itemgetter
import os.path

#Formatting characters
horz = '-'
vert = '|'

#List of existing donors and their donations
donors = {"Douglas Adams":[1000],
            "Bruce Lee":[9876.55],
            "Charles Barkley":[999999.99,55555.55,7777.77],
            "Scottie Pippen":[1, 5],
            "Ursula K Le Guin":[1234567.89]
        }


def create_letter(donor):
    """Creates letter for the supplied donor name and amount"""
    letter = f'Dear {donor},\n'
    letter += f'\tThank you for your donation of ${donors[donor][-1]:,.2f} to the foundation.  '

    if len(donors[donor]) > 1:
        letter += f'\tWe also thank you for your continuing support and appreciate that you are a repeat giver.  '

    letter += '\tYour generous gift will make a tremendous difference in the coming years.\n\n'
    letter += 'Sincerely,\n\tDirector of the Foundation\n'
    return letter

def get_donation():
    """Asks for and returns donation amount"""
    donation = ''
    while not donation.replace('.','',1).isdecimal():
            donation = input('\nEnter donation amount: ')
            if donation.replace('.','',1).isdecimal():
                return donation
            else:
                print('\n***Error! Use only numbers for the donation amount.***')


def thank_you():
    """Adds donation for name user enters, displays list of names if needed"""
    name = input('\nEnter a donor name or type list to see all current donors: ').title()
    print(name)

    #display list of names if requested
    if name.upper() == 'LIST':
        for donor in donors:
            print(donor)
        thank_you()

    #otherwise ask for donation and add it
    else:
        amount = float(get_donation())

        #if name is in list, add donation amount only
        if name in donors:
            donors[name].append(amount)

        #otherwise add new donor to list with donation amount
        else:
            donors[name] = [amount]

        #print thank you note for new donation
        print(create_letter(name))


def report():
    """Gets the aggregate donations sorted by descending aggregate donations and formats them into a report"""
    report_formatter(sorted(aggregate_donations(), key=itemgetter(1), reverse=True))
    #print(aggregate_donations())


def aggregate_donations():
    """Aggregates the donations from the donors and returns them in a list"""
    donor_totals = []

    #parse donor list and aggregate them into totals for each donor
    for donor in donors:
        donor_totals += [[donor,sum(donors[donor]),len(donors[donor]),sum(donors[donor])/len(donors[donor])]]

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

def send_all():
    """Sends letters to all donors when called"""
    filepath = input('\nEnter the path where the files should be created.  Hit enter to create in directory of program: ')
    for donor in donors:
        filename = os.path.join(filepath,donor.replace(' ','_') + '.txt')
        outfile = open(filename, 'w')
        outfile.write(create_letter(donor))
        outfile.close()



def quit():
    """Function that exists the program when called"""
    from sys import exit
    exit()

#dictionary for switch
menu = {'1':thank_you, '2':report, '3':send_all,'4':quit}



def main():
    """Main program flow for getting user input and performing actions"""
    #prompt user for action
    while True:
        print("1. Send a Thank You to a single donor","\n2. Create a Report", "\n3. Send letters to all donors", "\n4. Quit")
        selection = input("Enter the number for the action you require: ")

        #error handling
        if selection not in menu:
            print('\n***Error! Please enter only numbers from the menu.***')
        #perform action based on selection
        else:
            menu[selection]()


#Main program
if __name__ == '__main__':
    main()



