#!/usr/bin/python
from operator import itemgetter

# Lesson 03, Mailroom Part 1 Assignment


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


def menu_display():
    print("\n\n----- MENU -----\n"
          "1: Send a Thank You\n"
          "2: Create a Report\n"
          "3: Send letters to everyone\n"
          "4: Quit\n")
    menu_sel_ = input("------> "
                      "Select an option from the menu: ")
    return menu_sel_


def list_display():
    print("\n---- List of all Donors ----")
    for item in donor_data:
        print("- {}".format(item))
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
        print("{:<18} $  {:>9.2f}  {:>10}  $   {:>9.2f}".format(item[0], item[2], item[1], item[3]))


def compose_email(donor_name, donation_amount):
    greeting_email = "\nDear {},".format(donor_name)
    body_email = "\nThank you very much for your generous donation of {}".format(donation_amount)
    print(greeting_email, body_email)


def add_donation(donor_name):
    donation_amount = input("\nEnter the donation amount for {} ".format(donor_name))
    donor_data[donor_name].append(float(donation_amount))
    compose_email(donor_name, donation_amount)


def thank_you():
    donor_name = input("\nPlease enter the donor's full name: ")
    if donor_name == 'list':
        list_display()
    else:
        if donor_name in donor_data:
            add_donation(donor_name)
        else:
            donor_data[donor_name] = []
            add_donation(donor_name)


def calc_data():
    summary_data = []
    for i, item in enumerate(donor_data):
        donations_quantity = len(donor_data[item])
        donations_value = sum(donor_data[item])
        donations_average = (float(donations_value / donations_quantity))
        summary_data.append([])
        summary_data[i].extend([item, donations_quantity, donations_value, donations_average])
    return summary_data


def report():
    summary_data = calc_data()
    list_details(summary_data)


def send_all_letters():
    summary_data = calc_data()
    for item in summary_data:
        filename_format = "{}_{}.txt".format(item[0].split()[0], item[0].split()[1])
        thank_you_text = open(filename_format, 'w+')
        thank_you_text.write("Dear {},\n\nThank you very much for your {} generous donations totalling ${}.\n"
                             "\nYour donations will significantly aid our scholarship fund\n\n"
                             "Sincerely,\n - Advancement Office".format(item[0], item[1], item[2]))
        thank_you_text.close()
    print("\nAll thank you letters drafted")


if __name__ == "__main__":

    menu_map = {'1': thank_you, '2': report, '3': send_all_letters, '4': 'exit'}

    while True:
        menu_sel = menu_display()
        if menu_map[menu_sel] == 'exit':
            break
        menu_map[menu_sel]()
