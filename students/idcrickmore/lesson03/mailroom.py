#!/usr/bin/env python3

donors = [
        ["Galileo Galilei", 348, 8377, 123],
        ["Giovanni Cassini", 209],
        ["Christiaan Huygens", 9135, 39],
        ["Edmond Halley", 399, 1100, 357],
        ["Edwin Hubble", 1899]
        ]


def menu():
    print("\n------------------ MENU ------------------\n")
    print("PLEASE CHOOSE FROM THE FOLLOWING THREE OPTIONS\n")
    print("1. Send Thank You\n2. Create a Report\n3. Quit\n")

    # the 'option' function calls an appropriate function based on user input
    def options():
        # save user input to 'choice' as a lowercase string
        choice = input("-> ").lower()
        # user input can be a number or a string
        # if its a string, just look at the first letter
        if choice[0] == '1' or choice[0] == 's':
            thankyou()
        elif choice[0] == '2' or choice[0] == 'c':
            report()
        elif choice[0] == '3' or choice[0] == 'q':
            print("quiting")
            quit()
        else:
            # if the user input does not match one of the 3 options,
            # call the menu function again
            menu()

    options()


def thankyou():
    global donors
    print("\n------------------ THANK YOU ------------------\n")
    print("- type 'list' to to see a complete list of donors -")
    print("- type 'menu' at any time to return to the menu -\n")

    # simple function to list all the donors
    # calls the 'thankyou' function at the end to ask for user input
    def list():
        print("\n------------------ DONOR LIST ------------------\n")

        for name in donors:
            print(name[0])

        thankyou()

    # asks for a name from the user, or for the 'list' prompt
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


        # promp the user for a donation amount
        donation = input("What is the donation amount? -> ")
        if donation == 'menu':
            menu()
        donation = float(donation)
        if name_loc == len(donors):
            donors.append([name_check.title()])
        donors[name_loc].append(donation)

        print("\n---------------------------------------------\n")
        print(("\nDear {},\n\nYou rock.\nYour fat contribution" +
               " of ${:,.2f}\nwill go a long way to lining my pockets." +
               "\n\nSincerely," +
               "\nScrooge McDuck").format(donors[name_loc][0], donation))

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

    # sorts the donors report by the second column "donation[1] using 'lambda'
    # and reverses the order from largest to smallest
    donors_report.sort(key=lambda donation: donation[1], reverse=True)

    print("{:<15}{:>17}{:>15}{:>10}".format(*column))
    print("---------------------------------------------------------------")

    # loops through 'donors_report' and
    # dumps all values for 'name' into .format
    for name in donors_report:
        print('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}'.format(*name))

    menu()


if __name__ == '__main__':
    menu()
