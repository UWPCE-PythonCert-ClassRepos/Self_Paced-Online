#!/usr/bin/env python3
import os
import datetime

now = datetime.datetime.now()

"""
Lesson9 - Object Oriented Mailroom
"""

_donors = {
    'Jim Halpert': [1.00],
    'Pam Beesley': [1000.00, 2000.00, 3000.00],
    'Dwight Shrute': [2.00, 3.00],
    'Michael Scott': [10.00, 20.00, 30.00],
    'Andy Bernard': [500.00]
}


def format_currency_str(amount=None):
    return "${0:.2f}".format(float(amount))


class Donors:

    def __init__(self, donors=None):
        self.donors = donors if donors else _donors

    def list_donors(self):
        print('\n'.join([k for k in self.donors.keys()]))

    def sort_donors(self):
        sl = sorted(self.donors.items(), key=lambda x: sum(x[1]), reverse=True)
        return sl

    def donor_key_found(self, name=None):
        try:
            self.donors[name]
        except KeyError:
            return False
        else:
            return True

    @staticmethod
    def get_donor_summary(donors):
        """ pass summary list of strings that is ready for parsing"""
        summary = []
        for d in donors:
            name = d[0]
            donations = d[1]
            total = float(sum(donations))
            number = len(donations)
            str_total = format_currency_str(total)
            str_number = str(len(donations))
            str_average = format_currency_str(total / max(number, 1))
            summary.append([name, str_total, str_number, str_average])
        return summary

    @staticmethod
    def donor_email(name, donations):
        donations = format_currency_str(donations)
        m = ('\n\nDear {},\n\n'
             '        Thank you for your very kind donations totalling {}.\n\n'
             '        It will be put to very good use.\n\n'
             '               Sincerely,\n'
             '                  -The Team\n\n')
        print(m.format(name, donations))

    def generate_letters(self):
        cwd = os.getcwd()
        date = now.strftime('%Y-%m-%d')
        path = cwd + '/letters/'
        ext = '.txt'
        for key, val in self.donors.items():
            total_donations = sum(val)
            n = key.split(' ')
            file_path = "{}{}_{}_{}{}".format(path, date, n[0], n[1], ext)
            donations = format_currency_str(total_donations)
            with open(file_path, 'w') as letter:
                text = ('\n\nDear {} {},\n\n'
                        '        Thank you for your very kind '
                        'donation of {}.\n\n'
                        '        It will be put to very good use.\n\n'
                        '               Sincerely,\n'
                        '                  -The Team\n\n')
                body = text.format(n[0], n[1], donations)
                letter.write(body)
        print('\n\n========== Letters Created ==========\n\n')

    def create_report(self):
        sorted_donors = self.sort_donors()
        rows = self.get_donor_summary(sorted_donors)
        self.print_report(rows)

    @staticmethod
    def print_report(rows):
        # table heading
        h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        hs = ' | '
        hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
        print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))
        # table rows
        for r in rows:
            name = "{}".format(r[0])
            f0 = '{0:<' + str(max(len(name), 25)) + '}'
            f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
            f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
            f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
            rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
            args = [name, '  $', r[1], ' | ', r[2], '  $', r[3]]
            print(rf.format(*args))

    def donor_summary(self, name):
        summary = ('\n\n===========================\n'
                   'Donor: {}\n'
                   'Total Donations: {}.\n'
                   'Donation Count: {}\n'
                   'Donation Average: {}\n'
                   '===========================\n\n')
        total = self.donations_total(name)
        count = self.donations_count(name)
        average = self.donations_average(name)
        print(summary.format(name, total, count, average))

    def donations_total(self, name=None):
        return format_currency_str(sum(self.donors[name]))

    def donations_count(self, name=None):
        return len(self.donors[name])

    def donations_average(self, name=None):
        total = sum(self.donors[name])
        count = len(self.donors[name])
        return format_currency_str(total / count)


class Donor():

    @staticmethod
    def donors_update(name, donation):
        db = Donors()
        """ Update base donor dictionary """
        if db.donor_key_found(name) is False:
            # new donor
            db.donors[name] = [float(donation)]
        else:
            # existing donor
            db.donors[name].append(float(donation))

    @staticmethod
    def donor_email(name, donation):
        donation = format_currency_str(donation)
        m = ('\n\nDear {},\n\n'
             '        Thank you for your very kind donation of {}.\n\n'
             '        It will be put to very good use.\n\n'
             '               Sincerely,\n'
             '                  -The Team\n\n')
        print(m.format(name, donation))


