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

#for file dating
import datetime as dt

#Dictionary of donors name, dollar amount
donor = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00],
         'tim tam':[10.50],
         'roxanne raffle':[13.00, 75.00, 123.00],
         'jon jacob':[5000.00, 5.00]
         }

#Dictionary of user options
user_select = {0:'1 - Send a Thank You', 1:'2 - Create a Report', 2:'4 - quit', 3:'3 - Send letters to everyone', 4:'Enter an option: List (to give a list of names), A donors name, \"quit\" , to quit.', 5:'How much did they donate?'}

def donate(name, dictionary):
    """Appends a donation amount to a given donor."""
    amount = int(input(user_select.get(5)))
    return amount#, dictionary[name].append(amount)

def amount_append(name, dictionary, amount):
    return dictionary[name].append(amount)

def print_list(dictionary):
    """Prints our the donor list"""
    return print(list(dictionary.keys()))

def user_options():
    """Main user options menu choices."""
    user_action = input('Please choose from the following options:  \n'+ user_select.get(0) + '\n'+ user_select.get(1) + '\n'+ user_select.get(3)+ '\n'+ user_select.get(2))
    return user_action

def email(name, amount):
    """Create email for specific donor and amount donated."""
    return 'Thank you {} for the generous donation of $ {:.2f}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n'.format(name.title(), amount)

def quit():
    """Quit the program"""
    return print('Until next time!')

def sort_and_stats_dict(dictionary):
    """Create a stats dictionary from a donor dictionary and sort by total donated."""
    pre_sort = {k: [sum(v), len(v), round((sum(v) / len(v)), 0)] for k, v in dictionary.items()}
    print(pre_sort)
    donor_sorted = sorted(list(pre_sort.items()), key=lambda x: x[1], reverse=True)
    return donor_sorted

def print_report(dictionary):
    """Print out a report of donors and amounts donated, including stats (total donated, number of times donated, average donation)."""
    print('Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations')
    print('----------------------------------------------------------------------------------------')
    count = 0
    for donor in dictionary:
        print(
            f'{dictionary[count][0]:<20}$    {dictionary[count][1][0]:<23.2f}{dictionary[count][1][1]:<15}    ${dictionary[count][1][2]:>12.0f}')
        count += 1

def email_file(dictionary):
    """Generates a thank you letter and writes to disk for all donors."""
    print(dictionary.items())
    count = 0
    count_file = 0
    for name in dictionary.keys():
        amount = [sum(v) for v in dictionary.values()][count]
        file_name = '{}_{}.txt'.format(name, dt.date.today())
        count += 1
        with open(file_name, 'w+') as file:
            e_text = str(email(name, amount))
            count_file += 1
            file.write(e_text)
    return print('Emails written to file.')

#---------------------------------------------------------------
#Work Zone
if __name__== '__main__':
    print_list(donor)

    user_action = user_options()

    if user_action.lower() == 'quit':
        quit()

    while user_action == '1':
        option = input(user_select.get(4))

        if option.lower() == 'quit':
            print('Bye!')
            break

        if option.lower() == 'list':
            print_list(donor)
        else:
            if option.lower() in donor:
                amount = donate(option,donor)
                amount_append(option,donor,amount)
                print(donor)
                email(option,amount)

            else:
                donor[option] = []
                amount = donate(option,donor)
                amount_append(option, donor, amount)
                print(donor)
                email(option,amount)

    while user_action == '2':
        donor_sorted = sort_and_stats_dict(donor)
        print_report(donor_sorted)
        break

    while user_action == '3':
        """print(donor.items())
        count = 0
        count_file = 0
        for name in donor.keys():
            amount = [sum(v) for v in donor.values()][count]
            file_name = '{}_{}.txt'.format(name, dt.date.today())
            count += 1
            with open(file_name, 'w+') as file:
                e_text = str(email(name, amount))
                count_file += 1
                file.write(e_text)
        break"""
        email_file(donor)
        break


