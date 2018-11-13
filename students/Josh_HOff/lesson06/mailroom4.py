import pathlib
import os
import sys
donors_list = {'Ralph Anders': [5, 10], 'Andrei Wasinski': [101, 151, 75], 'Stalk Holmes': [40], 'Traci Johnston': [20], 'James Hendrick': [60], 'Angelica Kisel': [45, 25, 55.60]}
donor = ''
donation = 0
tab = '    '
sorted_donors = ()
rows = ''
top = ''

#this function gets a donor's name and donation amount and adds them both to the donor list.
def send_thank_you():
    while True:
        print('')
        donor = input('Type a Full Name: ')
        truthcheck = check_input(donor)
        if truthcheck == False:
            return
        elif truthcheck == True:
            continue
        else:
            while True:
                print('')
                donation = input('What is the donation amount?: ')
                truthcheck = check_donation(donor, donation)
                if truthcheck == False:
                    return
                elif truthcheck == True:
                    continue
                else:
                    add_donation_to_list(donor, donation)
                return
                
def add_donation_to_list(donor, donation):
    global donors_list
    donation = float(donation)
    if donor in donors_list:
        donors_list[donor] += [donation]
    else:
        donors_list[donor] = [donation]
    print(f'\nHello, {donor}! Thank you very much for your generous \
donation of ${donation:.2f}! Your contribution is essential and \
will be well utilized.\n')

                
def check_input(donor):
    if donor == 'quit':
        return False
    elif donor == 'list':
        switch_func_dict.get(donor, continue_func)()
        return True
        
        
def check_donation(donor, donation):
    if donation == 'quit':
        return False
    try:
        donation = float(donation)
    except ValueError:
        print("Please give a number instead.")
        return True
    return

    #this function prints out a list of the donors in the donor list.         
def print_list():
    print('')
    names = [i for i in donors_list]
    print(names)

#this function prints out a report on the prompt screen.    
def create_report():
    print(donors_list)
    print('')
    y = '|'
    rows = ''
    global sorted_donors
    reportvariable = f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift\n'
#    reportvariable = top
    reportvariable += ('-' * 63)
#    reportvariable += top
    sorted_donors = sorted(donors_list.items(), key=lambda k: sum(k[1]), reverse=True)
    for donor_name, donations in sorted_donors:
        gift = len(donations)
        average = ( sum(donations) / gift)
        rows += f'\n{donor_name:<23} $ {sum(donations):>11.2f} {gift:>11} {average:>11.2f}'
    reportvariable += rows
    print(f'\n{reportvariable}\n')
    return reportvariable
    
#this function quits the previous menu.    
def quitting():
    sys.exit()

#this function creates files for all donors in the donor list.
def letters_to_everyone():
    for i, val in donors_list.items():
        with open(f'{i}.txt', 'w') as outfile:
            donation = sum(val)
            outfile.write(f'Dear {i}, \n\n{tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company')

#this function will continue the previous while loop and prevents errors if a user enters an unexpected input.
def continue_func():
    return
    
    
switch_func_dict = {'1':send_thank_you, '2':create_report, '3':letters_to_everyone, '4':quitting, 'quit':quitting, 'list':print_list}

#main function
if __name__ == "__main__":
    while True:
        a = input('1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \nChoose an Option: ')
        switch_func_dict.get(a, continue_func)()