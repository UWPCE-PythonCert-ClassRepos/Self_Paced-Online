#!/usr/bin/env python3

# added exception handling in this version
# added list comprehension
import sys # import sys, so i can use sys.exit(0) later
import io
donation_history = [
                    {'name':'Anna','donations':[100,200,300]},
                    {'name':'Bob','donations':[1000,2000]},
                    {'name':'Chuck','donations':[10000]},
                    {'name':'David','donations':[1]},
                    {'name':'Ethan','donations':[10,20]}
                 ]

def generate_prompt(dispatch_dict):
    
    print('Please type your selection from the above options: ')
    
#  prompt the user (you) to choose from a menu
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == 'exit menu':
                break
        except KeyError:
            print('\nInvalid input. Please only choose from the availalbe options')
# Sending a Thank You
def send_a_thank_you(donation_history = donation_history):
    name = input("\nSend a Thank You. Please provide a name or type 'list' to display current names, or type 'back': ")
    if name != 'back':        
        # If the user types ‘list’, show them a list of the donor names and re-prompt    
        while name == 'list':
            print(list_name())
            name = input('\nSend a Thank You. Please provide a name: ')
        # If the user types a name not in the list, add that name to the data structure and use it.    
        if name not in list_name():
            add_name(name)
        # If the user types a name in the list, use it.  Once a name has been selected, prompt for a donation amount.
        if name in list_name():       
            while True: 
                donation_amount = input('\nPlease provide the amount of donation from {} : '.format(name))
                # added exception handling in this version
                try:
                    add_donation_amount(name, float(donation_amount))
                except ValueError:
                    print('\nInvalid donation ammount. Please enter a valid number.')
                else:
                    break
            print_thankyou_email(name,donation_amount)  
        
# print thank you email
def print_thankyou_email(name,donation_amount):
    print(f"\nDear {name},\n"
        f"Thanks for your generous donation of ${donation_amount}"
        )

# construct list of names
# use list comprehension 
def list_name(donation_history = donation_history):
    namelist = [item['name'] for item in donation_history]
    return namelist     

# add name to the list    
def add_name(name,donation_history = donation_history):
    donation_history.append({'name':name, 'donations':[]})
    print('\nNew name {} has been added to the list'.format(name))
    
def add_donation_amount(name, donation_amount, donation_history = donation_history):
    for item in donation_history:
        if item['name'] == name:
            item['donations'].append(donation_amount)
            break
    
def create_a_report(donation_history=donation_history):
    # create a summary list
    summary_list = create_summary()
    # sort summary list according to the total donation
    sorted_list = summary_list[:]
    sort_list(sorted_list)
    print_report(sorted_list)
    
# print a list
def print_report(list):
    donor_name_width = 20
    total_given_width = 15
    num_gifts_width = 5
    average_gift_width = 15
    seperator_width = 2
    title = ['Donor Name','|','Total Given', '|', 'Num Gifts', '|', 'Average Gift']
    divider = '-'*(donor_name_width+total_given_width+num_gifts_width+average_gift_width+seperator_width*5)
    print('{:<20}{:<2}{:<15}{:<2}{:<5}{:<2}{:<15}'.format(*title))
    print(divider)
    for item in list:
        print('{:<20}{:2}{:15.2f}  {:8} {:>2}{:12.2f}\n'.format(*item))
     
# create a summary list
def create_summary(donation_history=donation_history):
    summary_list = []
    for item in donation_history:
        total = sum(item['donations'])
        number_of_gifts = len(item['donations'])
        average = total/number_of_gifts
        summary_list.append([item['name'],'$',total,number_of_gifts,'$',average])
    return summary_list

# sort summary list according to the total donation
def sort_list(sorted_list):
    #return summary_list.sort(key=sort_by_total_given)
    sorted_list.sort(key=sort_by_total_given,reverse=True)

# get the total given amount 
def sort_by_total_given(list):
    return list[2]
    
# quit
def quit_program():
    print('Quit')
    return 'exit menu'

def send_letters_to_everyone(donation_history = donation_history):
    for item in donation_history:     
        Letter = "Dear {name},\n\n        Thank you for all your very kind donations of ${donations}\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team".format(**item)
        with open(item['name']+'.txt', 'w') as wf:
            wf.write(Letter)
    print("\nAll letters written to files")
   
    
if __name__ == "__main__":
    main_dispatch = {
                '1': send_a_thank_you,
                '2': create_a_report,
                '3': send_letters_to_everyone,
                '4': quit_program
                }
    main_prompt = ("\nYou are in the main menu now!\n"
                "Choose an action:\n\n"
                "1: Send a thank you\n"
                "2: Create a report\n"
                "3: Send letters to everyone\n"
                "4: Quit\n"
                "Type 1,2,3,4 >> "
              )
    menu_selection(main_prompt, main_dispatch)
