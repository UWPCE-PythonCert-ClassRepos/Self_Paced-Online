#!/usr/bin/env python3

# Data

donors = [
    ['Lorenzo Currie', 3000, 250, 5000],
    ['Marie Kane', 1000, 195, 50.50],
    ['John Beresford Tipton', 10000, 3000, 2500],
    ['Janna Adams', 35.50, 19.75],
    ['LeSean Haskell', 100],
    ['Laila Samir', 1000, 250]
]

# Input/Output


def print_menu():
    """print menu of user choices."""
    print('\nMain Menu\n' + '-'*25 +
          '\n(1)\tSend a Thank You\n(2)\tCreate a Report\n(3)\tQuit')


def print_donor_list(donors):
    """print list of donor names."""
    print('Our Current List of Donors:\n' + '-' * 25)
    for item in donors:
        print(item[0])


def print_email(donor, gift):
    """print email thanking donor for recent donation."""
    print(f'\nDear {donor}\n')
    print('We are delighted to acknowledge your generous')
    print(f'gift of ${gift:,.2f} to Northwest Lifeboats.')
    print('Your gift supports fishermen all along the Washington coast.\n')
    print('Sincerely yours\n\nJ. A. Bennett\nDirector')


def print_sorted_donors(sorted_donors):
    """print list of donors sorted by total donation history."""
    print('{0:32}{1:13}{2:14}{3:13}'.format
          ('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('-' * 73)
    for row in sorted_donors:
        print('{0:30s}  ${1:12.2f}{2:12d}  ${3:12.2f}'.format(*row))


# Processing


def update_donors(list, name, donation):
    """update the list of donors and their gift history.
    Function iterates the copy and mutates the original list. """
    count = 0
    for donor in donors[:]:
        count += 1
        if donor[0] == name:
            donor.append(donation)
            break
        elif count == len(donors[:]):
            donors.append([name, donation])
        else:
            continue
    return donors


def sort_donors(donors):
    """sort donors from largest to smallest aggregate givers, and calculate
    average gift and number of gifts per donor. """
    data_table = [[d[0], sum(d[1:]), len(d[1:]), sum(d[1:]) / len(d[1:])]
                  for d in donors]
    sorted_donors = sorted(data_table, key=lambda x: x[1], reverse=True)
    return sorted_donors

# Main


if __name__ == "__main__":
    while True:
        print_menu()
        menu_choice = input('Please enter the number of your choice: ')
        if menu_choice == '1':
            donor_name = input("\nEnter donor first and last name,\n " +
                               "'list' for a list of current donors: \n" +
                               "  or 'menu' to return to the main menu: ")
            if donor_name == 'menu':
                continue
            elif donor_name == 'list':
                print_donor_list(donors)
                continue
            else:
                gift = float(input("\nEnter amount of gift: " +
                                   " or '0' to return to the main menu: "))
                if gift == 0:
                    continue
                print_email(donor_name, gift)
                update_donors(donors, donor_name, gift)
                continue
        if menu_choice == '2':
            sorted_donors = sort_donors(donors)
            print_sorted_donors(sorted_donors)
            continue
        if menu_choice == '3':
            break
print("Exiting the program.  Changes made during session are not saved.")
