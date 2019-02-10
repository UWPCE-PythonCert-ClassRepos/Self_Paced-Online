import os
import sys

def new_thank_you():
    """Add donation amount to new or existing donor and generate a thank you text."""
    while True:
        current_dict = {'donor_name': input("Enter donor name, or type 'list' for current donor list:")}
        if current_dict['donor_name'] == 'list':
            for d in ddb:  # display all donor names on user input 'list'
                print(d + ': ', ddb[d])
        else:
            for key in ddb.keys():
                if key == current_dict['donor_name']:
                    print("Donor name found in database.")
                    current_dict['donation'] = float(input('Enter new donation amount:'))
                    ddb[key].append(current_dict['donation'])
                    break
            else:
                print(f"Donor name not found. Will add {current_dict['donor_name']} to database.")
                current_dict['donation'] = float(input('Enter donation amount:'))
                ddb[current_dict['donor_name']] = [current_dict['donation']]
            break

    print('\n\n', create_letter(current_dict))


def report():
    """Generate report based on existing donors and donations. Display in variable column widths."""
    report_table_header = [("Donor Name", "Total Given", " Num Gifts", "Average Gift")]

    report_table = []

    for key in ddb.keys():  # read dict values into 2D list to be displayed.
        total_given = sum(ddb[key])
        num_gifts = len(ddb[key])
        average_gift = total_given/num_gifts
        report_table += [(key, '$' + str(total_given), str(num_gifts), '$' + str(average_gift))]

    report_table = report_table_header + sorted(report_table, key=lambda list:int(list[1][1:]), reverse=True)

    mtl = []  # list for the longest characters in each column
    for i in range(len(report_table[0])):
        tl = 0
        for row in report_table:
            if len(str(row[i])) > tl:
                tl = len(str(row[i]))
        mtl.append(tl + 3)  # add 3 spaces to each column

    form_string = []
    for i in mtl:
        form_string.append('{:' + str(i) + '}')
    form_string = ''.join(form_string)

    print('\n\n')  # Begin printing out table
    print(form_string.format(*report_table.pop(0)))
    print('{}'.format('-'*sum(mtl)))  # spacer line between header and body of table
    for row in report_table:
        print(form_string.format(*row))


def letters_to_all():
    """Writes form letter to txt files based on input dictionary. Optional directory change."""
    user_input = input("Would you like save to current directory,{}? >(y,n)".format(os.getcwd()))
    if user_input == 'n':
        path = input("Enter full path to desired directory: ")
        os.chdir(path)

    for key in ddb.keys():
        print(key)
        current_dict = {'donor_name': key, 'donation': ddb[key][-1]}
        print("current_dict: ", current_dict)
        key = key.replace(' ', '_')
        with open('{}.txt'.format(key), 'w') as f:
            f.write(create_letter(current_dict))


def create_letter(letter_dict):
    """Returns form letter string based on input dictionary. Dictionary needs 'donor_name' and 'donation' keys"""
    letter_dict['fleebs_floobed'] = round(letter_dict['donation']/20)
    return ('Dear {donor_name},'
            '\n\n\tThank you for your generous gift of ${donation:,.2f}.'
            '\n\tYour contribution will keep {fleebs_floobed} Fleebs floobing for an entire year.'
            '\n\tWe truly could not do this important work without you.'
            '\n\nSincerely,'
            '\nFleeb Freedom Now'.format(**letter_dict))


def goodbye():
    print("goodbye!")
    sys.exit()

ddb = {'Archie Bunker': [20, 100, 75, 98],
       'Beyonce Knowles': [2000000, 50000000],
       'Charlie Kauffman': [12345],
       'David Sedaris': [23000, 1200, 2000],
       'Edvard Munch': [1, 2, 3]}


def main():
    """Establish initial donor database and initiate top user menu. """

    while True:
        user_input = input('\n\nMENU:\n'
                           '1 - Send a Thank You for a New Donation\n'
                           '2 - Create a Report\n'
                           '3 - Send letters to everyone\n'
                           '4 - Quit\n'
                           'Please enter 1-4>')
        user_menu = {'1': new_thank_you, '2': report, '3': letters_to_all, '4': goodbye}

        try:
            user_menu[user_input]()
        except TypeError:
            print('\nOption not found. Please enter the numeral 1,2,3 or 4')


if __name__ == '__main__':
    main()
