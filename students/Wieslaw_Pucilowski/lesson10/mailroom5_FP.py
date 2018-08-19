import copy as cp

__author__ = "Wieslaw Pucilowski"


class Donor():
    def __init__(self, val=None):
        self.name = val
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if val is None:
            self._name = None
        else:
            self._name = tuple(val.split())

    @staticmethod
    def check_list(l):
        return all((isinstance(item, int) or
                    isinstance(item, float)) for item in l)

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.donations.append(val)
        elif self.check_list(val):
            self._donations = val
        else:
            raise ValueError("Donation should be in USD!")

    def above_min(self, min_don):
        return list(filter(lambda x: x >= min_don, self.donations))

    def below_max(self, max_don):
        return list(filter(lambda x: x <= max_don, self.donations))

    def between_min_max(self, min_don, max_don):
        return list(filter(lambda x: min_don <= x <= max_don, self.donations))

    def above(self, min_don):
        return list(filter(lambda x: x > min_don, self.donations))

    def below(self, max_don):
        return list(filter(lambda x: x < max_don, self.donations))

    def multiply_donations(self, factor, min_donation=None,
                           max_donation=None):
        if min_donation and max_donation:
            ll = self.below(min_donation) + \
                 list(map(lambda x: x * factor,
                          self.between_min_max(min_donation,
                                               max_donation))) + \
                 self.above(max_donation)
        elif min_donation and not max_donation:
            ll = self.below(min_donation) + (
                list(map(lambda x: x * factor, self.above_min(min_donation))))
        elif max_donation and not min_donation:
            ll = list(map(lambda x: x * factor, self.below_max(max_donation))
                      ) + self.above(max_donation)
        else:
            ll = list(map(lambda x: x * factor, self.donations))
        self.donations = ll
        return(self)

    @property
    def total(self):
        return sum(self.donations)

    @property
    def average(self):
        return sum(self.donations) / len(self.donations)

    @property
    def number(self):
        return len(self.donations)

    @property
    def greetings(self):
        g1 = """
    Ex Programmers Charity
    1999 Heartbeat Avenue
    11111 Fresh Spring, Alaska

    Dear"""
        g2 = "".join([' {}']*len(self.name)).format(*self.name)
        g3 = """

    Thank you so much for your generous donation of ${}

    It will be put to very good use.

                       Sincerely,
                          -The Team

    """.format(self.total)
        return(g1+g2+","+g3)

    @property
    def print_greetings(self):
        print(self.greetings)

    def write_letter(self):
        try:
            with open("_".join(['{} ']*len(self.name)).
                      format(*self.name)+'.txt', 'w') as f:
                f.write(self.greetings)
        except IOErrors as e:
            print("""
                Cannot write a file, cought
                {}
            """.format(e))


