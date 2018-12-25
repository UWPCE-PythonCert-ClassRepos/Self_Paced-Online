#!/usr/bin/env python3
"""Takes donor and donation information and sends thank you notes. Adds donors and donations and reports it"""


# Donor Collection class - could be in different module
class Donors():
    def __init__(self):
        self.donors = []

    def add_donor(self, donor):
        self.donors.append(donor)

    def return_donors(self):
        return [x.name for x in self.donors]

    def donor_existence(self,name):
        return name in self.return_donors()

    def donor_summary(self):
        return [{"name": x.name, "total": x.total_donations(), "number": x.number_donations(),
                 "average": x.average_donation()} for x in self.donors]

    def return_donor(self,name):
        for x in self.donors:
            if x.name == name:
                return x

    def return_report(self):
        """Creates and prints a report of donors and donations"""
        report = f"{return_label()}\n"
        for item in self.donor_summary():
            row = "{:18} $ {:>12.2f}  {:>9d}  $ {:>12.2f}\n".format(item['name'],
                                                                    item['total'],
                                                                    item['number'],
                                                                    item['average'])
            report += row
        return report

    def send_letters(self,note):
        for don in self.donors:
            # write_letter(item, don_list[item][-1], note_format)
            outfile = open(don.name.replace(" ","_")+".txt", 'w')
            outfile.write(note.format(don.name, don.donations[-1]))



# Donor class - could be in a different module
class Donor():
    def __init__(self,name):
        self.name = name
        self.donations = []

    def add_donation(self,donation):
        self.donations.append(donation)

    def total_donations(self):
        return sum(self.donations)

    def average_donation(self):
        return sum(self.donations)/len(self.donations)

    def number_donations(self):
        return len(self.donations)


# Create Donor Collection for testing
donors = Donors()
d1 = Donor("William Gates, III")
d2 = Donor("Mark Zuckerberg")
d3 = Donor("Jeff Bezos")
d4 = Donor("Paul Allen")
d5 = Donor("Elon Musk")
donor_list = [d1, d2, d3, d4, d5]
for donor in donor_list:
    donors.add_donor(donor)
d1.add_donation(1000000)
d1.add_donation(585000)
d1.add_donation(5750000)
d2.add_donation(15000)
d2.add_donation(5000)
d3.add_donation(3000000)
d4.add_donation(25000)
d4.add_donation(1000)
d5.add_donation(30000)
d5.add_donation(3499)


# User interface

main_responses = {1:"1 - Send a Thank You\n", 2:"2 - Create a Report\n",
                  3: "3 - Send letters to everyone\n",4:"4 - quit\n"}
main_prompt = f"Please choose one of the following:\n" \
              f"{main_responses[1]}{main_responses[2]}{main_responses[3]}{main_responses[4]}"
thank_you_note = "Dear {}:\n\nWe want to thank you for your generous donation of ${:.2f}.\n\n" \
                 "It will be put to very good use.\n\n" \
                 "\tSincerely,\n\t\tThe Team"


def return_label():
    """Builds and returns a table row label"""
    label ="{:18} | {:>12} | {:>9} | {:>12}\n".format('Donor Name','Total Given','Num Gifts','Average Gift')
    label += "-"*len(label)
    return label


def prompt_donors():
    """Prompt donor name and adds donor and donations"""
    name = input("Please enter a donor name: ")
    if name == 'quit':
        return None
    if name == 'list':
        print()
        print(*donors.return_donors(), sep="\n")
        print()
        return prompt_donors()
    if not donors.donor_existence(name):
        donors.add_donor(Donor(name))
    return send_note(name, add_donation(name), thank_you_note)


def add_donation(name):
    """Takes the name of a donor and adds a donation on his behalf"""
    while True:
        try:
            amount = float(input("Please enter a donation amount for {}:".format(name)))
            donors.return_donor(name).add_donation(float(amount))
            return amount
        except ValueError:
            print("Please enter only digits")


def send_note(name,donation,note):
    """Takes a donor name,donation amount and a note and sends the note to the donor"""
    print()
    print(note.format(name,donation))
    print()
    return note.format(name,donation)


def menu_selection(prompt, dispatch_dict, key_def=None):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "quit":
                break
        except KeyError:
            if not callable(key_def):
                print("Please enter a valid number")
            else:
                key_def(donors)


def print_report():
    print()
    report = donors.return_report()
    print(report)
    return report


def quit_sys():
    return "quit"


def send_letters():
    donors.send_letters(thank_you_note)


def create_letters(don_list, note_format):
    for item in don_list:
        write_letter(item,don_list[item][-1],note_format)


def write_letter(donor, donation,note):
    outfile = open(file_name(donor),'w')
    outfile.write(note.format(donor,donation))


def file_name(donor):
    return donor.replace(" ","_")+".txt"


main_dispatch = {"1": prompt_donors, "2": print_report, "3": send_letters, "4": quit_sys}


if __name__ == '__main__':
    menu_selection(main_prompt,main_dispatch)

