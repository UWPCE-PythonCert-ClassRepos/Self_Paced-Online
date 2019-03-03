#Mailroom script that creates canned responses for donations and prints a report of all donations
from operator import itemgetter
import os.path
from sys import exit

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
    letter += f'\tThank you for your donation of ${donors[donor][-1]:,.2f} to the foundation.'

    if len(donors[donor]) > 1:
        letter += f'\tWe also thank you for your continuing support and appreciate that you are a repeat giver.'

    letter += '\tYour generous gift will make a tremendous difference in the coming years.\n\n'
    letter += 'Sincerely,\n\tDirector of the Foundation\n'
    return letter

def get_donation():
    """Asks for and returns donation amount"""
    try:
        donation = float(input('\nEnter donation amount: '))
    except ValueError:
        print('\n***Error! Use only numbers for the donation amount.***')
        return get_donation()
    else:
        return donation

def get_name():
    """Gets user input for donor name, displays list of names if needed"""
    name = input('\nEnter a donor name or type list to see all current donors: ').title()

    #display list of names if requested
    if name.upper() == 'LIST':
        #changed to comprehension
        [print(donor) for donor in donors]
        get_name()

    return name

def add_donation(name, amount):
    """Adds donation amount for name, adds new donor if not already on list"""

    #if name is in list, add donation amount only
    if name in donors:
        donors[name].append(amount)

    #otherwise add new donor to list with donation amount
    else:
        donors[name] = [amount]

    print(donors)


def thank_you():
    """prints thank you letter based on user input"""
    name = get_name()

    amount = float(get_donation())

    add_donation(name, amount)

    #print thank you note for new donation
    print(create_letter(name))


def report():
    """Gets the aggregate donations sorted by descending aggregate donations and formats them into a report"""
    print(report_formatter(order_donations(donors)))

def order_donations(donors):
    ordered_donations = sorted(aggregate_donations(donors), key=itemgetter(1), reverse=True)
    return ordered_donations


def aggregate_donations(donors):
    """Aggregates the donations from the donors and returns them in a list"""
    #parse donor list and aggregate them into totals for each donor
    #changed to list comprehension
    donor_totals = [[donor,sum(donors[donor]),len(donors[donor]),sum(donors[donor])/len(donors[donor])] for donor in donors]

    return donor_totals


def report_formatter(donations):
    """Formats the passed in aggregate donations into a report"""
    #print header
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    formatted_report = f'\n{header[0]:<20}|{header[1]:^15}|{header[2]:^11}|{header[3]:^16}'
    formatted_report += '\n'
    formatted_report += horz*(20+15+13+16+2)
    formatted_report += '\n'

    #print donor rows
    #changed to comprehension
    formatted_report += '\n'.join(f'{row[0]:<20}  ${row[1]:<15,.2f}{row[2]:<11} ${row[3]:<16,.2f}' for row in donations)
    formatted_report += '\n'
    return formatted_report


def get_file_path():
    """Requests file path from user"""
    userpath = input('\nEnter the path where the files should be created.  Hit enter to create in directory of program: ')

    return userpath

def export_letter(passedpath, donor):
    """Writes letter to file with given path"""
    try:
        os.path.isdir(passedpath)

        #add path if given
        filename = os.path.join(passedpath,donor.replace(' ','_') + '.txt')

        #updated to use with
        with open(filename, 'w') as outfile:
            outfile.write(create_letter(donor))
        outfile.close()
    except PermissionError:
        print('\n***Error! User does not have permission to write to this directory.***')

        return send_all()
    except FileNotFoundError:
        print('\n***Error! Please create directory before creating letters.***')
        return send_all()

def send_all():
    """Sends letters to all donors when called"""
    filepath = ''
    filepath = get_file_path()

    for donor in donors:
        export_letter(filepath, donor)


def quit():
    """Function that exists the program when called"""
    exit()

#dictionary for switch that calls functions based on key values
menu = {'1':thank_you, '2':report, '3':send_all,'4':quit}



def main():
    """Main program flow for getting user input and performing actions"""
    #prompt user for action and handle errors if invalid selection
    while True:
        print("1. Send a Thank You to a single donor","\n2. Create a Report", "\n3. Send letters to all donors", "\n4. Quit")
        selection = input("Enter the number for the action you require: ")
        try:
            menu[selection]()

        except KeyError:
            print('\n***Error! Please enter only numbers from the menu.***')


#Main program
if __name__ == '__main__':
    main()



