donationHistory = {'Tony Lee': [100.0], 'Michelle Cao': [100.0, 200.0], 'Andy Arko': [300.0], 'Tom Ludwinski': [200.0]}

def thankyou():
    name = input("Please enter the full name: ")
    while name == "list":
        for donorName in donationHistory.keys():
            print(donorName)
        name = input("Please enter the full name: ")

    if name not in donationHistory.keys():
        donationHistory[name] = []

    donationAmount = input("Please enter the donation amount: ")
    donationHistory[name].append(float(donationAmount))

    print(f'Thank you {name}, for your donation of {donationAmount}!')

def report():
    for name, donationAmount in donationHistory.items():
        print('{:20}|{:15}|{:10}|{:12}'.format(name, sum(donationAmount), len(donationAmount), sum(donationAmount)/len(donationAmount)))

def send_letter():
    for name, donationAmount in donationHistory.items():
        with open(name+'.txt', 'w') as letterFile:
            letterFile.write('Thank you {}, for your donation of {}!'.format(name, sum(donationAmount)))

if __name__ == '__main__':
    OptionSelect = {
         1: thankyou,
         2: report,
         3: send_letter
    }

    choice = 0
    while(choice != 4):
        choice = input('''Please choose from a menu of 3 actions:\n
                    1 - Send a Thank You
                    2 - Create a Report
                    3 - Send letters to everyone
                    4 - Quit\n''')
        choice = int(choice)
        if choice >=1 and choice < 4:
            OptionSelect[choice]()
