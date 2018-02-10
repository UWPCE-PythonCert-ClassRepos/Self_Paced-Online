#!/usr/bin/env python3

import sys
data=[['Andy',[960,256,123.5,40]],['Bryce',[30,45,27]],
      ['Charile', [25,50]],['David', [10]],
      ['Elaine',[75,26]]]
# this is my data form


def prompt():
    user_select = input("\n\nPlease select a action: \n1 Send a Thank You!"
                        "\n2 Create a Report  \n3 Quit\n\n  >")
    while not user_select.isdigit():
        user_select = input(" Please type a number")
    while user_select not in ['1','2','3']:
        user_select = input("\n\nPlease try again, select a action:\n1 Send a Thank You!"
                            "\n2 Create a Report.  \n3 Quit\n\n  >")
    return user_select
# main menu



def donor_name():
    donor_list=[]
    for info in data:
        donor_list.append(info[0])
    return donor_list
#this function gonna return a list of donaor, and it will be used in thankprompt function later

def thankprompt():
    user_select_thank=input('\n\nType "list" to show a list of the donor names, \n'
                            'Or type "back" to Back\n')
    while user_select_thank.lower() != 'back' and user_select_thank.lower() != 'list':
        user_select_thank=input('\n\nType "list" to show a list of the donor names, \n'
                            'Or type "back to Back\n\n')

    if user_select_thank == 'list':
        print('\n')
        for name in donor_name():
            print(name)
        a = newdonation()
        thankletter(a)
        main()

    if user_select_thank.lower() =='back':
        main()
#This function is when user select 1

def newdonation():
    donator =input('\n\nPlease input the name or the donator > ')
    money = input('\n\nThank you for donation , please type '
                'the money you want to donate > ')
    while not money.isdigit():
        money = input('\n\nPlease type number only > ')
    if donator in donor_name():
        for info in data:
            if info[0] == donator:
                info[1].append(float(money))
    else:
        new_donator_info = [donator,[float(money)]]
        data.append(new_donator_info)
    return donator, money
#this functio will append in data list if it is a new new_donator
#as an old donator, it will only save money amount in data


def thankletter(tuple):
    print(f'\nDear {tuple[0]}, \n\n'
         'Thank you so much for very generous donation of $'+f'{tuple[1]} to our chaple\n'
         '\n\nRespectfully'
         '\nZhuojing Xie')
#this function is only using for generating the thankletter after donation

def report():
    print('{:<20}'.format('Donor Name')+'| '+
          '{:<15}'.format('Total Given')+'| '+'{:<15}'.format('Num Gifts')+'| '+'{:<15}'.format('Average Gift'))
    print('='*68)

    for info in data:
        print(f'{info[0]:<20}'+f'$ {sum(info[1]):<16}' + f'{len(info[1]):<16}'+
              f'$ {(sum(info[1])/len(info[1])):<16}')
    main()

#this function will Create a report

def main():
    a = prompt()
    if a == '1':
        thankprompt()
    elif a =='2':
        report()
    elif a == '3':
        sys.exit()
#this is my main function

if __name__ == '__main__':
    main()
