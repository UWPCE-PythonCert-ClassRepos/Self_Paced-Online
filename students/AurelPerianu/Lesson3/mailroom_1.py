#!/usr/bin/env python3

#mailroon1

"""
Write a small command-line script called mailroom.py.
This script should be executable.
The script should accomplish the following goals:
-It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
-This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
-The script should prompt the user to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”
"""
donors = [['donor_a', 3580, 34124.31, 7654 ], ['donor_b', 110.55, 3500],
            ['donor_c', 11000], ['donor_d',2233.1, 6543.74,4567.35],
            ['donor_e',546123, 99.10, 23555,19], ['donor_f',78.75, 21.75]]
options = ["Send a Thank You", "Create a Report", "Quit"]

def donor_list(lst):
    """
    Create donor name list from the original donor combined list
    """
    lc=[]
    for i in lst:
        lc.append(i[0])
    return lc

def donor_stat(lst):
    """
    Generate total donations for each donor
    """
    lc=[]
    for i in lst:
        lx=[]
        lx.append(i[0])
        lx.append(sum(i[1:]))
        lx.append(len(i[1:]))
        lx.append(sum(i[1:])/len(i[1:]))
        lc.append(lx)
    lc.sort(key=lambda e: e[1], reverse=True)
    #print (x)
    return lc

def add_donor(nm, lst):
    return lst.append([nm])

def add_donat(lst, nm, amt=0):
    lx=donor_list(lst)
    #lx.index(nm)
    if nm not in lx or amt<=0:
        print ('Name not on the list or no valid amount.\n')
        return
    else:
        lst[lx.index(nm)].append(amt)
        return lst
def letter(name, amount):

    txt = """\n
            To:       {0:s}
            Subject:  Your donation of ${1:,.2f}
            Dear {0:s},\n

            Thank you for you donation of ${1:,.2f} to our fundation.\n
     """
    print (txt.format(name, amount))
    #return

def thank_you(lst):
    """
    Function to select existing donors or add new donor, add a donation and sent a thank you letter
    """
    while True:
        x=input('\nEnter: donor name; list; quit :\n')
        #x=x.lower()
        lx=donor_list(lst)
        if x=='quit':
            return (lst)
            #break
        elif x=='list':
            print ('\nExisting donors:\n', donor_list(lst))
            #print(donors)
        elif x not in lx and x not in ['list','quit']:
            print ('\nAdd new donor: ',x)
            add_donor(x, lst)
            lx=donor_list(lst)
        if x in lx and x not in ['list','quit']:
            try:
                print ('\nEnter a donation amount for donor:', x)
                amt=input()
                amt=float(amt)
                add_donat(lst, x, amt)
                letter(x, amt)
            except:
                print('\nWrong amount. Try again','\n')

def report(lst):
    """
    Generate the summary report for all donors.
    """
    print('\n')
    print ('Donor Name'+' '*16+'|'+' '*9+'Total Given'+' |'+' '*6+'Num Gifts'+' |'+' '*8+'Average Gift')
    print('-'*26+'|'+'-'*21+'|'+'-'*16+'|'+'-'*20+'|')
    #print (lst)
    for d in lst:
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                d[0], d[1],d[2],d[3]))
    print ('\n')

def donor_options(lst):
    """
    Menu for mailroom application
    """
    while True:
        for i, j in enumerate(options):
             print(i + 1, j+'\n')
        x=input('\nSelect an option (1,2,3):')
        try:
            x = int(x)
            if x ==1:
                #print ('\nSend a Thank You',x,'\n')
                thank_you(lst)
            elif x==2:
                #print ('\nCreate a Report',x,'\n')
                report(donor_stat(lst))
            elif x==3:
                #print (lst)
                print ("\nGood Bye\n")
                return
            else:
                print ('\nWrong option. Try again','\n')
        except ValueError:
            print('\nWrong option. Try again','\n')

if __name__=='__main__':
    donor_options(donors)
