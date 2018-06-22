#!/usr/bin/env python3
# lesson04 mailroom part2
from operator import itemgetter

__author__="Wieslaw Pucilowski"

# initial donors list
donors_hist = [
            ['Richard Lionheart', 100.5, 36.30, 230],
            ['Andreas Bolen', 220, 1000],
            ['Ivan Smirnoff', 1200],
            ['Karl Marx', 345.2, 140.20],
            ['Alvaro Speedy', 330, 850, 100.50],
			['Ilunga Mulungma', 350, 550],
            ['Denis Donuts', 68],
			['Haruto Asai', 45, 997.50],
			['Great Gatsby', 0.5],
        ]

# build all user dictionary based on initial donors list
dict_all={}
for item in donors_hist:
    dict_all[(item[0].split()[0], item[0].split()[1])]=item[1:]
    
def donor_greeting(first, last):
    if select_user(first, last) is None:
        greetings=""
    else:
        greetings="""
        Ex Programmers Charity
        1999 Heartbeat Avenue
        11111 Fresh Spring, Alaska
        
        Dear {first_name} {last_name},
        
        Thank you so much for your generous donation of ${total}
        
        It will be put to very good use.

                           Sincerely,
                              -The Team
        
        """.format(**select_user(first,last))
    return greetings

def write_letter(first, last):
    message=donor_greeting(first, last)
    if message:
        f=open(first+'_'+last+'.txt', 'w')
        f.write(message)
        f.close()

def send_letter_all():
    print("Sending letters to all donors...")
    for donor in dict_all.keys():
        write_letter(donor[0], donor[1])
        
def print_greetings(first, last):
    message=donor_greeting(first, last)
    if message:
        print(message)
        
def select_user(first, last):
    if (first, last) in dict_all.keys():
        # print(dict_all[(first,last)])
        # print(len(dict_all[(first,last)]))
        # print(sum(dict_all[(first,last)]))
        return {'first_name': first, 'last_name': last, 'donations': len(dict_all[(first,last)]), 'total':sum(dict_all[(first,last)])}
    else:
        return None
        
def list_donors():
    for donor in sorted(dict_all.keys()):
        print("{} {},".format(donor[0], donor[1]))
        
def add_donor():
    name = input("Type donor first and last name: ")
    if len(name.split()) >= 2:
        first, last = name.split()[0], name.split()[1]
    else:
        print("Only First name added")
        first = name.split()[0]
        last=""
    donation=input("Donation in USD: ")
    while not donation.isdigit():
        donation=input("Donation in USD: ")
    add_donor_dict(first,last, float(donation))
    print_greetings(first, last)

def add_donor_dict(first,last, donation):
    if (first, last) in dict_all.keys():
        dict_all[(first,last)].append(donation)
    else:
        dict_all[(first,last)]=[donation]

def custom_key(a):
    return sum(a[1])
    
def create_report():
    print("Creating a report...\n")
    print( "{:<30}| {:<18}| {:<8}| {:<18}".format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print("{:-<80}".format(''))
    for k,v in sorted(dict_all.items(), key=custom_key, reverse=True):
        print('{:<30}{}{:>18.2f}{:>11}{}{:>17.2f}'.format(k[0]+' '+k[1], ' $', sum(v), len(v), ' $', sum(v)/len(v)))

def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict.get(response, "default") == "default":
            print(response,wrong_option)
            continue
        elif dispatch_dict[response]() == "exit menu": # mind dispatch_dict[response] return function and following () call it
            break

wrong_option = "{:<20}".format(" - Wrong option !!!")

def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)
    
def quit():
    print("Goodbye...\n")
    return "exit menu"
    
main_prompt = """
    {:-^30}
    
    1 - Send a Thank You
    2 - Create a Report
    3 - Send letters to everyone
    q - Quit
""".format(' Main Menu ')

main_dispatch = {'1': sub_menu,
                 '2': create_report,
                 '3': send_letter_all,
                 'q': quit,
                }

sub_prompt = """
    {:-^30}

    1 - Add new donor, donation
    2 - List donors
    q - Go to Main Menu
    
""".format(' Add/List donors ')

sub_dispatch = {'1': add_donor,
                '2': list_donors,
                'q': quit,
               }


    

if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)