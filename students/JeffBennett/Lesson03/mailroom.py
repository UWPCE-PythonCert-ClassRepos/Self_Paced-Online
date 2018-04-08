#!/usr/bin/env python3

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
    print('Main Menu\n' + '-'*25 +
          '\n(1)\tSend a Thank You\n(2)\tCreate a Report\n(3)\tQuit')


def print_donor_list(donors):
    print('Our Current List of Donors:\n' + '-' * 25)
    for item in donors:
        print(item[0])


def print_email(donor, gift):
    print(f'Dear {donor}\n')
    print('We are delighted to acknowledge your generous')
    print(f'gift of ${gift:,.2f} to Northwest Lifeboats.')
    print('Your gift supports fishermen all along the Washington coast.\n')
    print('Sincerely yours\n\nJ. A. Bennett\nDirector')


def print_sorted_donors(ranked_list):
    print('{0:32}{1:13}{2:14}{3:13}'.format
          ('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('-' * 73)
    for row in ranked_list:
        print('{1:30s}  ${0:12.2f}{2:12d}  ${3:12.2f}'.format(*row))


# Processing


def update_donors(list, name, donation):
    count = 0
    for donor in donors[:]:
        count += 1
        if donor[0] == name:
            donor.append(donation)
            break
        elif count == len(donors[:]):
            donors.append([name, donation])
            break
        else:
            continue
    return donors


def sort_donors(donors):
    data_table = []
    for donor in donors:
        data_table = data_table.append
        ([sum(donor[1:]), donor[0],
          len(donor[1:]), sum(donor[1:]) / len(donor[1:])])
    print(data_table)
    sorted_donors = sorted(data_table, ascending=False)
    return sorted_donors


# Main


if __name__ == "__main__":
    while True:
        print_menu()
        menu_choice = input('Please enter the number of your choice: ')
        if menu_choice == '1':
            donor_name = input("Enter donor first and last name,\n or " +
                               "'list' for a list of current donors: ")
            if donor_name == 'list':
                print_donor_list()
                continue
            else:
                gift = float(input("Enter amount of gift: "))
                print_email(donor_name, gift)
                update_donors(donors, donor_name, gift)
                continue
        if menu_choice == '2':
            sort_donors(donors)
            print_sorted_donors()
            continue
        if menu_choice == '3':
            break
print("Exiting the program.  Changes made during this session not saved.")
