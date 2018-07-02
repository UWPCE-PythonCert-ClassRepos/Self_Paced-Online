#!/usr/bin/env python3


donors = {'Donor A': [3580, 34124.31, 7654], 'Donor B': [110.55, 3500],
          'Donor C': [11000], 'Donor D': [2233.1, 6543.74, 4567.35],
          'Donor E': [546123, 99.10, 23555, 19], 'Donor F': [78.75, 21.75]}


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt).lower()
        try:
            if dispatch_dict[response]() == 'exit menu':
                return True
                break
        except KeyError:
            print("Error: Value not an option, try again.")
            continue


def thank_you():
    menu_selection(thank_you_prompt, thank_you_dispatch)


def write():
    txt = """\n
        Dear {0:s},

        Thank you for your very kind donation of ${1:,.2f}.
        It will be put to very good use.

                    Sincerely,
                        -The Team
     """
    for d in donors.keys():
        file_name = d + ".txt"
        with open(file_name, 'w') as f:
            try:
                f.write(txt.format(d, sum(donors[d])))
                print("Generated letter for {:s}!\n".format(d))
            except(OSError, FileExistsError, IsADirectoryError,
                    PermissionError) as x:
                print('Error trying to write', file_name, ':', x)
                return False
    return True


def add_d():
    global donors
    print('add_donation')
    while True:
        try:
            # linit the donor name to letters and spaces
            x = str(input("\nEnter a donor name: "))
            if not all(a.isalpha() or a.isspace() for a in x) or x.isspace():
                raise ValueError()
            else:
                break
        except ValueError:
            print("Error: Donor names must contain letters and spaces")

    while True:
        try:
            d = float(input("\nPlease enter a donation amount: "))
            if d < 0.01:
                raise ValueError()
            else:
                break
        except ValueError:
            print("Error: Not a number, negative number, or number too small")
    donors = add_donation(x, d, donors)


def add_donation(x, d, ds):
    ds.setdefault(x, []).append(d)
    letter(x, float(d))
    return ds


def quit():
    print('Good Bye!')
    return "exit menu"


def donor_list():
    print('\nCurrent Donor list:')
    for i in donors.keys():
        print(i)
    return donors.keys()


def letter(name, amount):

    txt = """\n
            To:       {0:s}
            Subject:  Your donation of ${1:,.2f}
            Dear {0:s},\n

            Thank you for your donation of ${1:,.2f}.\n
     """
    print(txt.format(name, amount))
    return True


def donor_stat():
    lc = [[i, sum(donors[i]), len(donors[i]), sum(donors[i])/len(donors[i])]
          for i in donors.keys()]
    lc.sort(key=lambda e: e[1], reverse=True)
    print(lc[0])
    return lc


def report():
    """
    Generate the statistics for the donor list.
    """
    print('\n')
    print('Donor Name'+' '*16+'|'+' '*9+'Total Given'+' |'+' '*6+'Num Gifts'+'\
          |'+' '*8+'Average Gift')
    print('-'*26+'|'+'-'*21+'|'+'-'*17+'|'+'-'*21+'|')
    lst = donor_stat()
    for d in lst:
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
              d[0], d[1], d[2], d[3]))
    print('\n')
    return True


main_dispatch = {
    "1": thank_you,
    "2": report,
    "3": write,
    "q": quit
}

thank_you_dispatch = {
    "1": add_d,
    "2": donor_list,
    "q": quit
}


main_prompt = ("\nMain Menu\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "q  Quit\n")


thank_you_prompt = ("\nThank you menu:\n"
                    "1 - Add donation and send message\n"
                    "2 - Display list of current donors\n"
                    "q - Quit\n")


if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
