donations = [
            ['Bill Gates', 165234, 42335.37, 21000,4400],
            ['Jack Ma', 94834.44, 239102.23,9984],
            ['Jeff Bezos', 1234534,234123],
            ['Kate Jones', 948374.44, 987362.12],
            ['Walt Kistler', 1234, 4444, 38476.34],
            ['Jerry Paros', 110,44,85,8854]]

def createReport():
    """Print donation history"""

    print('Donor name                        Total given       Number of gifts         Average gift')
    print('=' *60)

    for donor in donations:
        total_amount=sum(donor[1:])
        total_donation=len(donor)-1
        avg_donation=total_amount/total_donation
        #print(total_amount)
        #print(total_donation)
        #print(avg_donation)
        print('{:<25s}  ${:>18,.2f}  {:>15d}  ${:>18,.2f}'.format( donor[0], total_amount, total_donation,
                                                                      avg_donation))

def send_ThankYou():
    ''' Send a Thank you note'''
    response=input('Type a name or ''list'' to see all the names=')

    #if user types in 'list' print all donors
    if response=='list':
        for donor in donations:
            print(donor[0])
    elif response=='quit':
        print ('Quit') # exit
    else: #For everything else
        for donor in donations:
            for donor in donations:
                if response == donor[0]:
                    donor.append([1])
                    break
            else:
                #if name is new, add and prompt for donation
                return

def showmenu ():
    """Displays the menu options"""
    select=True
    while select:
        print('\n')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print ('3. Quit')
        response=input("Please select and option (1,2 or 3)")
        print(response)
        if str(response)=='1':
            print('Thank you')
            send_ThankYou()
        elif str(response)=='2':
            print('Create report')
            createReport()
        elif str(response)=='3':
            print('Finished ...')
            break
        else:
            select=True


if __name__ == '__main__':
    showmenu()