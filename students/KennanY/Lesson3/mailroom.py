donations = [
            ['Bill Gates', 165234, 42335.37, 21000,4400],
            ['Jack Ma', 94834.44, 239102.23,9984],
            ['Jeff Bezos', 1234534,234123],
            ['Kate Jones', 948374.44, 987362.12],
            ['Walt Kistler', 1234, 4444, 38476.34],
            ['Jerry Paros', 110,44,85,8854]]

def createReport():
    """Print donation history"""
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

def PrintEMail(name, amount):
    ''' Print Email message'''
    print("\nDear " + name +'\n')
    print('We would like to thank you for continuing support for our organization!\n')
    print('Your contribution of $' + str(amount) + ' is received and very much appreciated!')
    print('\nThank you\nKennan Yilmaz')

def send_ThankYou():
    ''' Send a Thank you note'''
    donorname=input('Type donor name or ''list'' to see all the names=')

    if donorname=='list':
        #List all donots if user enters 'list'
        for donor in donations:
            print(donor[0])
    else: #It is assumed that name entered in this case
        # Prompt for donation amount
        amount = float(input('Please enter the donation amount='))
        #Is it in the db?
        # If in database, append value else create a new record
        found=False
        for loc in range(0,len(donations)):
            if donorname == donations[loc][0]:
                found=True
                break

        if found:
            #Append at the end
            donations[loc].append(amount)
        else:
            # Create new record since it does not exist
            new_record = [donorname, amount]
            donations.append(new_record)

        #Print the email now
        PrintEMail(donorname,amount)

def showmenu ():
    """Displays the menu options"""
    select=True
    while select:
        print('\n')
        print("====== Main Menu ======")
        print('1. Send a Thank You')
        print('2. Create a Report')
        print ('3. Quit')
        response=input("Please select and option (1,2 or 3)")
        if str(response)=='1':
            send_ThankYou()
        elif str(response)=='2':
            createReport()
        elif str(response)=='3':
            print('Finished ...')
            break
        else:
            select=True

if __name__ == '__main__':
    showmenu()