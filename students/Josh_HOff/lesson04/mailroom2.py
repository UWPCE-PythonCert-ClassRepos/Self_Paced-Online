arg_dict = {0:'zero', 1:'one', 2: 'two'}
donors_list = {'Ralph Anders': [5, 10], 'Andrei Wasinski': [101, 151, 75], 'Stalk Holmes': [40], 'Traci Johnston': [20], 'James Hendrick': [60], 'Angelica Kisel': [45, 25, 55.60]}
donor = 'Ralph Anders'

def send_email(donor):
    donation = sum(donors_list.get(donor))
    print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')

def send_thank_you():
    print('thank you')

#    print((donors_list['Ralph Anders'])
    
def create_report():
    print('created report')
    
def quitting():
    print('time to quit')
    return False
    
def letters_to_everyone():
    print('create txt files with thank you letters in each one')
    
switch_func_dict = {1:send_thank_you, 2:create_report, 3:letters_to_everyone, 4:quitting}

#main function
if __name__ == "__main__":
    while True:
        a = int(input('1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \n Choose an Option: '))
        if switch_func_dict.get(a)() == False:
            break