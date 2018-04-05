donors = [
    ['Lorenzo Currie', 3000, 250, 5000],
    ['Marie Kane', 1000, 195, 50.50],
    ['John Beresford Tipton', 10000, 3000, 2500],
    ['Janna Adams', 35.50, 19.75, 28.50, 45],
    ['LeSean Bennett', 100, 200, 65, 10],
    ['Laila Samir', 1000, 250]
]
"""
ranked_donors = [
    ['Lorenzo Currie', 3000, 250, 5000],
    ['Marie Kane', 1000, 195, 50.5],
    ['John Beresford Tipton', 10000, 6, 2500],
    ['Janna Adams', 35.5, 19, 28.5],
    ['LeSean Bennett', 100, 20, 5, 10],
    ['Laila Samir', 1000, 4, 250]]
    """
# Input/Output


def print_menu():
    print('Main Menu\n' + '-'*25 +
          '\n(1)\tSend a Thank You\n(2)\tCreate a Report\n(3)\tQuit Program')


def input_menu_choice():
    menu_choice = input('Please enter the number of your choice: ')
    return menu_choice


def print_donor_list(donors):
    print('Our Current List of Donors:\n' + '-' * 25)
    for item in donors:
        print(item[0])


"""
def print_email(donor, gift):
    print(f'Dear {donor}')
    print('We are delighted to acknowledge your generous')
    print(f'gift of ${gift:,d} to Northwest Lifeboats.')
    print('Your gift supports fishermen all along the Washington coast.\n')
    print('Sincerely yours\nJ. A. Bennett')
"""


def print_ranked_donors(ranked_donors):
    print('{0:32}{1:13}{2:14}{3:13}'.format
          ('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('-' * 73)
    for row in ranked_donors:
        print('{0:30s}  ${1:12.2f}{2:12d}  ${3:12.2f}'.format(*row))


# Processing
