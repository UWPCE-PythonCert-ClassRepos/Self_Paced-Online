#!/usr/bin/env python3

donors = ['papa', 'mama', 'bompa', 'bobonne', 'onbekende']
donations = [[100, 5, 15], [12, 200, 2, 66], [1000], [500, 500], [1000000]]

def thankyou():
    '''If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure
    and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for their
    generous donation. Print the email to the terminal and return to the original
    prompt.'''
    name = input('Please enter a name or type "list" to see a list of names > ')
    while name == 'list':
        print(donors)
        name = input('Please enter a name or type "list" to see a list of names > ')
    if not name in donors:
        donors.append(name)
        donations.append([])
    donation = input('Please enter a donation amount > ')
    donations[donors.index(name)].append(donation)
    print(f'Dear {name} , thank you very much for your generous donation of\
    {donation}. Looking forward receiving even more money next time.')
    print(donors)
    print(donations)

def report():
    ''' If the user (you) selected “Create a Report”, print a list of your donors,
     sorted by total historical donation amount.
     Include Donor Name, total donated, number of donations and average donation
     amount as values in each row. You do not need to print out all their
     donations, just the summary info.
     Using string formatting, format the output rows as nicely as possible.
     The end result should be tabular (values in each column should align with
     those above and below)
     After printing this report, return to the original prompt.
     At any point, the user should be able to quit their current task and return
     to the original prompt.
     From the original prompt, the user should be able to quit the script cleanly.'''
    print(f'{"Donor Name":20s} {"|  Total Given":20s} {"|  Num Gifts  |":20s} {"Average Gift":20s}')
    print(f'{"-"*80}')
    for name in donors:
        print(f'{name:20s} ${sum(donations[donors.index(name)]):20.2f}\
        {len(donations[donors.index(name)]):12d}\
        ${sum(donations[donors.index(name)])/len(donations[donors.index(name)]):20.2f}')

if __name__ == '__main__':
    response = input('Please choose between the following 3 actions:\
    1. Send a Thank You; 2. Create a Report; 3. quit >  ')
    while response != '3':
        if response == '1':
            thankyou()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. quit >  ')
        if response == '2':
            report()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. quit >  ')
