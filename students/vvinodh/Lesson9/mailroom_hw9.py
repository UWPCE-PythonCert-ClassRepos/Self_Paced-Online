from operator import itemgetter
import os
import sys
import datetime


class Donor:
    def __init__(self, donation=None):
        self.donation = donation if donation else []
        self.total = sum(self.donation)
        self.ave = self.total/len(self.donation) if donation else 0
        self.num_donations = len(self.donation)
        self.last = self.donation[-1]

donor_data = {
        'William Gates, III': [65000.00, 2, 326892.24],
        'Mark Zuckerberg': [16000.00, 3, 5465.37],
        'Jeff Bezos': [877.33, 1, 877.33],
        'Paul Allen': [708.42, 3, 236.14],
              }


class Donor_ops:


    def donor_append(name, don):
        try:
            donor_data[name].append(don)
        except KeyError:
            donor_data.setdefault((name), []).append(don)

    def thank_you(query):
        if query != 'list' and query != 'menu':
            donation_info = Donor(donor_data[query])
            thank_you_text = str(f"""\n---------------- Thank You ----------------\n
Dear {query},\n
Thank you for your contribution of ${donation_info.last:,.2f}.
It will be put to very good use.\n
Sincerely,
Vinodh""")

            return thank_you_text
        elif query == 'list':
            return Donor_ops.list_donors()
        else:
            return 'returning to main menu...'


    def list_donors():
        list_text = str("\n---------------- List of Donors ----------------\n\n")
        for donor in donor_data:
            list_text += (donor + '\n')
        return list_text

    def report():
        columns = ["DONOR", "TOTAL", "AVERAGE", "NUMBER"]
        report_text = str("\n--------------- Report -------------\n\n")
        report_text += str('{:<30}{:<15}{:<15}{:<15}\n'.format(*columns))
        for name in donor_data:
            donation_info = Donor(donor_data[name])
            report_text += str('{:<30}{:<15}{:<15,.2f}{:<15}\n'.format(name, donation_info.total, donation_info.ave, donation_info.num_donations))
        return report_text

    def letters():
        letters_text = """\n--------- Exporting Letters to Everyone ---------\n
Thank you letters have been exported to {}""".format(os.getcwd())
        for name in donor_data:
            donation_info = Donor(donor_data[name])
            letter = f"""Dear {name},

Thank you for your contribution of ${donation_info.last:,.2f}. It will be put to very good use.

Sincerely,
Vinodh"""
            with open(str(name) + "_" + str(datetime.date.today()) + '.txt', 'w') as out_file:
                out_file.write(letter)
        return letters_text



class user_input:

    def menu_render(text, key):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Choose an action:\n")
        for line in text:
            print(line)
        choice = input("-> ")
        if key[choice] == Donor_ops.thank_you:
            print_function(key[choice](user_input.donation_query()))
        else:
            try:
                print_function(key[choice]())
            except (KeyError):
                print("\nChoose an action:")
                for item in key:
                    print(f'"{item}",', end=" ")
                print("\n")

    # user input for new donations
    def donation_query():
        query = input("\nEnter first and last name of a donor\nor 'list' or 'menu'\n->")
        if query == 'list':
            return 'list'
        elif query == 'menu':
            return 'menu'
        try:
            donation_amount = float(input("What is the donation amount?\n->"))
        except(ValueError):
            print('invalid entry')
            user_input.menu_render(main_menu_text, main_menu_key)
        Donor_ops.donor_append(query, donation_amount)
        return query


def print_function(function):
    print(function)


def Ex():
    sys.exit("quiting application")


def main():
    while True:
        user_input.menu_render(main_menu_text, main_menu_key)


main_menu_text = ["Press 1 to send a Thank You", "Press 2 to create a report", "Press 3 to print letters", "Press 4 to quit"]
main_menu_key = {'1': Donor_ops.thank_you, '2': Donor_ops.report, '3': Donor_ops.letters, '4': Ex}


if __name__ == '__main__':
    main()
