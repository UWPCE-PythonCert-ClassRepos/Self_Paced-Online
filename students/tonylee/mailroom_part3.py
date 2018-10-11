donation_history = {'Tony Lee': [100.0], 'Michelle Cao': [100.0, 200.0], 'Andy Arko': [300.0], 'Tom Ludwinski': [200.0]}

def thank_you():
    name = input("Please enter the full name: ")
    while name == "list":
        for donor_name in donation_history.keys():
            print(donor_name)
        name = input("Please enter the full name: ")

    if name not in donation_history.keys():
        donation_history[name] = []

    donation_amount = input("Please enter the donation amount: ")
    try:
        donation_history[name].append(float(donation_amount))
        print(f'Thank you {name}, for your donation of {donation_amount}!')
    except ValueError:
        print("Not a valid donation amount. Please re-enter a valid donation amount.")

def report():
    print('{:20}|{:15}|{:10}|{:15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    for name, donationAmount in donation_history.items():
        print('{:20}|{:15}|{:10}|{:12}'.format(name, sum(donationAmount), len(donationAmount), sum(donationAmount)/len(donationAmount)))

def send_letter():
    for name, donation_amount in donation_history.items():
        with open(name+'.txt', 'w') as letter_file:
            letter_file.write('Thank you {}, for your donation of {}!'.format(name, sum(donation_amount)))

if __name__ == '__main__':
    OptionSelect = {
         1: thank_you,
         2: report,
         3: send_letter
    }

    choice = 0
    while(choice != 4):
        try:
            choice = input('''Please choose from a menu of 3 actions:\n
                    1 - Send a Thank You
                    2 - Create a Report
                    3 - Send letters to everyone
                    4 - Quit\n''')
            choice = int(choice)
            if choice >=1 and choice < 4:
              OptionSelect[choice]()
        except ValueError:
            print("Not a valid choice. Please re-enter a valid selection")