# donors are organized in dictionary
class DonorsCollection():
    def __init__(self, val=None):
        self._donors = {}
        self.donors = val
        self.rep = ""

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, val):
        if val is not None:
            if isinstance(val, Donor):
                self._donors[val.name] = val
            else:
                raise ValueError("Must be instance od Donor class")
                return

    def add_donor(self):
        name = input("Type donor first and last name: ")
        donor_name = tuple(name.split())
        if donor_name in self.donors:
            self.donors[donor_name].donations = float(
                input(" Donation in USD: "))
        else:
            d = Donor(name)
            try:
                d.donations = float(input("Donation in USD: "))
            except ValueError:
                print("""
                      Donation must be in USD...
                      Donor not added
                      """)
                del(d)
                return
            self.donors = d
        self.donors[donor_name].print_greetings

    def display_key(self, a):
        return a[-1]

    def display(self):
        for donor in sorted(self.donors, key=self.display_key):
            print("".join(["{} "]*len(donor)).format(*donor))

    def custom_key(self, a):
        return(a[1].total)  # 2nd arg => dict value => Donor instance

    def challenge(self, factor, min_donation=None, max_donation=None):
        for donor in self.donors:
            self.donors[donor] = \
                self.donors[donor].multiply_donations(factor,
                                                      min_donation,
                                                      max_donation)

    @property
    def report(self):
        self.rep = ""
        self.rep += "{:<40}| {:<18}| {:<8}| {:<18}\n".format('Donor Name',
                                                             'Total Given',
                                                             'Num Gifts',
                                                             'Average Gift')
        self.rep += "{:-<90}\n".format('')
        for k, v in sorted(self.donors.items(),
                           key=self.custom_key, reverse=True):

            name = " ".join(["{} "]*len(k)).format(*k)
            self.rep += "{:<40}{}{:>18.2f}{:>11}{}{:>17.2f}\n" \
                        .format(name, ' $', v.total, v.number, ' $', v.average)
        return(self.rep)

    def print_report(self):
        print(self.report)

    def write_letters(self):
        print("Sending letters to all donors...")
        for k, d in self.donors.items():
            d.write_letter()

    def projections(self, factor, min_donation=None, max_donation=None):
        for donor in self.donors.values():
            temp = cp.deepcopy(donor)  # projection done on donor copy
            print("Donor: {} Current total of dination: {} \
                   Total after factor applied: {}"
                  .format(donor.name, donor.total,
                          temp.multiply_donations(factor=factor,
                                                  min_donation=min_donation,
                                                  max_donation=max_donation)
                          .total))
            del(temp)
        answer = None
        while answer not in ['Yes', 'No']:
            answer = input("Whould you like to multiply " +
                           "(above min, below max) donations: [Yes, No]:")
        if answer == "Yes":
            self.challenge(factor,
                           min_donation=min_donation,
                           max_donation=max_donation)
            print("Changes applied...")
        else:
            print("No changes applied...")


# Donors DB initialization
dd = DonorsCollection()


class Main:
    @staticmethod
    def report():
        dd.print_report()

    @staticmethod
    def letters():
        dd.write_letters()

    @staticmethod
    def donor():
        dd.add_donor()

    @staticmethod
    def show():
        dd.display()

    @staticmethod
    def challenge():
        dd.challenge()

    @staticmethod
    def project(factor, min_donation, max_donation):
        dd.projections(factor, min_donation, max_donation)


if __name__ == "__main__":

    def menu_selection(prompt, dispatcher):
            while True:
                response = input(prompt)
                try:
                    if dispatcher[response]() == "exit menu":
                        break
                except KeyError:
                    print(response, "Wrong response !")

    def quit(msg):
        print("{}".format(msg))
        return "exit menu"

    def main_quit():
        return quit("Goodbye...")

    def sub_quit():
        return quit("Back to Main menu...")

    def sub_menu():
        menu_selection(submenu, subfeatures)

    def projections_prompt():
        try:
            factor = int(input("What is the multiplication factor:"))
        except ValueError:
            print("Multiplication factor should be integer...")
            return
        try:
            x = input("Above Min donation:")
            min_donation = float(x) if x != '' else None
            y = input("Below Max donation:")
            max_donation = float(y) if y != '' else None
        except ValueError:
            print("Min, Max donation should be in USD...")
            return
        Main.project(factor=factor, min_donation=min_donation, max_donation=max_donation)

    menu = """
        {:-^30}

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Projections
        q - Quit
    """.format(' Main Menu ')

    submenu = """
        {:-^30}

        1 - Add new donor, donation
        2 - List donors
        q - Go to Main Menu

    """.format(' Add/List donors ')

    features = {
            '1': sub_menu,
            '2': Main.report,
            '3': Main.letters,
            '4': projections_prompt,
            'q': main_quit,
            }

    subfeatures = {
            '1': Main.donor,
            '2': Main.show,
            'q': sub_quit,
            }

    d1 = Donor("Stephan LeClerc")
    d2 = Donor("Chris Ping")
    d3 = Donor("James Bond")
    for i in range(4):
        d1.donations, d2.donations, d3.donations = (10*i)+10, \
                                                   (10*i+2)+10, (10*i+3)+10
    dd.donors = d1
    dd.donors = d2
    dd.donors = d3
    # start program menu
    menu_selection(menu, features)
