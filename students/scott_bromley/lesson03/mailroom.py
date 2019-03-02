#!/usr/bin/env python3
import datetime

# prompt user to select from mailroom menu: send a thank you, create a report, or quit
# send a thank you: allows user to select a name, adds donor if not in donor list, otherwise ask for donation
# and thanks donor
# create a report summarizes the donors and their donations in a table
# quit ends the program


def main():
    donors = [["David Einhorn", "Mark Zuckerberg", "Seth Klarman", "Bill Ackerman"],
                 [1800.18, 36036.36],
                 [7272.72, 1818.18, 545454.54],
                 [180.00, 72.72, 18.00],
                 [324.32]]
    menu = ("Send a Thank You", "Create a Report", "quit")
    mailroom_open = True
    while mailroom_open is True:
        response = get_user_input(f"Please enter an option from the following menu: \n {menu} > ").strip()
        if response.casefold() == "send a thank you":
            full_name = get_user_input("Please enter the full name of a donor: > ").strip()
            if full_name in donors[0]:
                donation = float(get_user_input("Please enter the donation amount: > ").strip('$'))
                donors[donors[0].index(full_name) + 1].append(donation)
                send_thank_you(full_name, donation)
                continue
            else:
                add_donor(full_name, donors)
                continue
        elif response.casefold() == "create a report":
            create_report(donors)
            continue
        elif response.casefold() == "quit":
            mailroom_open = False
        else:
            print(f"The option you entered '{response}' is invalid, please try again.")
            continue


def send_thank_you(full_name, donation):
    '''
    :param full_name: name of the donor
    :param donation: the amount donated
    :return: None
    '''
    now = datetime.datetime.now()
    print(f'''
    {now.date()} 
    
    Dear {full_name},

    On behalf of all of us at the ADL-PNW office we'd like to recognize and thank you for your generous 
    donation of ${donation}.  These funds will be used to further our mission in the Pacific Northwest
    through leadership programs and education.  We look forward to seeing you at this year's banquet. 
    
    Sincerely, 
    
    ADL-PNW, Seattle

    ''')
    return None


def create_report(donors=None):
    '''
    prints a formatted table of donors ranked in descending order by Total Given
    :param donors: list of donors and donations
    :return: None
    '''
    if donors is None:
        donors = []
    names, totals, num_gifts, avg_gift = get_donor_summary(donors)
    print(f"Donor Name{'':<20} | Total Given{'':>0} | Num Gifts{'':>0} | Average Gift{'':>0}")
    print(f"-" * 72)
    for name, total, num_gift, avg_gift in zip(names, totals, num_gifts, avg_gift):
        print(f"{name:<32}${total:>11}{num_gift:>12}  ${avg_gift:>13}")
    return None


def get_donor_summary(donors=None):
    '''
    :param donors: list of donors and donations
    :return: lists of names, totals, number of gifts, avg gift sorted by highest total
    '''
    if donors is None:
        donors = []
    totals = [float(format(sum(donations), '.2f')) for donations in donors[1:]]
    num_gifts = [len(gifts) for _, gifts in sorted(zip(totals, donors[1:]), reverse=True)]
    avg_gift = [float(format(sum(donations) / len(donations), '.2f')) for _, donations in sorted(zip(totals, donors[1:])
                                                                                                 , reverse=True)]
    names = [names for _, names in sorted(zip(totals, donors[0]), reverse=True)]
    totals.sort(reverse=True)
    return names, totals, num_gifts, avg_gift


def add_donor(donor_name, donors=None):
    '''
    :param donor_name: full name of donor
    :param donors: list of donors
    :return: updated list of donors
    '''
    if donors is None:
        donors = []
    donors[0].append(donor_name)
    donors.append([])
    return donors


def get_user_input(prompt):
    '''
    :param prompt: prompt for user to respond to
    :return: response to question/prompt
    '''
    response = input(prompt).strip()
    return response


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)