def thank_you(donor_list):
    """Add donation amount to new or existing donor and generate a thank you text."""
    while 1:
        donor_name = input("Enter donor name:")
        if donor_name == 'list':
            for d in donor_list:  # display all donor names on user input 'list'
                print(d[0])
                continue
        else:
            for d in range(len(donor_list)):
                if donor_list[d][0] == donor_name:
                    print("Donor name found in database.")
                    donation = int(input('Enter donation amount:'))
                    donor_list[d].append(donation)
                    break
            else:
                print(f"Donor name not found. Will add {donor_name} to database at position {len(donor_list)+1}.")
                donation = int(input('Enter donation amount:'))
                donor_list += [[donor_name, donation]]
                print(donor_list)
            break
    print('Dear {},\nThank you for your generous gift of ${}\n'
          'Sincerely,\nLocal Charity.'''.format(donor_name, donation))
    return donor_list


def report(donor_list):
    """Generate report based on existing donors and donations. Display in variable column widths."""
    report_table = [("Donor Name", "Total Given", " Num Gifts", "Average Gift")]

    for row in donor_list:
        total_given = sum(row[1:])
        num_gifts = len(row)-1
        average_gift = total_given/num_gifts
        report_table += (row[0], '$' + str(total_given), str(num_gifts), '$' + str(average_gift)),

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

    print(form_string.format(*report_table[0]))
    print('{}'.format('-'*sum(mtl)))
    for row in range(len(report_table)-1):
        print(form_string.format(*report_table[row+1]))


def main():
    """Establish initial donor database and initiate top user menu. """
    ddb = [['Archie Bunker', 20, 100],
           ['Beyonce Knowles', 2000000, 50000000],
           ['Charlie Kauffman', 12345],
           ['David Sedaris', 23000, 1200, 2000],
           ['Edvard Munch', 1, 2, 3]]
    while 1:
        user_input = input('\n\nMENU:\n1 - Send a Thank You\n2 - Create a Report\n3 - Quit\nPlease enter 1-3>''')
        if user_input == '1':
            ddb = thank_you(ddb)
        elif user_input == '2':
            report(ddb)
        elif user_input == '3':
            print('Goodbye')
            break
        else:
            print('Option not found. Please enter the numeral 1,2 or 3')


if __name__ == '__main__':
    main()
