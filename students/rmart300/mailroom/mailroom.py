from datetime import date
import os

# dictionary to hold donors and list of donation amounts
letter_directory = 'temp/'
donor_list = ['Fred Smith', 'Terrie Ann', 'Murray Martin', 'Josh Jones', 'Jane Doe']
donation_dict = {}
donor_dict = {}

def is_number(n):
    """ tests conversion to float """
    try: 
        float(n)
        return True
    except ValueError:
        return False

def send_thank_you():
    """
        prompt user for name and donation amount, add to donation dictionary
        provide list of names if user enters \'list\' as name
    """

    name = 'list'
    while name == 'list':
        name = input("Provide full name: ")
        if name == 'list':
            for donor in donation_dict:
                print(donor)

    amount = input("Provide a donation amount:")
    thank_you_message = validate_and_create_thank_you(name, amount)
    print(thank_you_message)

def validate_and_create_thank_you(name, amount):
    """ send a thank you email to the donor for donation """

    if not is_number(amount):
        return 'invalid donation amount: ' + str(amount)  
 
    try:
        name.split()[1]
    except IndexError as e:
        return 'Could not send thank you.  The first and last name of donor must be provided\n'
    else:
        donor_dict[name] = { 'firstname': name.split()[0], 'lastname': name.split()[1] }
        amount_list = donation_dict[name] if name in donation_dict else []
        amount_list.append(amount)
        donation_dict[name] = amount_list
        return f"Hi {name}\nThank you for your donation of {amount} to the mailroom!\n"

def create_report():

    """ Print a list of donors, sorted by total historical donation amount"""
    title = "{0:20} | {1:15} | {2:10} | {3:15}".format('Donor Name','Total Given','Num Gifts','Average Gift')
    print(title)
    
    #sort the dictionary by descending order of the sum of values 
    sorted_dict = sorted(donation_dict.items(), key=lambda x: sum(int(v) for v in x[1]),reverse=True)
    for donor, amount_list in sorted_dict:
        donation_count = len(amount_list)
        donation_total = sum(int(v) for v in amount_list)
        donation_average = round(donation_total/donation_count,2)
        data_row = "{0:20}  ${1:>15}   {2:>10}   ${3:>15}".format(donor, 
            str(donation_total), str(donation_count), str(donation_average))
        print(data_row)

def write_letters():
    """ write letters to every donor in dict """

    #clear files from directory before creating new ones
    for f in os.listdir(letter_directory):
        if '.txt' in f:
            os.remove(letter_directory + f)

    for donor,name_dict in donor_dict.items():
        first_name = name_dict['firstname']
        last_name = name_dict['lastname']
        amount_list = donation_dict[donor]
        donation_num = 1
        for donation_amt in amount_list:      
            message = f"Dear {first_name} {last_name},\n\n    "
            message += f"Thank you for your very kind donation of ${donation_amt}.\n\n    "
            message += f"It will be put to very good use.\n\n    Sincerely,\n"
            message += f"        -The Team"
            with open(f"{letter_directory}{first_name}_{last_name}_{donation_num}.txt",'w') as f:
                f.write(message)
            donation_num += 1

def validate_user_selection(action):
    """ validate the user selection versus available actions """

    key_list = list(action_dict.keys())
    if not is_number(action) or int(action) not in key_list:
        return False
    else:
        return True

action_dict = { 1: send_thank_you, 2: create_report, 3: write_letters, 4: exit }

if __name__ == '__main__':
    # build initial dictionary of donors and donation amounts
    amount_list = [ 500, 100, 1000]
    for donor in donor_list:
        first_name = donor.split(' ')[0]
        last_name = donor.split(' ')[1]
        donor_dict[donor] = { 'firstname': first_name, 'lastname': last_name }    
        donation_dict[donor]= amount_list[:] 

    # prompt user for action and then call function
    action = 0
    while not is_number(action) or int(action) != 4:
        prompt_message = 'What would you like to do: '
        prompt_message += '1 - \“Send a Thank You\”, '
        prompt_message += '2 - \“Create a Report\” or '
        prompt_message += '3 - \"Send letters to everyone\" or 4 - \“quit\”\n'
        action = input(prompt_message)
        
        if not validate_user_selection(action):
            key_list = list(action_dict.keys())
            print("please enter a number {0}-{1}".format(key_list[0],key_list[-1]))
        else:
            action_dict[int(action)]()

