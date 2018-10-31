def menu():
    while True:
        try:
            print("\n==========================================")
            print("Would you like to:")
            print("\t1 - Send a thank you letter.")
            print("\t2 - Send thank you letters to everyone.")
            print("\t3 - Add a donation.")
            print("\t4 - Create a report.")
            print("\t5 - Quit.")
            response = int(input(">>> "))
            return response
            break
        except ValueError:
            print("Oops: Please select an option (1-5):")
            pass


def send_thanks_one():
    while True:
        print(list_donors(donors))
        print("Who from the list above would you like to thank?")
        response = input(">>> ")
        response = response.title()
        if response in donors.keys():
            thanks_letter(response)
            break
        else:
            print("{} is not a donor, would you like to add them?".format(response))
            x = input("Y/N >>> ")
            if x.lower() == "y":
                rec_dontation()
                break
            if x.lower() == "n":
                break


def send_thanks_all():
    name_lst = list_donors(donors)
    for i in name_lst:
        thanks_letter(i)


def list_donors(dnr_dict):
    name_lst = [d for d in dnr_dict.keys()]
    return name_lst

# Need to evaluate, might return the same donor twice if two doners have
# equal donation amounts.
def sorted_donors():
    total_gift_lst = [sum_gifts(d) for d in donors]
    total_gift_lst.sort(reverse = True)
    sorted_name_lst = []
    sorted_name_lst = [
    d for i in total_gift_lst for d in donors if sum_gifts(d) == i
    ]
    return sorted_name_lst


def rec_dontation():
    # Need to find a way to prevent use of numbers!!!!!
    while True:
        print("Who made the donation?")
        donor = input(">>> ").title()
        if donor.isnumeric() == False:
            break
    while True:
        try:
            print("How much was the donation?")
            donation = float(input(">>> "))
            break
        except ValueError:
            print("Oops, please enter only numbers.")
            pass
    if donor in donors.keys():
        donors[donor].append(donation)
    else:
        donors[donor] = [donation]


def thanks_letter(donor):
    file_name = "{}.txt".format(donor.replace(" ", "_"))
    donation = sum_gifts(donor)

    header = "Dear {},".format(donor)
    body = "Thank you for your donation of ${:.2f}.".format(donation)
    close = "\tSincerely,\n\t\t-The Team"

    letter = "{}\n{}\n\n{}".format(header, body, close)

    with open(file_name, 'w+') as f:
        f.write(letter)
    print("Thank you letter for {} created.".format(donor))


def create_report():
    dnr_names = sorted_donors()
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    i_count = 1
    for i in dnr_names:
        i_total_gift = sum_gifts(i)
        i_count = count_gifts(i)
        i_ave_gift = i_total_gift / i_count
        s = f'{i:<21}{"$":<1}{i_total_gift:>14.2f}{" ":<1}{i_count:>15}{" ":<1}{"$":<1}{i_ave_gift:>14.2f}'
        print(s)


def sum_gifts(donor):
    total = 0
    donations = donors[donor]
    for i in donations:
        total = total + i
    return total


def count_gifts(donor):
    donations = donors[donor]
    count = len(donations)
    return count


def run_func(fun_dict):
    while True:
        response = menu()
        if response != 5:
            fun_dict[response]()
        else:
            break


donors = {"Anita Bath": [200, 150],
          "Isabelle Ringing": [101],
          "John Smith": [100],
          "Seymour Butz": [95, 500]}


functions = {1: send_thanks_one,
             2: send_thanks_all,
             3: rec_dontation,
             4: create_report,
             5: quit}


if __name__ == '__main__':
    run_func(functions)
