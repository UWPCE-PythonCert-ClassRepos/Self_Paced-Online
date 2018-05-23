#!/usr/bin/env python3
import sys # import sys, so i can use sys.exit(0) later
donation_history =[
['Anna',100,200,300],
['Bob', 1000,2000],
['Chuck', 10000],
['David', 1],
['Ethan', 10,20]
]

#  prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
def menu():
    actions = ['\nPlease choose from the above options (type a number):','1. Send a Thank You', '2. Create a Report', '3. Quit']
    print(('{}\n'*len(actions)).format(*actions))
    action = ''    
    while action not in ['1','2','3']:
        action = input('Please choose from the above options (type a number): ')
    if action == '1':
        send_a_thank_you()
    elif action == '2':
        create_a_report()
    elif action == '3':
        quit()
        
# Sending a Thank You
def send_a_thank_you(donation_history = donation_history):
    name = input('\nSend a Thank You. Please provide a name (or type \'back\' to go back to main menu): ')
    if name == 'back':        
        menu()
    # If the user types ‘list’, show them a list of the donor names and re-prompt    
    while name == 'list':
        print(list_name())
        name = input('\nSend a Thank You. Please provide a name: ')
    # If the user types a name not in the list, add that name to the data structure and use it.    
    if name not in list_name():
        add_name(name)
    # If the user types a name in the list, use it.  Once a name has been selected, prompt for a donation amount.
    if name in list_name():
        donation_amount = input('\nPlease provide the amount of donation from {} (or type \'back\' to go back to main menu): '.format(name))
        if donation_amount == 'back':        
            menu()    
        add_donation_amount(name, float(donation_amount))
    print_thankyou_email(name,donation_amount)
    menu()
    
    
# print thank you email
def print_thankyou_email(name,donation_amount):
    print(f"\nDear {name},\n"
        f"Thanks for your generous donation of ${donation_amount}"
        )

# construct list of names
def list_name(donation_history = donation_history):
    namelist = []
    for item in donation_history:
        namelist.append(item[0])
    return namelist     

# add name to the list    
def add_name(name,donation_history = donation_history):
    donation_history.append([name])
    print('\nNew name {} has been added to the list'.format(name))
    
def add_donation_amount(name, donation_amount, donation_history = donation_history):
    for item in donation_history:
        if item[0] == name:
            item.append(donation_amount)
            break
    
def create_a_report(donation_history=donation_history):
    # create a summary list
    summary_list = create_summary()
    # sort summary list according to the total donation
    sorted_list = summary_list[:]
    sort_list(sorted_list)
    print_report(sorted_list)
    menu()

# print a list
def print_report(list):
    Donor_name_width = 20
    Total_given_width = 15
    Num_gifts_width = 5
    Average_gift_width = 15
    seperator_width = 2
    title = ['Donor Name','|','Total Given', '|', 'Num Gifts', '|', 'Average Gift']
    divider = '-'*(Donor_name_width+Total_given_width+Num_gifts_width+Average_gift_width+seperator_width*5)
    print('{:<20}{:<2}{:<15}{:<2}{:<5}{:<2}{:<15}'.format(*title))
    print(divider)
    for item in list:
        print('{:<20}{:2}{:15.2f}  {:8} {:>2}{:12.2f}\n'.format(*item))
    
    
# create a summary list
def create_summary(donation_history=donation_history):
    summary_list = []
    for item in donation_history:
        total = sum(item[1:])
        number_of_gifts = len(item) -1
        average = total/number_of_gifts
        summary_list.append([item[0],'$',total,number_of_gifts,'$',average])
    return summary_list

# sort summary list according to the total donation
def sort_list(sorted_list):
    #return summary_list.sort(key=sort_by_total_given)
    sorted_list.sort(key=sort_by_total_given,reverse=True)

# get the total given amount 
def sort_by_total_given(list):
    return list[2]
    
# quit
def quit():
    print('Quit')
    sys.exit(0) # keep python open until closing
    
if __name__ == "__main__":
    menu()
