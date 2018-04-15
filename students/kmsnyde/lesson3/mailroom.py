# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:31:38 2018

@author: Karl M. Snyder
"""

#[[fill]align][sign][#][0][minimumwidth][.precision][type]

donor_data = [['Karl Stick', [10, 20, 30]],
               ['Kate Stam', [5, 30]], 
               ['Christine Goose', [21]],
               ['Matt Hen', [40, 5, 11]],
               ['Zumi Was', [32]]]

def send_1():
    print('\nType a user\'s name or "list" to show names.')
    input1 = input('-> ')
    if input1 == 'list':
        for name in donor_data:
            print(name[0])
        send_1()
    elif any(input1 in i for i in donor_data):
        input2 = float(input('Donation amount: '))
        for i, item in enumerate(donor_data):
            if donor_data[i][0] == input1:
                donor_data[i][1].append(input2)
                print('Thank you {} for your donation in the amount of ${:02.02f}; it is very generous.'\
                      .format(input1, input2))
    else:
        donor_data.append([input1])
        input3 = float(input('Donation amount: '))
        donor_data[-1].append([input3])
        print('Thank  you {} for your donation in the amount of \
                      ${:02.02f}; it is very generous.'\
                      .format(input1, input3))
        
def create_2():
    names = [data[0] for i, data in enumerate(donor_data)]
    sums = [sum(data[1]) for i, data in enumerate(donor_data)]
    donations = [len(num_donations[1]) for i, num_donations in
                 enumerate(donor_data)]
    averages = [sum(data[1])/len(data[1]) for i, data in
                enumerate(donor_data)]
    sum_data = zip(names, sums, donations, averages)
    sum_data = sorted(sum_data, key=lambda x: x[1], reverse=True)
    print('{:<20} {:>20} {:>20} {:>20}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift'))
    print('{}'.format('-' * 83))
    for line in sum_data:
        print('{:<20} {:>20.02f} {:>20} {:>20.02f}'.format(line[0], line[1], line[2], line[3]))

if __name__ == "__main__":
    user_input = None
    while user_input != 3:
        print('\nPick your selection (1, 2, 3)')
        print('1: Send a Thank You.')
        print('2: Create a Report.')
        print('3: Quit')
        user_input = int(input('\nMake your selection: '))
        if user_input == 1:
            send_1()
        elif user_input == 2:
            create_2()