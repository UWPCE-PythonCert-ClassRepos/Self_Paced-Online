# Sending a Thank you
def sendingthank(donors):
    f_name = input('Please type the Full Name or list> ')
    while f_name == 'list':
        print(' ')
        for x in donors:
            print(x)
        print(' ')
        f_name = input('Please type the Full Name or list> ')
    if donors.get(f_name, False):
        s = 'Existing donor, please type the donation amount from {}> '
        amount = input(s.format(f_name))
        donors[f_name].append(float(amount))
    else:
        s = 'New donor, please type the donation amount from {}> '
        amount = input(s.format(f_name))
        donors[f_name] = [float(amount)]
    print('\n', "Thank you {} for the generous donation!".format(f_name), '\n')
    return


# Creating Report
def createreport(donors):
    s = '\n, {:<20}| {:<10} | {:<10}| {:<20}'
    print(s.format('Donor Name', 'Total Given', "Num Gift", "Average Gift"))
    print('-' * 60)
    total = []
    for keys in donors:
        num_gift = len(donors[keys])
        total.append([sum(donors[keys]), num_gift, keys])
    total.sort(reverse=True)
    s = '{:<20}  $ {:<10.2f}  {:^12} $ {:<20.2f}'
    for i in range(len(total)):
        print(s.format(total[i][2], total[i][0], total[i][1], total[i][0] / total[i][1]))
    print(' ')
    return


def sendletters(donors):
    for keys in donors:
        s = "{}.txt".format(keys)
        f = open(s, "w+")
        f.write("Dear {},".format(keys))
        f.write("\n\n     Thank you for your very kind donation of ${:<10.2f}".format(sum(donors[keys])))
        f.write('\n\n     It will be put to very good use.')
        f.write('\n\n             Sincerely,')
        f.write('\n                   -The Team')
        f.close()


def main():
    # Mailroom
    response = '0'
    # menu_prompt
    while not (response == '4'):
        print('Menu')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print('3. Send letters to everyone')
        print('4. Quit')
        response = input("Please type number from menu > ")
        switch_func_dict = {'1': sendingthank, '2': createreport, '3': sendletters}
        if not response == '4':
            switch_func_dict.get(response)(donors)


if __name__ == "__main__":
    donors={'William Gates, III':[54842.49,48965.25],'Mark Zuckerberg':[7852.25,48652.0,3548.0],'Jeff Bezos':[5486.0,58794.02,7412.1],'Paul Allen':[46872.02]}
    main()
