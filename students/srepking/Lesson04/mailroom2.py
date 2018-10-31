import os

def thank_you():
    print('\n''Ok, you chose 1, lets see what we can do.')
    while True:
        name = input('\n''Type the full name to add entry, '
                     '\'list\' to see list of names, or \'e\' to exit: > ')
        if name == 'e':
            return
        if name != 'list':
            break
        for x in donors:
            print(x)
    # Add Name to list if not in list
    if name not in donors:
        print('Name is not there, added to the list')
        donors[name] = []
        amount = input('\n''What is the donation amount? or \'e\' to exit >')
        if amount == 'e':
            return
        new_amount = [float(amount)]
        old_amount = donors[name]
        donors[name] = old_amount + new_amount
        print('Thank you so much for the generous gift of ${0:.2f}, {1}!'
              .format(float(amount), name))


def summary_donors() -> object:

    # Create a new dictionary with Total, number of donations,
    # and average donation amount
    donors_f = {}
    for name, donations in donors.items():
        # Calculate total donation amount
        total = sum(donations)
        count = 0
        average = 0
        i = 0

        # Calculate total number of donations, not counting $0
        for i in donations:
            if i != 0:
                count = count + 1
        # Calculate total donation amount
        if count > 0:
            average = total / count
        donors_f[name] = [total, count, average]
    return donors_f


def report():
    """Return a report on all the donors"""
    donors_f = summary_donors()
    print('\n''A summary of your donors donations:')
    name_list = list(donors_f.keys())  # creates a list of keys
    name_wi = 11 # Establish minimum column width
    for i in name_list:
        if len(i) > name_wi:
            name_wi = (len(i))  # width of name column
    # Find the longest donation amount
    tot_wi = 12
    ave_wi = 12
    num_wi = 12
    for name, summary in donors_f.items():
        if len(str(summary[0])) > tot_wi:
            # width of total column
            tot_wi = (len(str(summary[0]))) + 3
            # width of number of donations column
        if len(str(summary[1])) > num_wi:
            num_wi = (len(str(summary[1]))) + 3
            # width of total average column
        if len(str(int(summary[2]))) > ave_wi:
            ave_wi = (len(str(int(summary[2])))) + 3
    list_sorted = sorted(donors_f, key=donors_f.__getitem__, reverse=True)
    # Print the Table
    print(f"{'Donor Name':{name_wi}}| {'Total Given':^{tot_wi}}| "
          f"{'Num Gifts':^{num_wi}}| {'Average Gift':^{ave_wi}}")
    print(f"{'-':-^{(name_wi+tot_wi+ave_wi+num_wi+8)}}")
    # print("-")
    for key in list_sorted:
        temp = donors_f[key]
        print(f"{key:{name_wi}}${temp[0]:{tot_wi}}{temp[1]:^{num_wi}}   "
              f"${temp[2]:>{ave_wi}.2f}")

    print('\n')


def letters_for_all():
    path_letters = os.getcwd()
    print(f"You chose to send letters for everyone. "
          f"The letters have been completed and you "
          f"can find them here: {path_letters}")
    donors_f = summary_donors()
    for donor, donation in donors.items():
        donation_summary = donors_f[donor]
        letter = f'Dear {donor}, thank you so much for your last ' \
                 f'contribution of ${donation[-1]:.2f}! ' \
                 f'You have contributed a total of ${donation_summary[0]:.2f}, ' \
                 f'and we appreciate your support!'
        # Write the letter to a destination
        with open(donor + '.txt', 'w') as to_file:
            to_file.write(letter)


def wrong_choice():
    pass

def quit():
    exit()

if __name__ == '__main__':

    donors = {'Joe Edgar Allen Poe the Third ': [1, 4, 200],
              'Jack': [4, 5], 'Jill': [4], 'Jake': [.30],
              'Jim': [1, 2, 1.04]}
    switch_dict = {'1': thank_you, '2': report, '3': letters_for_all, '4': quit}
    while True:
        response = input(
            '\nChoose an Action:\n'
            '1 - Send a Thank You\n'
            '2 - Create a Report\n'

            '3 - Send letters to everyone\n'
            '4 - Quit\n'
            '>>')

        switch_dict.get(response, wrong_choice)()

