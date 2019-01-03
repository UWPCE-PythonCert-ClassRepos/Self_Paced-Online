"""Ian Sahlberg
Assignment 4 mailroom2
Python 210
01/02/2019"""
"""In this version, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter, 
and writes it to disk as a text file.

Your main menu may look something like:

Choose an action:

1 - Send a Thank You
2 - Create a Report
3 - Send letters to everyone
4 - Quit
The letters should each get a unique file name – derived from the donor’s name, and maybe a date.

After running the “send letters to everyone” option, you should get a bunch of new files in the working dir – one for each donor.

After choosing (3) above, I get these files in the dir I ran it from:

Jeff_Bezos.txt
Mark_Zuckerberg.txt
Paul_Allen.txt
William_Gates_III.txt
(If you want to get really fancy, ask the user for a directory name to write to!)"""

#Dictionary of donors name, dollar amount
donor = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00],
         'tim tam':[10.50],
         'roxanne raffle':[13.00, 75.00, 123.00],
         'jon jacob':[5000.00, 5.00]
         }

#Dictionary of user options
user_select = {0:'1 - Send a Thank You', 1:'2 - Create a Report', 2:'4 - quit', 3:'How much did they donate?', 4:'Enter an option: List (to give a list of names), A donors name', 5:'3 - Send letters to everyone'}

def donate(name, dictionary):
    """Appends a donation amount to a given donor."""
    amount = int(input(user_select.get(3)))
    return amount, dictionary[name].append(amount)

def print_list(dictionary):
    """Prints our the donor list"""
    return print(list(dictionary.keys()))

def user_options():
    """Main user options menu choices."""
    user_action = input('Please choose from the following options:  \n'+ user_select.get(0) + '\n'+ user_select.get(1) + '\n'+ user_select.get(5)+ '\n'+ user_select.get(2))
    return user_action

def email(name, amount):
    return print('\n\nThank you {} for the generous donation of $ {}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n'.format(name, amount))

def quit():
    return print('Until next time!')

def sort_and_stats_dict(dictionary):
    pre_sort = {k: [sum(v), len(v), round((sum(v) / len(v)), 0)] for k, v in dictionary.items()}
    print(pre_sort)
    donor_sorted = sorted(list(pre_sort.items()), key=lambda x: x[1], reverse=True)
    return donor_sorted

def print_report(dictionary):
    print('Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations')
    print('----------------------------------------------------------------------------------------')
    count = 0
    for donor in dictionary:
        print(
            f'{dictionary[count][0]:<20}$    {dictionary[count][1][0]:<23.2f}{dictionary[count][1][1]:<15}    ${dictionary[count][1][2]:>12.0f}')
        count += 1


print_list(donor)

user_action = user_options()

if user_action.lower() == 'quit':
    quit()

while user_action == '1':
    option = input(user_select.get(4))
    if option.lower() == 'list':
        print_list(donor)
    else:
        if option.lower() in donor:
            amount = donate(option,donor)[0]
            print(donor)
            email(option,amount)

        else:
            donor[option] = []
            amount = donate(option,donor)[0]
            print(donor)
            email(option,amount)

while user_action == '2':
    donor_sorted = sort_and_stats_dict(donor)
    print_report(donor_sorted)
    break

while user_action == '3':
    for name in donor.keys():
        amount = (sum(v) for v in donor.values())
        file_name = '{}.txt'.format(name)
        with open(file_name, 'w+') as file:

            file.write(email(name, amount))

    "{k: [sum(v), len(v), round((sum(v) / len(v)), 0)] for k, v in dictionary.items()}"
