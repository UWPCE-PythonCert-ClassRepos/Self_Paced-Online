from datetime import date

#dictionary to hold donors and list of donation amounts
letter_directory = 'temp/'
donation_dict = {}
donor_dict = {}

def is_number(n):
    try: 
        float(n)
        return True
    except:
        return False

def send_thank_you():
    """ 
        prompt user for name and donation amount, add to donation dictionary 
        provide list of names if user enters \'list\' as name
        send a thank you email to the donor for donation
    """

    name = 'list'
    while name == 'list':
        name = input("Provide full name: ")
        if name == 'list':
            for donor in donation_dict:
                print(donor)
    
    amount = float(input("Provide a donation amount:"))
    amount_list = donation_dict[name] if name in donation_dict else [] 
    amount_list.append(amount)
    donation_dict[name] = amount_list    
    donor_dict[name] = { 'firstname': name.split(' ')[0], 'lastname': name.split(' ')[1] }
    thank_you_string = f"Hi {name}\nThank you for your donation of {amount} to the mailroom!\n"
    print(thank_you_string)    

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
        data_row = "{0:20}  ${1:>15}   {2:>10}   ${3:>15}".format(donor, str(donation_total), str(donation_count), str(donation_average))
        print(data_row)

def write_letters():
   for donor,name_dict in donor_dict.items():
       first_name = name_dict['firstname']
       last_name = name_dict['lastname']
       amount_list = donation_dict[donor]
       donation_num = 1
       for donation_amt in amount_list:      
           message = f"Dear {first_name} {last_name},\n\n    Thank you for your very kind donation of ${donation_amt}.\n\n    It will be put to very good use.\n\n    Sincerely,\n        -The Team"
           with open(f"{letter_directory}{first_name}_{last_name}_{donation_num}.txt",'w') as f:
               f.write(message)
           donation_num += 1

if __name__ == '__main__':
    #build initial dictionary of donors and donation amounts
    donor_list = ['Fred Smith','Terrie Ann','Murray Martin','Josh Jones','Jane Doe']
    amount_list = [ 500, 100, 1000]
    #donor_donation_dict = { datetime.date(2008, 6, 24): 500, datetime.date(2010, 8, 13): 100, datetime.date(2013, 1, 16),1000 }
    for donor in donor_list:
        first_name = donor.split(' ')[0]
        last_name = donor.split(' ')[1]
        donor_dict[donor] = { 'firstname': first_name, 'lastname': last_name }    
        donation_dict[donor]= amount_list[:] 
    

    #prompt user for action and then call function
    action_dict = { 1: send_thank_you, 2: create_report, 3: write_letters, 4: quit }
    action = 0
    while not is_number(action) or int(action) != 4:
        action = input('What would you like to do: 1 - \“Send a Thank You\”, 2 - \“Create a Report\” or 3 - \"Send letters to everyone\" or 4 - \“quit\”\n')
        
        if not is_number(action) or int(action) < 1 or int(action) > 4:
            print("please enter a number 1-4")
        else:
            action_dict[int(action)]()

