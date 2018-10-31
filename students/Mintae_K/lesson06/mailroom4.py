# Error Handling function for sending_thank function
def check_error(amount):
    try:
        checked_amount = float(amount)
        return 1
    except ValueError:
        print('\nValue entered is not a number. Only number allowed.\n')
        return 0


# Adding donation to existing person or creating new donation data
def check_name_exist(f_name, donors):
    if donors.get(f_name):
        s = 'Existing donor, please type the donation amount from {}> '
        return 1, s
    else:
        s = 'New donor, please type the donation amount from {}> '
        return 0, s


def append_donation(f_name, amount, yes_exist, donors):
    #global donors
    if yes_exist == 1:
        donors[f_name].append(float(amount))
    else:
        donors[f_name] = [float(amount)]
    return donors


# Sending a Thank you
def sending_thank():
    f_name = input('Please type the Full Name or list> ')
    while f_name == 'list':
        print(' ')
        for x in donors:
            print(x)
        print(' ')
        f_name = input('Please type the Full Name or list> ')
    (yes_exist, s) = check_name_exist(f_name, donors)
    myexit = 0
    while not myexit == 1:
        amount = input(s.format(f_name))
        myexit = check_error(amount)
    append_donation(f_name, amount, yes_exist, donors)
    print('\n', "Thank you {} for the generous donation!".format(f_name), '\n')


# Creating Report
def create_report():
    s = '\n, {:<20}| {:<10} | {:<10}| {:<20}'
    print(s.format('Donor Name', 'Total Given', "Num Gift", "Average Gift"))
    print('-' * 60)
    total = [[sum(donors[key]), len(donors[key]), key] for key in donors]
    total.sort(reverse=True)
    s = '{:<20}  $ {:<10.2f}  {:^12} $ {:<20.2f}'
    for i in range(len(total)):
        print(s.format(total[i][2], total[i][0], total[i][1], total[i][0] / total[i][1]))
    print(' ')


def send_letters():
    for name in donors:
        s = "{}.txt".format(name)
        with open(s, "w+") as f:
            f.write("Dear {},".format(name))
            f.write("\n\n     Thank you for your very kind donation of ${:<10.2f}".format(sum(donors[name])))
            f.write('\n\n     It will be put to very good use.')
            f.write('\n\n             Sincerely,')
            f.write('\n                   -The Team')
        f.closed


def just_quit():
    print('\n You have exited')


def main():
    # Mailroom
    response = '0'
    # menu_prompt
    switch_func_dict = {'1': sending_thank, '2': create_report, '3': send_letters, '4': just_quit}
    while not response == '4':
        print('Menu')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print('3. Send letters to everyone')
        print('4. Quit')
        response = input("Please type number from menu > ")
        try:
            switch_func_dict.get(response)()
        except TypeError:
            print('\n Please type a number from 1 to 4.\n')
    return response


if __name__ == "__main__":
    donors = {'William Gates, III':[54842.49,48965.25],'Mark Zuckerberg':[7852.25,48652.0,3548.0],'Jeff Bezos':[5486.0,58794.02,7412.1],'Paul Allen':[46872.02]}
    main()
