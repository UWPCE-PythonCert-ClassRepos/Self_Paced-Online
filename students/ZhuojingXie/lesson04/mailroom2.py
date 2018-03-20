#!/usr/bin/env python3

import sys
import os

data = [{'name':'Andy','donation':[960,256,123.5,40]},{'name':'Bryce','donation':[30,45,27]},
        {'name':'Charile','donation': [25,50]},{'name':'David', 'donation':[10]},
        {'name':'Elaine','donation':[75,26]}]

def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == 'exit menu':
            break

def sub1_menu():
    menu_selection(sub1_prompt,sub1_dispatch)

def quit():
    return 'exit menu'

def thankletter(Name,Money):
    print(f'\nDear {tuple[0]}, \n\n'
         'Thank you so much for very generous donation of $'+f'{tuple[1]} to our chaple\n'
         '\n\nRespectfully'
         '\nZhuojing Xie')

def list_name():
    for info in data:
        print(info['name'])
    donator =input('\n\nPlease input the name or the donator > ')
    money = input('\n\nThank you for donation , please type '
                'the money you want to donate > ')
    while not money.isdigit():
        money = input('\n\nPlease type number only > ')
    for info in data:
        if donator == info['name']:
            info['donation'].append(float(money))
        else:
            data.append({'name':donator,'donation':[float(money)]})
            break
    menu_selection(main_prompt,main_dispatch)

def creat_a_report():
    print('{:<20}'.format('Donor Name')+'| '+
          '{:<15}'.format('Total Given')+'| '+'{:<15}'.format('Num Gifts')+'| '+'{:<15}'.format('Average Gift'))
    print('='*68)

    for info in data:
        print(f'{info["name"]:<20}'+f'$ {sum(info["donation"]):<16}' + f'{len(info["donation"]):<16}'+
              f'$ {(sum(info["donation"])/len(info["donation"])):<16}')
    menu_selection(main_prompt,main_dispatch)


def send_letters_to_everyone():
    for info in data:
        name = info['name']
        amount = info['donation'][-1]
        with open(name+'.txt', 'w') as wf, open("template.txt", 'r') as rf:
            for line in rf:
                wf.write(line.replace('{name}', name).replace('{amount:.2f}',str(amount)))

def exit():
    sys.exit()

main_prompt = ('\n\nPlease select a action: \n1 Send a Thank You!'
               ' \n2 Create a Report  \n3 Send letters to everyone \n4 Quit \n\n  >')
sub1_prompt = ('\n\nType "list" to show a list of the donor names, \n'
                'Or type "back" to Back\n')
main_dispatch ={'1':sub1_menu,'2':creat_a_report,'3':send_letters_to_everyone,'4':exit}
sub1_dispatch ={'list':list_name, 'back':quit}

menu_selection(main_prompt,main_dispatch)
