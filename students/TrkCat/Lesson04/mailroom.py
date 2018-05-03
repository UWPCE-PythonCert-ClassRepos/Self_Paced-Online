#!/usr/bin/env python

def send_thank_you():
    """Print a thank you email"""
    donate_prompt = ('\n\nSend a Thank You Letter:\n'
                 'Please select an option from the list:\n'
                 '1 - Send a Thank You for New Donation\n'
                 '2 - List Current Donors\n'
                 '3 - Exit to Main Menu\n'
                 '>> '
                )
    donate_menu = {'1': add_donation,
                   '2': list_donors,
                   '3': quit_menu
                  }
    show_menu(donate_prompt, donate_menu)
    
  
def create_report():
    """Print a donation report"""
    sorted_donors = sorted(donors.values(), key = lambda v:v['tot_don'], 
                           reverse = True)
    # Add in dynamic column widths in future iteration
    header = ' | '.join(('     Donor Name    ','Total Given','Num Gifts',
             'Average Gift'))
    print('\n' + header)
    print('-' * len(header))
    for donor in sorted_donors:
        print(('{name:20s}  $ {tot_don:>10.2f}   {num_don:>9d}'
               '  $ {avg_don:>10.2f}').format(**donor))
    

def send_all_letters():
    write_dir = input('\nWhich directory should the letters be writen in?: ')
    if not write_dir:
        write_dir = '.'
    for donor in donors.values():
        letter = gen_email()
        file_name = donor['name'] + '.txt'
        print('Writing Letter: {}'.format(file_name))
        with open('/'.join([write_dir, file_name]),'w') as f:
            f.write(letter.format(**donor))
    print('\nAll letters complete.\n')
  
  
def add_donation():
    """Add donation amount to list under donors name"""
    donor_name = input("\nPlease enter donor's full name: ")
    if donor_name.lower() not in donors:
        donors[donor_name.lower()] = {'name': donor_name}
    cur_dict = donors[donor_name.lower()]
    donation = float(input('Enter the donation amount: '))
    cur_dict.setdefault('donations',[]).append(donation)
    cur_dict['last_don'] = donation
    update_tot_avg(cur_dict)
    letter = gen_email()
    print(letter.format(**cur_dict))
    return False


def list_donors():
    """Print list of current donors"""
    print('\n\nCurrent Donors:\n')
    for donor in donors.values():
        print(donor['name'])
    
    
def gen_email():
    """Return a thank you email"""
    letter = ('\nFROM: Your friendly local charity mailroom.\n'
              'TO: {name}\n'
              'RE: Your recent donation\n\n'
              '\nThank you so much for your recent donation of'
              ' ${last_don:,.2f}. This will go a long way towards helping to'
              ' save the pythons. Your generosity is most appreciated!'
              '\n\nBest Regards,\nSave The Pythons\n'
             )
    return letter
  
  
def quit_menu():
    """Quit current menu"""
    return False
    
    
def update_tot_avg(d):
    """Update total and average donation value in dict d."""
    d['tot_don'] = sum(d['donations'])
    d['num_don'] = len(d['donations'])
    d['avg_don'] = d['tot_don']/d['num_don']
    
    
def show_menu(prompt, disp_dict):
    """Generate menu with dispatch dictionary"""
    while True:
        sel = input(prompt)
        if disp_dict[sel]() is False:
            return False
     
     
if __name__ == '__main__':      
    donors = {'bill gates': {'name': 'Bill Gates',
                             'donations': [789.25,87562.22,125000.00],
                             'last_don': 125000                          
                            },                              
              'jeff bezos': {'name': 'Jeff Bezos',
                             'donations': [3456.89,130],
                             'last_don': 130
                            }, 
              'jimmy buffett': {'name': 'Jimmy Buffett',
                                'donations': [85000],
                                'last_don': 85000
                               },
              'abe lincoln': {'name': 'Abe Lincoln',
                              'donations': [5,2,1],
                              'last_don': 1
                             },
              'yankee doodle': {'name': 'Yankee Doodle',
                                'donations': [67],
                                'last_don': 67
                               }                          
             }

    for donor in donors.values():
        update_tot_avg(donor)
    
    main_prompt = ('\n\nMain Menu:\n\n'
                   'Please select an option from the list:\n'
                   '1 - Send a Thank You\n'
                   '2 - Create a Report\n'
                   '3 - Send Thank You Letters to All\n'
                   '4 - Quit Menu\n'
                   '>> '
                  )
    main_menu = {'1': send_thank_you, 
                 '2': create_report,
                 '3': send_all_letters,
                 '4': quit_menu
                }  
    show_menu(main_prompt, main_menu)