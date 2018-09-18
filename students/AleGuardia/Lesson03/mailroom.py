#!/usr/bin/env python3

donations = [[['William Gates, III'], [1000000, 585000, 5750000]],
             [['Mark Zuckerberg'], [15000, 5000]],
             [['Jeff Bezos'], [3000000]],
             [['Paul Allen'], [25000,1000]],
             [['Elon Musk'], [30000,3499]]]

responses = ["Send a Thank You","Create a Report", "quit"]


def return_average(seq):
    return sum(seq)/len(seq)


def return_label():
    label ="{:18} | {:>12} | {:>9} | {:>12}\n".format('Donor Name','Total Given','Num Gifts','Average Gift')
    label += "-"*len(label)
    return label


def return_report(data):
    report = f"{return_label()}\n"
    for item in data:
        row = "{:18} $ {:>12.2f}  {:>9d}  $ {:>12.2f}\n".format(item[0][0],sum(item[1]),len(item[1]),return_average(item[1]))
        report += row
    return report


def initial_prompt():
    resp = input(f"Please choose one of the following: "
                 f"'{responses[0]}', '{responses[1]}', or '{responses[2]}' :")
    return resp


def return_donors():
    donors = ""
    for item in donations:
        donors += item[0][0] + "\n"
    return donors


def prompt_donors():
    name = input("Please enter a donor name: ")
    if name == 'quit':
        return None
    if name == 'list':
        print(return_donors())
        return prompt_donors()
    if name in return_donors():
        add_donation(name)
    return initial_prompt()


def add_donor(name):
    donations.append([[name],[]])
    return print(donations)


def return_pos(name):
    for i, donor in enumerate(donations):
        if name == donor[0][0]:
            return i


def add_donation(name):
    amount = float(input("Please enter a donation amount for {}:".format(name)))
    print(name)
    donations[return_pos(name)][1].append(float(amount))
    return initial_prompt()


if __name__ == '__main__':
    response = initial_prompt()
    while response != responses[-1]:
        if response == responses[0]:
            prompt_donors()
        elif response == responses[1]:
            print(return_report(donations))
        response = initial_prompt()







