from datetime import date

#dictionary to hold donors and list of donation amounts
donation_dict = {}

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
    donation_list = donation_dict[name] if name in donation_dict else [] 
    donation_list.append(amount)
    donation_dict[name] = donation_list    
    thank_you_string = f"Hi {name}\nThank you for your donation of {amount} to the mailroom!\n"
    print(thank_you_string)    

def create_report():
    """ Print a list of donors, sorted by total historical donation amount"""
    title = "{0:20} | {1:15} | {2:10} | {3:15}".format('Donor Name','Total Given','Num Gifts','Average Gift')
    print(title)
    
    #sort the dictionary by descending order of the sum of values 
    sorted_dict = sorted(donation_dict.items(), key=lambda x: sum(int(v) for v in x[1]),reverse=True)
    for donor, donation_list in sorted_dict:
        donation_count = len(donation_list)
        donation_total = sum(int(v) for v in donation_list)
        donation_average = round(donation_total/donation_count,2)
        data_row = "{0:20}  ${1:>15}   {2:>10}   ${3:>15}".format(donor, str(donation_total), str(donation_count), str(donation_average))
        print(data_row)
        
    
if __name__ == '__main__':
    #build initial dictionary of donors and donation amounts
    donor_list = ['Fred Smith','Terrie Ann','Murray Martin','Josh Jones','Jane Doe']
    amount_list = [500,100,1000]
    for donor in donor_list:
        donation_dict[donor]=amount_list
    

    #prompt user for action and then call function
    action = 0
    while not is_number(action) or int(action) != 3:
        action = input('What would you like to do: 1 - \“Send a Thank You\”, 2 - \“Create a Report\” or 3 - \“quit\”\n')
        
        if not is_number(action) or int(action) < 1 or int(action) > 3:
            print("please enter a number 1-3")
        elif int(action) == 1:
            send_thank_you()
        elif int(action) == 2:
            create_report()
    
