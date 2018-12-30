from datetime import datetime
import os

flag=True

#Data structures
people={'Jeff Bezos': [1005.49, 3116.72, 5200],
             'Kelly Hirsch': [21.47, 1500],
             'Alice Wong': [2400.54],
             'Malcolm Wang': [355.42, 579.31],
             'Kayla McAllison': [636.9, 850.13, 125.23],
             'Jack Boyle': [66.9, 85.13, 443.23]}

#Functions
def PrintEMail(name, amount):
    ''' Print Email message'''
    print("\nDear " + name +'\n')
    print('We would like to thank you for continuing support for our organization!\n')
    print('Your contribution of $' + str(amount) + ' is received and very much appreciated!')
    print('\nThank you\nKennan Yilmaz')

def Generate_Letters(donationdata):
    for donor, amount in donationdata.items():
        #Build file name
        dt= str(datetime.now().strftime('%Y%m%d%H%M%S'))
        filename=donor + dt + ".txt"

        #Write to file
    try:
        with open(filename, 'w') as file:
            letter='Dear {}, \n\n\tThank for for your very kind donations of ${}.\n\n\tIt will be put to very ' \
                   'good use.\n\n\t\tSincerely, \n\n\t\t\t - The Team'.format(donor,
                                                                                                       str(amount[len(amount)-1]))
            file.write(letter)
    except OSError as fileerr:
        print(fileerr)
        print("\nThere was an error opening the file.\n")
        return
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("\nThere was an error reading the file")
        return
    except ValueError as verr:
        print("There was an error writing to the file.")
        return

def func_Send_Thankyou():
    ''' Send a Thank you note'''
    print('Thank you')
    value=0
    name = input('Type donor name or ''list'' to see all the names=')
    if name == 'list':
        # List all donors if user enters 'list'
        for donor in people.keys():
            print(donor)
    else:  # It is assumed that name entered in this case
        # Prompt for donation amount
        try:
            value = float(input('Please enter the donation amount='))
            # Is it in the db?
            # If in database, append value else create a new record
            if name in people:
                #Add the donation
                getlist = people[name]
                getlist.append(value)
        except:
            print("Invalid value entered!")
            return
        else:
            #Add the name and the donation
            people[name] = value
        # Print the email now
        PrintEMail(name, value)

def func_Create_Report():
    """Print donation history"""
    donations= []
    for donors in people:
        entry=[]
        entry.append(donors)
        for item in people[donors]:
            entry.append(item)

        donations.append(entry)

    #Sort the donations
    report_data = [[person[0], sum(person[1:]), len(person[1:]), sum(person[1:]) / len(person[1:])]
                  for person in donations]
    sorted_data = sorted(report_data, key=lambda x: x[1], reverse=True)

    #Print the header
    print('{0:25}{1:15}{2:15}{3:15}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('=' * 50)

    for donor in donations:
        total_amount=sum(donor[1:])
        total_donation=len(donor)-1
        avg_donation=total_amount/total_donation
        print('{:<25s}  ${:>18,.2f}  {:>15d}  ${:>18,.2f}'.format( donor[0], total_amount, total_donation,
                                                                      avg_donation))

def  func_Send_Letters():
    print('Write the letters to file in ' + os.getcwd())
    Generate_Letters(people)

def func_Quit():
    global flag
    flag=False
    print('Quiting ... DONE!')

def print_donors():
    print('Print Donors')


#Display the menu
def showmenu ():
    """Displays the menu options"""
    while (flag):
        print('\n')
        print('1 - Send a Thank You')
        print('2 - Create a Report')
        print('3 - Send letters to everyone')
        print ('4 -  Quit')
        response=int(input("Please select and option (1,2, 3 or 4)"))
        # Dict implementation of the menu
        switch_func_dict = {
            1: func_Send_Thankyou,
            2: func_Create_Report,
            3: func_Send_Letters,
            4: func_Quit,
        }
        if (response >= 0) and (response < 5):
            switch_func_dict[response]()

if __name__ == '__main__':
    showmenu()

