#!/usr/bin/env python3

donors = [
        ['Jesse Johnson', [150, 345]],
        ['Mary May', [1000, 750]],
        ['Spencer Samuels', [50, 200, 1100]],
        ['Zach Zillow', [85]],
        ['Tina Thompson', [76, 250, 300]]
        ]


def donor_list():
    for donor in donors:
        print(donor[0])


def prompt_user():
    choice = input('Please select from the following: \n1) Send a Thank You \n2) Create a Report \n3) Quit\n')
    return choice


def thank_you():
    select_user = input('Enter a full name: ')
    if select_user == 'list':
        donor_list()
        select_user = input('Enter a full name: ')
    return select_user


def user(select_user):
    user_exists = False
    for item in donors:
        for donor in item:
            if select_user == donor:
                user_exists = True
    if user_exists:
        pass
    else:
        donors.append([select_user, []])
    update_donation = int(input('Please enter donation: '))
    for donor in donors:
        donations = False
        for i in donor:
            if not donations:
                donations = True
                continue
            else:
                if select_user in donor:
                    i.append(update_donation)
    print(donors)
    print('Thank you {} for your thoughtful donation of ${}.'.format(select_user, update_donation))


def create_report():
    title = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20} | {:>17} | {:>17} | {:>17}'.format(*title))
    print('{:-<80}'.format(''))
    for donor in donors:
        a = sum(donor[1])
        b = len(donor[1])
        total = a // b
        print('{:20} $ {:>17} $ {:>17} $ {:>17}'.format(donor[0], a, b, total))


def main():
    while True:
        try:
            users_choice = prompt_user()
            if users_choice == '1':
                thanked_user = thank_you()
                user(thanked_user)
            elif users_choice == '2':
                create_report()
                prompt_user()
            elif users_choice == '3':
                quit()
            else:
                prompt_user()
        except Exception as e:
            print("Exception [{}]".format(e))


if __name__ == "__main__":
    main()
