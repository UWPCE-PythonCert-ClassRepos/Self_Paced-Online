#!/usr/bin/python
from operator import itemgetter
from functools import reduce

# Lesson 10, Mailroom Part 6 Assignment (functional programming)
# StartedS from lesson06 (Mailroom_Part_4)


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
          "4: Philanthropic Challenge\n"
          "5: Project Philanthropic Contribution\n"
          "6: Quit\n")
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


def calc_data(data_for_donors):
    summary_data = list(map(calc_data_2, data_for_donors.values(), data_for_donors.keys()))
    return summary_data


def calc_data_2(donation_data, donor):
    donations_quantity = len(donation_data)
    donations_value = sum(donation_data)
    donations_average = (float(donations_value / donations_quantity))
    return [donor, donations_quantity, donations_value, donations_average]


def report(db=donor_data):
    summary_data = calc_data(db)
    list_details(summary_data)


def send_all_letters():
    summary_data = calc_data(donor_data)
    list(map(send_letter, summary_data))
    print("\nAll thank you letters drafted")


def send_letter(item):
    filename_format = "{}_{}.txt".format(item[0].split()[0], item[0].split()[1])
    thank_you_text = open(filename_format, 'w+')
    thank_you_text.write("Dear {},\n\nThank you very much for your {} generous donations totalling ${}.\n"
                         "\nYour donations will significantly aid our scholarship fund\n\n"
                         "Sincerely,\n - Advancement Office".format(item[0], item[1], item[2]))
    thank_you_text.close()


def philanthropic(report_option=1):
    factor = get_challenge_factor()
    min_threshold = get_minimum_threshold()
    max_threshold = get_maximum_threshold()
    donor_data_philanthropic_list = list(map(challenge, donor_data.keys(), [factor] * len(donor_data),
                                             donor_data.values(), [min_threshold] * len(donor_data),
                                             [max_threshold] * len(donor_data)))
    donor_data_philanthropic_dict = {}
    for entry in donor_data_philanthropic_list:
        if entry[1]:
            donor_data_philanthropic_dict[entry[0]] = entry[1]
    if report_option:
        report(donor_data_philanthropic_dict)
    else:
        projection_report(donor_data_philanthropic_dict, factor, min_threshold, max_threshold)


def challenge(donor, factor, data, min_th, max_th):
    data = list(filter(lambda x: filtering(x, min_th, max_th), data))
    return donor, list(map(challenge_m, [factor]*len(data), data))


def challenge_m(factor, val):
    return factor * val


def filtering(val, minimum=0, maximum=100000):
    return minimum < val < maximum


def get_challenge_factor():
    return int(input("\nBy what factor do you want to multiply all donations? "))


def get_minimum_threshold():
    return int(input("\nWhat is the minimum threshold for donations you want to multiply? "))


def get_maximum_threshold():
    return int(input("\nWhat is the maximum threshold for donations you want to multiply? "))


def project_philanthropic():
    philanthropic(report_option=0)


def projection_report(data, fact, min_, max_):
    total_donations = sum(list(map(summer, data.values())))
    print("\nBy matching all donations greater than ${} and less than ${}, by a factor of {}, your total donation "
          "comes to ${}".format(min_, max_, fact, total_donations))


def summer(val):
    return sum(val)


def exit_program():
    exit()


def main_exec():
    menu_map = {'1': thank_you_input, '2': report, '3': send_all_letters, '4': philanthropic, '5': project_philanthropic
                , '6': exit_program}

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
