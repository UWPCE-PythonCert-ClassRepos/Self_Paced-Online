donors = [
        ["William Gates, III", 653784.49, 2, 326892.24],
        ["Mark Zuckerberg", 16396.10, 3, 5465.37],
        ["Jeff Bezos", 877.33, 1, 877.33],
        ["Paul Allen", 708.42, 3, 236.14],
        ]


def menu():
    quit_program = False
    while not quit_program:

        print("\n------------------ Main Menu ------------------\n")
        print("Choose an action:\n")
        print("Press 1 to send a Thank You\n")
        print("Press 2 to create a report\n")
        print("Press 3 to quit the program\n")
        choice = input("-> ")

        if choice == '1':
            thankyou()
        elif choice == '2':
            report()
        elif choice == '3':
            quit_program = True
            break
        else:
            print("Please try again")
        menu()


def thankyou():
    global donors
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("- If the user types ‘list’, show them a list of the donor names and re-prompt -")
    print("- type 'menu' at any time to return to the menu -\n")

    def list():
        print("\n------------------ DONOR LIST ------------------\n")

        for name in donors:
            print(name[0])

        thankyou()

    name_check = input("Enter first and last name of a donor\n\n-> ").lower()

    if name_check == 'menu':
        menu()
    if name_check == 'list':
        list()
    else:
        name_loc = 0

        for name in donors:
            if name_check == name[0].lower():
                break
            name_loc += 1

        donation = float(input("What is the donation amount? -> "))
        if donation == 'menu':
            menu()
        if name_loc == len(donors):
            donors.append([name_check.title()])
        donors[name_loc].append(donation)

        print("\n---------------------------------------------\n")
        print(("\nDear {},\n\nThank you for your contribution" +
               " of ${:,.2f}\nIt will be put to very good use." +
               "\n\Sincerely," +
               "\nVinodh").format(donors[name_loc][0], donation))

        menu()
def report():
    print("\n-------------------- REPORT --------------------\n")

    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    name_loc = 0
    donors_report = []

    for name in donors:
        sum_don = sum(donors[name_loc][1:])
        num_don = len(donors[name_loc])-1
        ave_don = sum_don / num_don
        donors_report += [[donors[name_loc][0], sum_don, num_don, ave_don]]
        name_loc += 1


    donors_report.sort(key=lambda donation: donation[1], reverse=True)

    print("{:<15}{:>17}{:>15}{:>10}".format(*column))
    print("---------------------------------------------------------------")


    for name in donors_report:
        print('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}'.format(*name))

    menu()

if __name__ == '__main__':
    menu()