#!/usr/bin/env python3

donor_info = [
             ['Ernest Hemingway',[35, 65.25, 40]],
             ['John Steinbeck',[25.50, 20, 10]], 
             ['Joseph Heller',[45, 20, 105.50]],
             ['Kurt Vonnegut', [60, 40, 400]],
             ['Michael Chabon', [100, 200, 300, 400]]
             ]

def start_program():
    """Prompt user for desired donor action and fulfill the request"""
    exit_program = False
    while not exit_program:
        selection = input('''Please enter a selection (1-3): 
                           1. Send a thank you
                           2. Create a report
                           3. Quit
                           ''')
        if selection=='1':
            send_thankyou()
        elif selection=='2':
            create_report()
        elif selection=='3':
            exit_program = True
        else:
            print('Your selection was not recognized')


def send_thankyou():
    """Send a thank you note to person designated by user; add person to
       donor_info if they aren't already there"""
    while True:
        name = input('Please enter full name:\n')
        if name == 'list':
            print('This is the list of donor names:\n')
            for item in donor_info:
                print(item[0])
        else:
            donation = float(input('Please enter donation amount:\n'))
            for i, item in enumerate(donor_info):
                if name == item[0]:  # The name is already in donor_info
                    donor_info[i][1].append(donation)  # Add current donation
                    break
            else:  #The name was not found
                donor_info.append([name, [donation]])

            print(f'Dear {name}:\nThank you for your generous donation of',
                  f'${donation:.2f}. We really appreciate it!')
            break
    return


def create_report():
    """Print summary report of donor info"""
    max_donor_width = 0
    for i in donor_info:
        if len(i[0])>max_donor_width:
            max_donor_width = len(i[0])
    print('{:{}}|{:12}|{:10}|{:8}'.format('Donor Name', max_donor_width, 
          'Total Given', 'Num Gifts', 'Average Gift'))
    donor_info.sort(key = lambda x: sum(x[1]))
    for donor in donor_info:
        print('{:{}}|${:^11.2f}|{:^10}|${:^8.2f}'.format(donor[0], 
            max_donor_width, sum(donor[1]), len(donor[1]), 
            sum(donor[1])/len(donor[1])))


if __name__ == '__main__':
    start_program()