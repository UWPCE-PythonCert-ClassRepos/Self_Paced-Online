# Sending a Thank you
def sendingthank(donors):
    f_name = input('Please type the Full Name or list> ')
    while f_name == 'list':
        print(' ')
        for x in donors:
            print(x[0])
        print(' ')
        f_name = input('Please type the Full Name or list> ')
    for x in range(len(donors)):
        if f_name == donors[x][0]:
            name_exists = True
            break
        else:
            name_exists = False
    if name_exists is False:
        s = 'New donor, please type the donation amount from {}> '
        amount = input(s.format(f_name))
        donors = donors + [[f_name, float(amount)]]
    else:
        s = 'Existing donor, please type the donation amount from {}> '
        amount = input(s.format(f_name))
        donors[x] = donors[x] + [float(amount)]
    print('\n', "Thank you {} for the generous donation!".format(f_name), '\n')
    return donors


# Creating Report
def createreport(donors):
    s = '\n, {:<20}| {:<10} | {:<10}| {:<20}'
    print(s.format('Donor Name', 'Total Given', "Num Gift", "Average Gift"))
    print('-' * 60)
    for x in range(len(donors)):
        total = sum(donors[x][1:])
        num_gift = len(donors[x]) - 1
        s = '{:<20}  $ {:<10.2f}  {:^12} $ {:<20.2f}'
        print(s.format(donors[x][0], total, num_gift, total / num_gift))
    print(' ')
    return donors


def main():
    # Mailroom
    donors=[['William Gates, III',54842.49,48965.25],['Mark Zuckerberg',7852.25,48652.0,3548.0],['Jeff Bezos',5486.0,58794.02,7412.1],['Paul Allen',46872.02]]
    response = '0'
    # menu_prompt
    while not (response == '3'):
        print('Menu')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print('3. Quit')
        response = input("Please type number from menu > ")
        if response == '1':
            donors = sendingthank(donors)
        if response == '2':
            donors = createreport(donors)


if __name__ == "__main__":
    main()
