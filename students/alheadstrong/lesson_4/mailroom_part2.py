def thank_you(donor_dict):
    """Add donation amount to new or existing donor and generate a thank you text."""
    while 1:
        donor_name = input("Enter donor name:")
        if donor_name == 'list':
            for d in donor_dict:  # display all donor names on user input 'list'
                print(d[0])
                continue
        else:
            for d in range(len(donor_dict)):
                if donor_dict[d][0] == donor_name:
                    print("Donor name found in database.")
                    donation = int(input('Enter donation amount:'))
                    donor_dict[d].append(donation)
                    break
            else:
                print(f"Donor name not found. Will add {donor_name} to database at position {len(donor_dict)+1}.")
                donation = int(input('Enter donation amount:'))
                donor_dict += [[donor_name, donation]]
                print(donor_dict)
            break
    print('Dear {},\nThank you for your generous gift of ${}\n'
          'Sincerely,\nLocal Charity.'''.format(donor_name, donation))
    return donor_dict


def report(donor_dict):
    """Generate report based on existing donors and donations. Display in variable column widths."""
    report_table_header = [("Donor Name", "Total Given", " Num Gifts", "Average Gift")]

    report_table = []

    for key in donor_dict.keys():
        total_given = sum(donor_dict[key])
        num_gifts = len(donor_dict[key])
        average_gift = total_given/num_gifts
        new_report_line = (key, '$' + str(total_given), str(num_gifts), '$' + str(average_gift))
        if not report_table:
            report_table += [new_report_line]
        else:
            for i in range(len(report_table)):
                if average_gift > float(report_table[i][3][1:]):
                    report_table = report_table[:i]+[new_report_line]+report_table[i:]
                    break
    report_table = report_table_header + report_table

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
    return donor_dict

def goodbye(arg):
    print("goodbye!")



def main():
    """Establish initial donor database and initiate top user menu. """
    ddb = {'Archie Bunker': [20, 100],
           'Beyonce Knowles': [2000000, 50000000],
           'Charlie Kauffman': [12345],
           'David Sedaris': [23000, 1200, 2000],
           'Edvard Munch': [1, 2, 3]}

    while ddb != quit:
        user_input = input('\n\nMENU:\n1 - Send a Thank You\n2 - Create a Report\n3 - Quit\nPlease enter 1-3>')
        user_menu = {'1': thank_you, '2': report, '3': goodbye}
        ddb = user_menu.get(user_input,'Option not found. Please enter the numeral 1,2 or 3')(ddb)

if __name__ == '__main__':
    main()
