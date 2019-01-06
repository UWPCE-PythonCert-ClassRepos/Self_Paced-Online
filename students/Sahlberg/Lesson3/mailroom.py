"""Ian Sahlberg
Assignment 3 mailroom
Python 210
12/28/2018"""


#Disctionary of donors name, dollar amount
donor = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00],
         'tim tam':[10.50],
         'roxanne raffle':[13.00, 75.00, 123.00],
         'jon jacob':[5000.00, 5.00]
         }

def donate(name, dictionary):
    """Appends a donation amount to a given donor."""
    amount = int(input('How much did they donate?'))
    return amount, dictionary[name].append(amount)

def print_list(dictionary):
    """Prints our the donor list"""
    return print(list(dictionary.keys()))

def user_options():
    """Main user options menu choices."""
    user_action = input('Please choose from the following options: Send a Thank You, Create a Report, quit')
    return user_action

def email(name, amount):
    return print(f'\n\nThank you {name.title()} for the generous donation of $ {amount:.2f}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n')

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

if __name__== '__main__':
    user_action = user_options()

    if user_action.lower() == 'quit':
        quit()

    while user_action == 'Send a Thank You':
        option = input('Enter an option: List (to give a list of names), A donors name, \"quit\" , to quit.')
        if option.lower() =='quit':
            print('Bye!')
            break
        if option.lower() == 'list':
            print_list(donor)
        else:
            if option.lower() in donor:
                amount = int(donate(option,donor)[0])
                print(donor)
                email(option,amount)

            else:
                donor[option] = []
                amount = int(donate(option,donor)[0])
                print(donor)
                email(option,amount)

    while user_action == 'Create a Report':
        donor_sorted = sort_and_stats_dict(donor)
        print('Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations')
        print('----------------------------------------------------------------------------------------')
        count = 0
        for donor in donor_sorted:
            print(
                f'{donor_sorted[count][0]:<20}$    {donor_sorted[count][1][0]:<23.2f}{donor_sorted[count][1][1]:<15}    ${donor_sorted[count][1][2]:>12.0f}')
            count += 1
        break

