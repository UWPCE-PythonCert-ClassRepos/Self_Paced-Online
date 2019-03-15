#!/usr/bin/env python3

donor_db = {"Wassily Kandinsky": [43928.13, 131.34, 1928.0],
            "Jasper Johns": [3134.43, 153.34],
            "Mark Rothko": [135353.33],
            "Richard Serra": [153757.87, 28457.12, 1293451.0],
            "Yves Tanguy": [1534.23, 2542.19]}

PROMPT = "\n".join(("\nMain Menu", 
        "Type a number from the options below",
        "1 - Send a Thank You to a single donor",
        "2 - Create a Report",
        "3 - Send letters to all donors",
        "4 - Quit\n"))

SUB_PROMPT = "\n".join(("\nThank You",
            "Type a number from the options below",
            "1 - View all donor names",
            "2 - Add donation for current donor",
            "3 - Add donation for new donor",
            "4 - Back to main menu\n"))


def menu_selection(prompt, switch_dict):
    while True:
        response = input(prompt)
        try: 
            func = switch_dict[response]()
        except KeyError:
            print("Not a valid option")
        else:
            if func == "exit menu":
                break

def exit_menu():
    return "exit menu"


def print_donors():
    print("\n".join([key for key in donor_db]))
    return "\n".join([key for key in donor_db])


def ask_for_name():
    name = input("Type donor name: ").title()
    return name

def ask_for_donation(name):
    try:
        donation = float(input(f"Add a donation amount for {name}: $"))
    except ValueError:
        donation = float(input(f"Please enter a number. Donation Amount: $"))
    return donation  

def generate_thank_you_text(name, donation):
    return f"\nDear {name},\n\nThank you so much for your donation of ${donation}.\n\nSincerely,\n\nThe Mailroom\n"



def current_donor_donation(name, donation):
    donor_db[name].append(donation)

def current_donor():
    name = ask_for_name()
    if name in donor_db.keys():
        donation = ask_for_donation(name)
        current_donor_donation(name, donation)
        print(generate_thank_you_text(name, donation))
    else:
        print("Donor is not in the system.")



def new_donor_to_database(name, donation):
    donor_db[name] = [donation]

def new_donor():
    name = ask_for_name()
    donation = ask_for_donation(name)
    new_donor_to_database(name, donation)
    print(generate_thank_you_text(name, donation))



SWITCH_SUB_PROMPT_DICT = {"1": print_donors, "2": current_donor, "3": new_donor, "4": exit_menu}


def thank_you():
    menu_selection(SUB_PROMPT, SWITCH_SUB_PROMPT_DICT)


def generate_report():
    report_list = ["{:<26}{}{}{}".format("Donor Name", "| Total Given ", "| Num Gifts ", "| Average Gift"),"-" * 66]
    for key, value in sorted(donor_db.items(), key=lambda t: sum(t[1]), reverse=True):
        report_list.append(("{:<27}${:12.2f}{:11}  ${:12.2f}".format(key, sum(value), len(value), sum(value)/len(value))))
    return "\n".join(report_list)


def display_report():
    print(generate_report())


def letter_text(name, donation):
    return f'Dear {name},\n\n\tThank you for your donation of ${donation}.\n\n\t\tSincerely,\n\t\t-The Mailroom'


def letter_to_all():
    for key, value in donor_db.items():
        with open(f'{key}.txt', 'w') as f:
            f.write(letter_text(key, value[-1]))
    print("Emails have been saved as .txt files in your working directory.")


SWITCH_FUNC_DICT = {"1": thank_you, "2": display_report, "3": letter_to_all, "4": exit_menu}


def main():
    print("\nWelcome to The Mailroom")
    menu_selection(PROMPT, SWITCH_FUNC_DICT)


if __name__ == '__main__':
    main()