import os

donor_db = {"John Smith": [18774.48, 8264.47, 7558.71], "Jane Doe": [281918.99, 8242.13],
            "Alan Smithee": [181.97, 955.16], "Tom D.A. Harry": [67.10, 500.98], "Joe Shmoe": [200.01]}


def thank_you():
    user_input = input('Enter a donor\'s full name, or type \'list\' for a full list. ' +
                       'Type \'e\' to exit and return to the main menu.\n> ').title()
    if user_input.lower() == 'list':
        for k in donor_db:
            print(k)
        thank_you()
    elif user_input.lower() == 'e':
        mailroom()
    else:
        donation = float(input("Please enter a donation amount: "))
        donor_list = []
        for k in donor_db:
            donor_list.append(k)
            if user_input in donor_list and k == user_input:
                donor_db[k].append(donation)
                print("Existing donor found.")
                print("Appending the amount of {0} to {1}'s file...".format(donation, user_input))
                print("Printing thank you email...")
                print("---------------------------")
                create_letter(0, user_input, donation)
            else:
                donor_db[user_input] = [donation]
                print("New donor detected. Creating record for {0}...".format(user_input))
                print("Printing thank you email...")
                print("---------------------------")
                create_letter(1, user_input, donation)


def report():
    while True:
        print('Donor Name' + ' ' * 16 + '| Total Given | Num Gifts | Average Gift')
        print('-' * 66)
        for k in donor_db:
            num_gifts = len(donor_db[k])
            total_given = sum(donor_db[k])
            average_gifts = total_given / num_gifts
            print(f'{k: <26}| ${total_given:>10.2f} |{num_gifts:^11}| ${average_gifts:>11.2f}')
        print('\nReturning to main menu...')
        return


def send_letters():
    print("Creating letters...")
    for k in donor_db:
        with open(k + '.txt', 'w') as letter:
            letter.write(create_letter(2, k, sum(donor_db[k])))
    print("Letters saved to text file.")


def quit_program():
    quit("Exiting...")


def create_letter(donor_status, donor_name, donation_amt):
    if donor_status == 0:
        letter_text = """
        Dear {0},
    
            Thank you for your very kind donation of ${1}, and for your continuing support.
    
            Your generous contribution will be put to very good use.
    
                           Sincerely,
                              -The Team
                              """.format(donor_name, donation_amt)
        print(letter_text)
        print("---------------------------")
        print("Returning to thank you letter menu...")
        thank_you()
    elif donor_status == 1:
        letter_text = """
        Dear {0},

            Thank you for your very kind donation of ${1}.

            Your generous contribution will be put to very good use.

                           Sincerely,
                              -The Team
                              """.format(donor_name, donation_amt)
        print(letter_text)
        print("---------------------------")
        print("Returning to thank you letter menu...")
        thank_you()
    elif donor_status == 2:
        return("""
        Dear {0},

            Thank you for your very kind contribution(s) totaling ${1}.

            We would like you to know that your generous donation(s) will be put to very good use.

                           Sincerely,
                              -The Team
                              """.format(donor_name, donation_amt))


def thank_all():
    current_dir = os.getcwd()
    print("Saving letters to {0}.".format(current_dir))

    for k, v in donor_db.items():
        letter = create_letter(2, k, sum(v))
        with open('{:s}.txt'.format(k), 'w') as f:
            f.write(letter)
    print("---------------------------")
    print("Letters printed and saved to text files in directory. Returning to main menu...")
    mailroom()


def mailroom():
    while True:
        selection = input('MAILROOM v0.2\n------------------------\nChoose an option:\n1) Send a thank you' +
                          '\n2) Create a report\n3) Send letters to everyone\n4) Quit\n> ')
        menu_dict = {'1': thank_you, '2': report, '3': thank_all, '4': quit_program}
        if selection in menu_dict:
            menu_dict.get(selection)()
        else:
            print("Invalid value. Enter a number from 1-4.")


if __name__ == "__main__":
    mailroom()
