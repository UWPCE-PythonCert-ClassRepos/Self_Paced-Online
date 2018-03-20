#!/usr/bin/env python3


if __name__ == "__main__":
	#this will only run if run as a script.
    print("This is inside the name:main block.")

donors = [["Luke Rodriguez", [12.75, 50.31, 42.59]], ['Emma Burgess', [390.87, 30.00]], ['Greg Cayetano', [875.60, 1120.00]],
          ["Hannah Watson", [20.58, 1120.14]], ['Emily Connor', [10.00]], ['Catherine Davis', [400.00]],
          ["River Tails", [63.56, 1200.00, 300.65]], ['Virginia Ferdinand', [350.35, 5000.00]], ['Joseph Kibson', [3498.00, 5.50]],]


def donor_list():
    for item in donors:
        print(item[0])
    thank_you()

def menu():
    close_menu = False
    while not close_menu:

        print("Hello! What would you like to do today?\nWrite a Thank You (1), Create a Report (2) or Quit(3)?"'\n')

        menu_input = input()

        if menu_input == '1':
            thank_you()

        elif menu_input == '2':
            donor_report()

        elif menu_input in '3':
            close_menu = True

        else:
            print('Please enter a valid option.')

def thank_you():
    print("Please enter the name of the donor you wish to thank.\n (Enter \'list\' for a list of donors.)")
    answer = input()

    if answer.lower() == 'list':
        donor_list()

    elif answer == '3':
        return

    else:
        donation = float(input('Please enter the amount of the donation:'))


        for j, k in enumerate(donors):
            if answer == k[0]:
                donors[j][1].append(donation)
                break
        else:
            donors.append([answer, [donation]])

        print('\n'"Dear {}, \nThank you for your donation to The Nature Conservancy in the amount of ${:.2f}.".format(answer, donation))
        print("We are extremely appreciative of your contribution and your dedication to saving the environment.")
        print("Sincerely,\nThe Nature Conservancy"'\n')

def donor_report():
    print("Here is a list of donors and the amount they have contributed.")
    print("|     Donor Name     |     Total Given    |  Number of Gifts   |   Average Gift     |")
    print(" ____________________________________________________________________________________")
    for data in donors:
        a = sum(data[1])
        b = len(data[1])
        print("|{:>20}|{:>20}|{:>20}|{:>20}|".format(data[0], a, b, round(a/b,2)))


#Run the Mailroom program.
menu()

