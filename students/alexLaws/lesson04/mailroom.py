#!/usr/bin/env python3

donor_list = []
donor_list.append({'Name': 'Ryan Moore', 'Donation': 500})
donor_list.append({'Name': 'Ryan Moore', 'Donation': 250})
donor_list.append({'Name': 'Ted Laws', 'Donation': 1000})
donor_list.append({'Name': 'Ted Laws', 'Donation': 100})
donor_list.append({'Name': 'Ben Snell', 'Donation': 150})
donor_list.append({'Name': 'Andrew Crawford', 'Donation': 2000})
donor_list.append({'Name': 'Andrew Crawford', 'Donation': 2000})
donor_list.append({'Name': 'Andrew Crawford', 'Donation': 4000})
donor_list.append({'Name': 'Beth Ross', 'Donation': 400})


def user_action():
    print("Choose an action from this list:")
    print("Send a Thank You")
    print("Create a Report")
    print("Quit")
    while True:
        option = input("What is your choice: ")
        if option.lower() in ["send a thank you", "create a report", "quit"]:
            return option
            break
        else:
            print("That is not an option. Choose again.")


def dnrs(x):
    names = []
    for dnr in x:
        person = dnr.get("Name")
        if person in names:
            pass
        else:
            names.append(person)
    return names


def send_to(x):
    donors = dnrs(x)
    recipient = input("Who is the thank you note for? Enter a full name or 'list' to see a list: ")
    if recipient.lower() == 'list':
        print("Here are all the donors:")
        for name in donors:
            print(name)
        recipient = input("Who is the thank you note for? ")
        return recipient
    else:
        return recipient


def name_sum(person, x):
    donor_total = 0
    for i in x:
        if i.get('Name') == person:
            donor_total += int(i.get('Donation'))
    return donor_total


def name_cnt(person, x):
    donor_count = 0
    for i in x:
        if i.get('Name') == person:
            donor_count += 1
    return donor_count


def thank_you(recip, x):
    print("OK, here is a thank you note for {}".format(recip))
    total = name_sum(recip, x)
    note = "Dear {},\nThank you for your recent donation. You have now donated ${}.\nThank you so much!\n- Alex Laws"
    print(note.format(recip, total))


def total_sort(x):
    donors = dnrs(x)
    to_sort = []
    for i in donors:
        to_sort.append({'Name': i, 'Total': name_sum(i, x)})
    amounts = []
    for n in to_sort:
        amounts.append(n.get('Total'))
    amounts.sort(reverse=True)
    ordered = []
    for num in amounts:
        for i in to_sort:
            if i.get('Total') == num and i.get('Name') not in ordered:
                ordered.append(i.get('Name'))
    return ordered


def report(x):
    print("Donor Name       |  Total Given  |  Num Gifts  |  Average Gift")
    donors = total_sort(x)
    for donor in donors:
        total = name_sum(donor, x)
        number = name_cnt(donor, x)
        average = total / number
        print("{:17} ${:14,.2f} {:13} ${:13,.2f}".format(donor, total, number, average))


if __name__ == '__main__':
    while True:
        act = user_action().lower()
        if act == "send a thank you":
            name = send_to(donor_list)
            if name in dnrs(donor_list):
                thank_you(name, donor_list)
            else:
                amt = int(input("Wait, A new donation! How much: "))
                donor_list.append({'Name': name, 'Donation': amt})
                thank_you(name, donor_list)
        if act == "create a report":
            report(donor_list)
        if act == "quit":
            break
        print("Would you like to do something else...")
