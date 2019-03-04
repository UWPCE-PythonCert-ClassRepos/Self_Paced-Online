"""Ian Sahlberg
Assignment 4 mailroom2
Python 210
01/02/2019"""

#for file dating
import datetime as dt
#Dictionary of donors name, dollar amount
donors = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00],
         'tim tam':[10.50],
         'roxanne raffle':[13.00, 75.00, 123.00],
         'jon jacob':[5000.00, 5.00]
         }

#Dictionary of user options
user_select = {0:'1 - Send a Thank You', 1:'2 - Create a Report', 2:'4 - quit', 3:'3 - Send letters to everyone', 4:'Enter an option: List (to give a list of names), A donors full name, \"Menu\" to return to main menu.', 5:'How much did they donate?'}

def donate():
    """Appends a donation amount to a given donor."""
    amount = int(input(user_select.get(5)))
    return amount


def amount_append(name, dictionary, amount):
    return dictionary[name].append(amount)

def print_list(dictionary):
    """Prints our the donor list"""
    return list(dictionary.keys())

def email(name, amount):
    """Create email for specific donor and amount donated."""
    return 'Thank you {} for the generous donation of $ {:.2f}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n'.format(name.title(), amount)

def quit():
    """Quit the program"""
    print('Until next time!')
    return 'Until next time!'

def sort_and_stats_dict(dictionary):
    """Create a stats dictionary from a donor dictionary and sort by total donated."""

    pre_sort = {k: [sum(v), len(v), round((sum(v) / len(v)), 0)] for k, v in dictionary.items()}
    donor_sorted = sorted(list(pre_sort.items()), key=lambda x: x[1], reverse=True)
    return donor_sorted

def print_report(stats_dictionary):
    """Print out a report of donors and amounts donated, including stats (total donated, number of times donated, average donation)."""
    # access indexed results in stats dictionary
    print_out = 'Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations\n,----------------------------------------------------------------------------------------\n'
    for name, donor in stats_dictionary:
        print_out += f'{name:<20}$    {donor[0]:<23.2f}{donor[1]:<15}    ${donor[2]:>12.0f}\n'
    return print_out


def email_file(dictionary):
    """Generates a thank you letter and writes to disk for all donors."""
    import datetime as dt

    count = 0
    for name, donations in dictionary.items():
        amount = sum(donations)
        file_name = '{}_{}.txt'.format(name, dt.date.today())
        count += 1
        with open(file_name, 'w+') as file:
            e_text = email(name, amount)
            file.write(e_text)
    return print('Emails written to file.')

def user_action1(dict):
    "Runs through donors and donor amount options. Appends donation amounts to the donors list"
    option = input(user_select.get(4))
    if option.lower() == 'menu':
        return 'menu'

    if option.lower() == 'list':
        print(print_list(dict))
        return user_action1(dict)

    else:
        if option.lower() in dict:
            amount = donate()
            amount_append(option, dict, amount)
            print(email(option, amount))
            return user_action1(dict)

        else:
            dict[option] = []
            amount = donate()
            amount_append(option, donors, amount)
            print(email(option, amount))
            return user_action1(dict)

def user_action2(dict):
    #Prints a report of donors and stats details"
    donor_sorted = sort_and_stats_dict(dict)
    return print_report(donor_sorted)

switchitdic = {1 : lambda : user_action1(donors), 2 : lambda :print(user_action2(donors)), 3 : lambda : email_file(donors), 4 : lambda : quit()}

#---------------------------------------------------------------
#Work Zone

x = True
while x:
    option1 = int(input('Please choose from the following options: \n1 - Send a Thank You \n2 - Create a Report \n3 - Send letters to everyone \n4 - quit'))
    y = switchitdic.get(option1)()
    if y == 'Until next time!':
        x = False
    elif y == 'menu':
        continue

