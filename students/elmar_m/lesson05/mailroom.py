#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson05: Mailroom Exercise Part 3
'''
import time, collections, sys

main_p = '\n> Main menu. Options: t == thankyou | r == report | q == quit program\n'
sub_p = '\n>> Sub menu "thankyou". Options: l == list current donors | a == add donation / donor | m == send mail to every donor | x == exit submenu\n'

donors = collections.defaultdict(list)
 
donors['berta'] = [90, 9.01, 0.99]
donors['bill'] = [2000, 7.5, 950000]
donors['steve'] = [5.5, 234000, 928]
donors['donald'] = [657, 234, 28.57, 90456]
donors['angie'] = [2, 99, 297765, 47, 28346]
donors['kim'] = [38982, 66.23, 9856, 0.1]


def writefile(name, content):
    '''
    Create mail files
    
        ARGS:
    name: filename / name of donor
    content: mail body text
    '''
    ts = time.strftime('%Y%m%d-%H%M%S')
    fname = '{}.{}.txt'.format(name, ts)
    try:
        # with open(fname, 'w') as f:
        with open(fname, 'x') as f:     # intentionally doing it with 'x' to be able to test a FileExistsError
            f.write(content)
            return True
    except (OSError, FileExistsError, IsADirectoryError, PermissionError) as e:
        print('>> EXCEPTION ALERT trying to write', fname, ':', e)
        return False


def mail():
    '''
    Create mail body text for every donor
    '''
    for i in donors:
        text = '''Dear {},\n 
    Thank you very much for your very kind donation of ${}.\n
    It will be put to very good use.\n
        Sincerely,
             -The Team'''.format(i, donors[i][-1])
        if writefile(i, text):
            print('>> mailfile created for', i, 'in your current working directory')
        else:
            print('>> ERROR: could not create mailfile for', i)
            


def thankyou():
    '''
    # Show list of known donors, add new donor to list, 
    # add new donation to donor and print letter of thanks.
    Start submenu
    '''
    menu(sub_p, sub_d)


def list_donors():
    '''
    Print list of donors
    '''
    print('\n'.join(donors))
    return '\n'.join(donors)
    

def add():
    '''
    Add new donation and / or donor
    '''
    while True: 
        dname = input('>> Please give donor name: ')
        if not dname.isalpha():
            print('>> only alphabetical characters in donor name allowed, please try again')
            continue
        else:
            break
    if dname in donors:
        print('>>', dname, 'already in list')
        add_amount(dname)
    else:
        print('>>', dname, 'not in list, adding it ')
        add_amount(dname)


def add_amount(donor):
    '''
    Add donation amount
        
        ARGS:
    donor: name of donor
    '''
    while True:
        amount = input('>> please add current donation (int or float, use \'.\' as decimal separator):\n>> ')
        # make sure given donation values are positive: 
        if '-' in amount:
            print('>> only positive integers or floats allowed.')
            continue
        # Throw exception and ask again, if given value is not int or float:
        try:
            donors[donor].append(float(amount))
            break
        except ValueError:
            print('>> only numerical values allowed, please try again')
    print(amount, 'added to donation list of', donor, ', thank you')     


def report():
    '''
    Print a formatted list of current donors and donations
    '''
    # get the highest number of digits to create formatstring accordingly:
    sumlist = []
    for i in donors.values():
        sumlist.append(sum(i))
    maxn = len(str(max(sumlist)))
    maxn += 2
    fstring = '{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' 
    print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
    print('-' * (maxn + 54)) 
    for i in donors:
        print(fstring.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) 


def efunc():
    '''
    Exit menu
    '''
    print('exiting.\n')
    return 'exiting'


main_d = {
    # Dispatcher dictionary main menu
    't' : thankyou,
    'r' : report,
    'q' : efunc,
    }


sub_d= {
    #Dispatcher dictionary submenu
    'l' : list_donors,
    'a' : add,
    'x' : efunc,
    'm' : mail,
    }


def menu(p, d):
    '''
    Display menu to user. 
    This function uses a "dispatcher dictionary".

        ARGS:
    p:  prompt which is shown to the user
    d:  the dispatcher dictionary which holds the menu options
    '''
    try:
        while True:
            response = input(p)
            if d[response]() == 'exiting':
                break
    except KeyError:
        print('sorry, unknown option:', response)
        print(p)
        menu(p, d)

	
if __name__ == '__main__':
    menu(main_p, main_d)
