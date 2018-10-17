import pathlib
import os
donors_list = {'Ralph Anders': [5, 10], 'Andrei Wasinski': [101, 151, 75], 'Stalk Holmes': [40], 'Traci Johnston': [20], 'James Hendrick': [60], 'Angelica Kisel': [45, 25, 55.60]}
donor = ''
donation = 0
tab = '    '

#this function gets a donor's name and donation amount and adds them both to the donor list.
def send_thank_you():
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
            print('')
            print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation:.2f}! Your contribution is essential and will be well utilized.')
            
#this function prints out a list of the donors in the donor list.            
def print_list():
    print('')
    for i in donors_list:
        print(i)
    return True

#this function prints out a report on the prompt screen.    
def create_report():
    print('')
    y = '|'
    print(f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift')
    print('-' * 63)
    temp_set = donors_list.copy()
    for i, val in donors_list.items():
        temp_set[i] = sum(val)        
    temp_set = dict(sorted(temp_set.items(), key=lambda kv: kv[1], reverse=True))
    for i, val in temp_set.items():
        gift = len(donors_list[i])
        average = ( val / gift)
        print(f'{i:<23} $ {val:>11.2f} {gift:>11} {average:>11.2f}')
    print('')    

#this function quits the previous menu.    
def quitting():
    return False

#this function creates files for all donors in the donor list.
def letters_to_everyone():
#    pth = pathlib.Path('./donations/')
#    p = pth.absolute()
#    print(p)
    for i, val in donors_list.items():
        outfile = open(f'{i}.txt', 'w')
        donation = sum(val)
        outfile.write(f'Dear {i}, \n\n{tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company')
        outfile.close()

#this function will continue the previous while loop and prevents errors if a user enters an unexpected input.
def continue_func():
    return True
    
switch_func_dict = {'1':send_thank_you, '2':create_report, '3':letters_to_everyone, '4':quitting, 'quit':quitting, 'list':print_list}
#main function
if __name__ == "__main__":
    while True:
        send_thank_you_set = set(donors_list)
        a = input('1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \nChoose an Option: ')
        if switch_func_dict.get(a, continue_func)() == False:
            break