#!/usr/bin/python
from operator import itemgetter

# Lesson 03, Mailroom Part 1 Assignment


# ------- Global Assignments -------
donor_data = [['John', 'Marks', 5000.34, 2500, 1267],
              ['Matt', 'Smith', 750],
              ['Kelsey', 'Rodgers', 55.76],
              ['John', 'Williams', 500, 1898],
              ['Morgan', 'Stanley', 12000.98, 8670],
              ['Roger', 'Johnson', 264, 942.23],
              ['Sherry', 'Wilson', 4000, 2324.1, 1352],
              ['Alex', 'Grant', 8739, 4312]]

# ----------------------------------


def menu_disp():
    print("\n\n----- MENU -----")
    print("1: Send a Thank You")
    print("2: Create a Report")
    print("3: Quit")
    menu_sel_ = input("------> "
                      "Select an option from the menu: ")
    return menu_sel_


def list_display(data):
    print("\n---- List of all Donors ----")
    for item in data:
        print("- {} {}".format(item[0], item[1]))
    print("----------------------------")
    thank_you()


def list_details(data):
    header = "\n{:<18}| {:<12}| {:<10}| {:<12}".format("Donor Name", "Total "
                                                       "Given", "Num Gifts",
                                                       "Average Gift")
    buffer = "------------------------------------------------------------------"
    print(header)
    print(buffer)
    for item in sorted(data, key=itemgetter(-2), reverse=True):
        print("{:<18} $  {:>9.2f}  {:>10}  $   {:>9.2f}".format(item[0] + ' ' + item[1],
                                                                item[-2], item[-3],
                                                                item[-1]))


def compose_email(donor_name, donation_amount):
    greeting_email = "\nDear {},".format(donor_name)
    body_email = "\nThank you very much for your generous donation of {}".format(donation_amount)
    print(greeting_email, body_email)


def add_donation(donor_name, i):
    donation_amount = input("\nEnter the donation amount for {} ".format(donor_name))
    donor_data[i].append(float(donation_amount))
    compose_email(donor_name, donation_amount)


def thank_you(data=donor_data):
    donor_name = input("\nPlease enter the donor's full name: ")
    if donor_name == 'list':
        list_display(donor_data)
    else:
        donor_first_name = donor_name.split()[0]
        donor_last_name = donor_name.split()[1]
        for i, item in enumerate(data):
            if item[0] == donor_first_name and item[1] == donor_last_name:
                add_donation(donor_name, i)
                break
        else:
            donor_data.append(donor_name.split(' '))
            add_donation(donor_name, -1)


def calc_data(data=donor_data):
    for i, donor in enumerate(data):
        donations_quantity = len(donor) - 2
        donor_data[i].append(donations_quantity)
        donor_data[i].append(sum(donor[2:-1]))
        donor_data[i].append(float(donor[-1]) / donations_quantity)


def report(data=donor_data):
    calc_data(data)
    list_details(data)


if __name__ == "__main__":

    menu_map = {'1': thank_you, '2': report, '3': 'exit'}

    while True:
        menu_sel = menu_disp()
        if menu_map[menu_sel] == 'exit':
            break
        menu_map[menu_sel]()
