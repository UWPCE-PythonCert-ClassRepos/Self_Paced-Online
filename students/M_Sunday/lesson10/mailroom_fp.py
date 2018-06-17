#!/usr/bin/python
from operator import itemgetter

# Lesson 10, Mailroom Part 6 Assignment (functional programming)
# Starting from lesson06 (Mailroom_Part_4)


# ------- Global Assignments -------
donor_data = {'John Marks': [5000.34, 2500, 1267],
              'Matt Smith': [750],
              'Kelsey Rodgers': [55.76],
              'John Williams': [500, 1898],
              'Morgan Stanley': [12000.98, 8670],
              'Roger Johnson': [264, 942.23],
              'Sherry Wilson': [4000, 2324.1, 1352],
              'Alex Grant': [8739, 4312]}
# ----------------------------------


def get_menu_option():
    sel_ = input("------> "
                 "Select an option from the menu: ")
    return sel_


def menu_display():
    print("\n\n----- MENU -----\n"
          "1: Send a Thank You\n"
          "2: Create a Report\n"
          "3: Send letters to everyone\n"
          "4: Quit\n")
    menu_sel_ = get_menu_option()
    return menu_sel_


def list_display():
    print("\n---- List of all Donors ----")
    [print("- {}".format(item)) for item in donor_data]
    print("----------------------------")


def list_details(data):
    header = "\n{:<18}| {:<12}| {:<10}| {:<12}".format("Donor Name", "Total "
                                                       "Given", "Num Gifts",
                                                       "Average Gift")
    buffer = "------------------------------------------------------------------"
    print(header)
    print(buffer)
    for item in sorted(data, key=itemgetter(-2), reverse=True):
        print("{:<18} $  {:>9.2f}  {:>10}  $   {:>9.2f}".format(item[0], item[2], item[1], item[3]))


def compose_email(donor_name, donation_amount):
    greeting_email = "\nDear {},".format(donor_name)
    body_email = "\nThank you very much for your generous donation of {}".format(donation_amount)
    print(greeting_email, body_email)


def get_donation_amount(donor_name_):
    amount_ = input("\nEnter the donation amount for {} ".format(donor_name_))
    return amount_


def add_donation(donor_name):
    donation_amount = get_donation_amount(donor_name)
    donor_data[donor_name].append(float(donation_amount))
    compose_email(donor_name, donation_amount)


def thank_you(donor_name):
    if donor_name == 'list':
        list_display()
    else:
        if donor_name in donor_data:
            add_donation(donor_name)
        else:
            donor_data[donor_name] = []
            try:
                add_donation(donor_name)
            except ValueError:
                print("Donation amount must be a number with no commas or currency symbols")
                donor_data.pop(donor_name)


def get_donors_name():
    name_ = input("\nPlease enter the donor's full name: ")
    return name_


def thank_you_input():
    donor_name_ = get_donors_name()
    thank_you(donor_name_)


def calc_data():
    summary_data = list(map(calc_data_2, donor_data.values(), donor_data.keys()))
    return summary_data


def calc_data_2(donation_data, donor):
    donations_quantity = len(donation_data)
    donations_value = sum(donation_data)
    donations_average = (float(donations_value / donations_quantity))
    return [donor, donations_quantity, donations_value, donations_average]


def report():
    summary_data = calc_data()
    list_details(summary_data)


def send_all_letters():
    summary_data = calc_data()
    list(map(send_letter, summary_data))
    print("\nAll thank you letters drafted")


def send_letter(item):
    filename_format = "{}_{}.txt".format(item[0].split()[0], item[0].split()[1])
    thank_you_text = open(filename_format, 'w+')
    thank_you_text.write("Dear {},\n\nThank you very much for your {} generous donations totalling ${}.\n"
                         "\nYour donations will significantly aid our scholarship fund\n\n"
                         "Sincerely,\n - Advancement Office".format(item[0], item[1], item[2]))
    thank_you_text.close()


def exit_program():
    exit()


def main_exec():
    menu_map = {'1': thank_you_input, '2': report, '3': send_all_letters, '4': exit_program}

    while True:
        try:
            menu_sel = menu_display()
            menu_map[menu_sel]()
        except KeyError:
            print("\nMenu selection must be one of the following:\n")
            for key in menu_map:
                print("- {}".format(key))


if __name__ == "__main__":

    main_exec()

