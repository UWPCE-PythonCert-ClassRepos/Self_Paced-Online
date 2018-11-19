"""
Author: Alyssa Hong
Date: 11/04/2018
Update:
Lesson4 Assignments > Mailroom, Part 2
"""

#!/usr/bin/env python3

import os


list_col = ['Donor Name','Total Given','Num Gifts','Average Gift']
#list of donation : donor_name,[total_given,num_gifts,avg_gift]
list_donation = {'Fred':[7000,4500],'Alex':[30000,30000,10000],\
                'Henry':[5000],'Alyssa':[120000,30000,40000],\
                'Leo':[107000,53500]}


def send_thanks():
    user_input = input("Do you want to see the list of donor? Please type 'list'--> ")
    if user_input == "list":
        show_list_donation(list_donation)
        donor_name = input("Type the donor's name: ")
        new_donation = int(input("Type your donations: "))
        if donor_name not in list_donation.keys():
            list_donation.update({donor_name: [new_donation]})
        else:
            list_donation[donor_name] += [new_donation]
        #print the email
        print('\n' + 'Dear {:s}, thank you for your ${:.2f} donation!'.format(donor_name,new_donation) + '\n')
        #return to the original prompt
        show_list_donation(list_donation)
    else:
        print("Please type 'list' or quit")

    # return_menu()


def create_report():
    show_list_donation(list_donation)
    # return_menu()


def send_letters():
    for i, j in list_donation.items():
        writepath = i + '.txt'
        # mode = 'a' if os.path.exists(writepath) else 'w'
        if os.path.exists(writepath):
            mode = 'a'
        else:
            mode = 'w'

        with open(writepath, mode) as f:
            f.write(letter_content(i, j))


    # return_menu()

def letter_content(donor_name, donation):
   #  \n : line change
   #  \t : to add space using tap
    content = 'Dear {},'.format(donor_name) + '\n'*2 + '\t'*1 + 'Thank you for your donation of ${:.2f}.'.format(sum(donation))+'\n' + '\t'*1 + 'It will be put to very good use.\n'+'\t'*5 +'Sincerely,\n' + '\t'*5 +'-The Team'
    return content


def show_list_donation(list_donation):
    print('{:<20} | {:^10} | {:^10} | {:^10}'.format(*list_col))
    print('{}'.format("-"*63))

    list_donation = dict(sorted(list_donation.items(), key=lambda x: x[1], reverse=True))
    for i, j in list_donation.items():
        donor_name = i
        total_given = sum(j)
        num_gifts = len(j)
        avg_gift = total_given/num_gifts
        result = '{:<20}   ${:>10,.2f}   {:>10}   ${:>10,.2f}'.format(donor_name,\
                  total_given,num_gifts,avg_gift)
        print(result)

    print('{}'.format("-"*63))


def return_menu():
    print('\n''Choose the menu again or Quit!')
    main()


def main():
    print('\n'
          'Choose an action\n'
          '1 - Send a Thank you\n'
          '2 - Create a Report\n'
          '3 - Send letters to everyone\n'
          '4 - Quit')
    while True:
        choice_action = int(input(': '))
        if choice_action == 1:
            send_thanks()
        elif choice_action == 2:
            create_report()
        elif choice_action == 3:
            send_letters()
        elif choice_action == 4:
            print('Quit current task!')
            break


if __name__ == '__main__':
    main()
