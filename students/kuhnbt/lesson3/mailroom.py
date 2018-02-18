#!/usr/bin/env python3

donor_info = [
             ['Ernest Hemingway',[35, 65.25, 40]],
             ['John Steinbeck',[25.50, 20, 10]], 
             ['Joseph Heller',[45, 20, 105.50]]
             ]

exit_program = False
while not exit_program:
    selection = input(('Please choose a number:\n1. Send a thank you\n2.', 
                       'Create a report\n3. Quit'))
    if selection==1:
        send_thankyou()
    elif selection==2:
        create_report()
    elif selection==3:
        exit_program = True
    else:
        print('Your selection was not recognized')


def send_thankyou():
    """Send a thank you note to user-designated person; add person to
       donor_info if they aren't already there"""

    name = input('Please enter full name:\n')
    if name == 'list':
        print('This is the list of donor names:\n')
        for item in donor_info:
            print(item[0])
    else:
        donation = float(input('Please enter donation amount:\n'))
        for i, item in enumerate(donor_info):
            if name == item[0]  #The name is already in donor_info
                donor_info[i][1].append(donation)
                break
        else:  #The name was not found
            donor_info.append([name, [donation]])

    print(f'Dear {name}:\nThank you for your generous donation of',
          f'${donation:.2f}. We really appreciate it!')
    return


def create_report():
    max_donor_width = 0
    for i in donor_info:
        if len(i[0])>max_donor_width:
            max_donor_width = len(i[0])
    print('{:{}}|{:12}|{:10}|{:8}'.format('Donor Name', donor_width, 
          'Total Given', 'Num Gifts', 'Average Gift'))
    donor_info.sort(key = lambda x: sum(x[1]))
    for donor in donor_info:
        print('{:{}}|${:^12.2f}|{:^10}|${:^8.2f}'.format(donor[0], 
            donor_width, sum(donor[1]), len(donor[1]), 
            sum(donor[1])/len(donor[1])))

def quit_program():
    pass


if __name__ == 'main':
    pass