#!/usr/bin/env python3

donors = [["Manny Machado",[12.2,2.51,3.20]],["Adam Jones",[1024.14,22.21,323.45]],["Chris Davis",[3.2,5.55,4.20]]]


def displaylist():    
    for sublist in donors:
        print(sublist[0])

def writeletter(name,amount):
    print('Dear {},'.format(name))
    print("Thank you for donating ${:.2f} to the Human Fund. Your money will be used appropriately.".format(amount))

def writereport(donors):
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*67)
    for i in donors:
        print('{1:27}${0:11.2f}{2:12}  ${3:12.2f}'.format(*i))


# Function to send a thank you letter.
def thankyou():
    loop_trigger = True
    while loop_trigger == True:
        input_name = input("Enter full name: ")
        for i, donor_row in enumerate(donors):
            if donor_row[0] == input_name:
                donation = float(input("Enter donation amount:"))
                donors[i][1].append(float(donation))
                #print(donors)
                writeletter(donors[i][0],donors[i][1][len(donors[i][1])-1])
                loop_trigger = False
                break
            elif input_name == 'list':
                displaylist()
                break
            else:
                print("adding {} to list".format(input_name))
                donation = float(input("Enter donation amount:"))
                donors.append([input_name,[donation]])
                #print(donors)
                writeletter(donors[len(donors)-1][0],donors[len(donors)-1][1][0])
                loop_trigger = False
                break


# Function to write a report of the donors.
def createreport():
    donors_report = []
    for i, name in enumerate(donors):
        sum_donation = 0
        avg_donation = 0
        for j in donors[i][1]:
            sum_donation = sum_donation + j
            num_donation = len(donors[i][1])
        avg_donation = sum_donation/num_donation
        donors_report.append([sum_donation, name[0], num_donation, avg_donation])
    donors_report.sort(reverse=True)
    writereport(donors_report)




if __name__ == "__main__":
    while True:
        print("What do you want to do?")
        response = input("1. Send a Thank You, 2. Create a Report, 3. Quit: ")
        if response == '1':
            thankyou()
        elif response == '2':
            createreport()
        elif response == '3':
            exit()