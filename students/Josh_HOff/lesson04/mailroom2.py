donors_list = {'Ralph Anders': [5, 10], 'Andrei Wasinski': [101, 151, 75], 'Stalk Holmes': [40], 'Traci Johnston': [20], 'James Hendrick': [60], 'Angelica Kisel': [45, 25, 55.60]}
donor = ''
donation = 0

def send_email(donor):
    donation = sum(donors_list.get(donor))
    print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')

def send_thank_you():
    print('thank you')
    while True:
        print('')
        donor = input('Type a Full Name: ')
        if switch_func_dict.get(donor, continue_func)() == False:
            return
        elif donor != 'list':
            print('')
            donation = input('What is the donation amount?: ')
            if donation == 'quit':
                return
            donation = float(donation)
            if donor in donors_list:
                donors_list[donor] += [donation]
            else:
                donors_list[donor] = [donation]
            print(donors_list)
            print('')
            print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')
            
            
def print_list():
    print('')
    for i in donors_list:
        print(i)
    return True
    
def create_report():
    print('created report')
    print('')
    y = '|'
    print(f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift')
    print('-' * 63)
    
    
    donation = sum(donors_list.get(donor))

    
    
    
    
    
    
    
    
    
    
    
def quitting():
    print('time to quit')
    return False
    
def letters_to_everyone():
    print('create txt files with thank you letters in each one')
    
def continue_func():
    print('continuing the function')
    return True
    
switch_func_dict = {'1':send_thank_you, '2':create_report, '3':letters_to_everyone, '4':quitting, 'quit':quitting, 'list':print_list}
#main function
if __name__ == "__main__":
    while True:
        send_thank_you_set = set(donors_list)
        a = input('1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \n Choose an Option: ')
        if switch_func_dict.get(a, continue_func)() == False:
            break