class MailroomCli:

    @staticmethod
    def prompt_name():
        while True:
            name = input('Type donor name: ')
            try:
                if name is None:
                    raise ValueError()
            except ValueError:
                print('Name string required.')
                continue
            return name

    @staticmethod
    def prompt_donation():
        while True:
            donation = input('Donation amount: ')
            try:
                donation = float(donation)
            except ValueError:
                print('Input must be a int/float, try again.')
                continue
            return donation

    def process_new_donor(self):
        db = Donors()
        d = Donor()

        while True:
            name = self.prompt_name()
            if db.donor_key_found(name) is False:
                break
            else:
                print('Donor already exists, use append.')

        donation = self.prompt_donation()
        self.thank_donor(name, donation)
        d.donors_update(name, donation)

    def process_donation(self):
        db = Donors()
        d = Donor()

        while True:
            name = self.prompt_name()
            if db.donor_key_found(name) is False:
                print('Type the exact donor name (see list): ', end='\n\n')
                db.list_donors()
                continue
            else:
                break

        donation = self.prompt_donation()
        self.thank_donor(name, donation)
        d.donors_update(name, donation)

    def call_summary(self):
        db = Donors()
        while True:
            name = self.prompt_name()
            if db.donor_key_found(name) is False:
                print('Type the exact donor name (see list): ', end='\n\n')
                db.list_donors()
                continue
            else:
                break
        db.donor_summary(name)

    def thank_donor(self, name=None, amount=None):
        db = Donors()
        d = Donor()

        if name is not None:
            # called by method
            d.donor_email(name, amount)  # single donation
        else:
            # called by menu
            while True:
                name = self.prompt_name()
                if db.donor_key_found(name) is True:
                    amount = db.donors[name]
                    break
                else:
                    print('Type the exact donor name (see list): ', end='\n\n')
                    db.list_donors()
            db.donor_email(name, sum(amount))  # total donations

    @staticmethod
    def call_report():
        db = Donors()
        db.create_report()

    @staticmethod
    def call_list():
        db = Donors()
        db.list_donors()

    @staticmethod
    def call_letters():
        db = Donors()
        db.generate_letters()

    @staticmethod
    def quit_menu():
        return 'break'

    def main_menu(self):
        main_prompt = ("\n--- MAIN MENU ---\n"
                       "What do you want to do?\n"
                       "Type '1' - Donors Menu\n"
                       "Type '2' - Reports Menu\n"
                       "Type '3' - Gratitude Menu\n"
                       "Type 'q' - Quit >> "
                       )
        main_dispatch = {'1': self.donors_sub_menu,
                         '2': self.reports_sub_menu,
                         '3': self.gratitude_sub_menu,
                         'q': self.quit_menu,
                         }
        self.menu_selection(main_prompt, main_dispatch)

    def donors_sub_menu(self):
        donors_prompt = ("\n--- DONOR SUB MENU ---\n"
                         "Type '1' - Add Donor\n"
                         "Type '2' - Append Donation\n"
                         "Type '3' - List Donors\n"
                         "Type 'q' - Quit >> "
                         )
        donors_dispatch = {'1': self.process_new_donor,
                           '2': self.process_donation,
                           '3': self.call_list,
                           'q': self.quit_menu,
                           }
        self.menu_selection(donors_prompt, donors_dispatch)

    def reports_sub_menu(self):
        reports_prompt = ("\n--- REPORTS SUB MENU ---\n"
                          "Type '1' - Donors Report\n"
                          "Type '2' - Donor Summary\n"
                          "Type 'q' - Quit >> "
                          )
        reports_dispatch = {'1': self.call_report,
                            '2': self.call_summary,
                            'q': self.quit_menu,
                            }
        self.menu_selection(reports_prompt, reports_dispatch)

    def gratitude_sub_menu(self):
        gratitude_prompt = ("\n--- GRATITUDE SUB MENU ---\n"
                            "Type '1' - Print Individual Letter\n"
                            "Type '2' - Generate Letters for All Donors\n"
                            "Type 'q' - Quit >> "
                            )
        gratitude_dispatch = {'1': self.thank_donor,
                              '2': self.call_letters,
                              'q': self.quit_menu,
                              }
        self.menu_selection(gratitude_prompt, gratitude_dispatch)

    @staticmethod
    def menu_selection(prompt, dispatch):
        while True:
            r = input(prompt)
            if r not in dispatch:
                print('Please choose a valid menu option.')
                continue
            if dispatch[r]() == "break":
                break


if __name__ == "__main__":
    MailroomCli().main_menu()
