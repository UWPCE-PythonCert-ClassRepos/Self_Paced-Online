#!/usr/bin/env python

def send_thank_you():
    """Print a thank you email"""
    while True:
        donor_name = input("Please enter donor's full name: ")
        if donor_name.lower() == 'list':
            print('\nCurrent Donors:')
            print(donor_names,'\n')
        elif donor_name.lower() == 'quit':
            return
        elif not donor_name in donor_names:
            add_donor(donor_name)
            break
        else:
            break
      
    donation = float(input('Enter the donation amount: '))
    add_donation(donor_name,donation)

    write_email(donor_name,donation)
  
  
def create_report():
    """Print a donation report"""
    donors_report = create_donor_summary()
    #Add in dynamic column widths in future iteration
    header = ' | '.join(('Donor Name' + ' ' * 10,'Total Given','Num Gifts',
             'Average Gift'))
    print('\n' + header)
    print('-' * len(header))
    for donor in donors_report:
        print('{:20s}  $ {:>10.2f}   {:>9d}  $ {:>11.2f}'.format(*donor))
    
    
def create_donor_summary():
    donors_report = []  
    for donor in donors:
        num_don = len(donor[1:])
        tot_don = sum(donor[1:])
        donors_report.append([donor[0], tot_don, num_don, tot_don/num_don])
    return sorted(donors_report, key=lambda v:v[1], reverse=True)
  
  
def add_donor(donor_name):
    """Add a donor to donor list"""
    donors.append([donor_name])
    donor_names.append(donor_name)
  
  
def add_donation(donor_name, amount):
    """Add donation amount to list under donors name"""
    for donor in donors:
        if donor[0] == donor_name:
            donor.append(amount)
            return

        
def write_email(donor_name, amount):
    """Print a thank you email"""
    print('\nFROM: Your friendly local charity mailroom.')
    print('TO: {}'.format(donor_name))
    print('RE: Your recent donation')
    print('\nThank you so much for your recent donation of ${:,.2f}. This will'
          ' go a long way towards helping to save the pythons. Your generosity'
          ' is most appreciated!'.format(amount))
    print('\nBest Regards,\nSave The Pythons\n')
  
  
if __name__ == '__main__':
    donors = [['Bill Gates',789.25,87562.22,125000.00],
              ['Jeff Bezos',3456.89,130],['Jimmy Buffett',85000],
              ['Abe Lincoln',5,2,1],['Yankee Doodle',67]]
    donor_names = [donor[0] for donor in donors]

    while True:
        main_menu = input('\nSelect an option: "Send a Thank You", '
                          '"Create Report", "quit" > ')
        if main_menu.lower() == 'send a thank you':
            send_thank_you()
        elif main_menu.lower() == 'create report':
            create_report()
        elif main_menu.lower() == 'quit':
            break
        else:
            print('Please select an option from the list.')
