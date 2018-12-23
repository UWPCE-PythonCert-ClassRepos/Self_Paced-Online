"""
Author: Alyssa Hong
Date: 11/21/2018
Update:
Lesson4 Assignments > Mailroom, Part 4
"""

#!/usr/bin/env python3

import os


list_col = ['Donor Name','Total Given','Num Gifts','Average Gift']
#list of donation : donor_name,[total_given,num_gifts,avg_gift]
list_donation = {'Fred':[7000,4500],'Alex':[30000,30000,10000],\
                'Henry':[5000],'Alyssa':[120000,30000,40000],\
                'Leo':[107000,53500]}


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def check_list(fc, check_item):
    if fc == "main":
        if check_item in [1,2,3,4]:
            pass
        else:
            raise MyError("Your choice was wrong.\n""Choose an action again!")
    elif fc == "send_thanks":
        if check_item != "list":
            raise MyError("Probably mistyped!\n""Please type 'list' or quit!")


def send_thanks():
    create_report(list_donation)
    donor_name = input("Type the donor's name: ")
    new_donation = int(input("Type your donations: "))
    if donor_name not in list_donation.keys():
        list_donation.update({donor_name: [new_donation]})
    else:
        list_donation[donor_name] += [new_donation]
    print('\n' + 'Dear {:s}, thank you for your ${:.2f} donation!'.format(donor_name, new_donation) + '\n')
    create_report(list_donation)



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



def letter_content(donor_name, donation):
   #  \n : line change
   #  \t : to add space using tap
    content = 'Dear {},'.format(donor_name) + '\n'*2 + '\t'*1 + 'Thank you for your donation of ${:.2f}.'.format(sum(donation))+'\n' + '\t'*1 + 'It will be put to very good use.\n'+'\t'*5 +'Sincerely,\n' + '\t'*5 +'-The Team'
    return content


def create_report(list_donation):
    print('{:<20} | {:^10} | {:^10} | {:^10}'.format(*list_col))
    print('{}'.format("-"*63))

    list_donation = dict(sorted(list_donation.items(), key=lambda x: x[1], reverse=True))
    for i, j in list_donation.items():
        donor_name = i
        total_given = sum(j)
        num_gifts = len(j)
        avg_gift = total_given/num_gifts
        [print('{:<20}   ${:>10,.2f}   {:>10}   ${:>10,.2f}'.format(donor_name,\
                  total_given,num_gifts,avg_gift))]
        # print(result)

    print('{}'.format("-"*63))



def main():
    while True:
        print('\n'
            'Choose an action\n'
            '1 - Send a Thank you\n'
            '2 - Create a Report\n'
            '3 - Send letters to everyone\n'
            '4 - Quit')

        try:
            choice_action = int(input(': '))
            check_list("main", choice_action)
        except MyError as e:
            print(e)
        else:
            pass

        if choice_action == 1:
            try:
                user_input = input("Do you want to see the list of donor? Please type 'list'--> ")
                check_list("send_thanks", user_input)
                send_thanks()
            except MyError as e:
                print(e)
        elif choice_action == 2:
            create_report(list_donation)
        elif choice_action == 3:
            send_letters()
        elif choice_action == 4:
            print('Quit current task!')
            break


if __name__ == '__main__':
    main()
