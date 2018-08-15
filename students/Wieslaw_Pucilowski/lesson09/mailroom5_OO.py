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

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.donations.append(val)
        else:
            raise ValueError("Donation should be in USD!")

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
            self.rep += "{:<40}{}{:>18.2f}{:>11}{}{:>17.2f}\n".format(name,
                                                        ' $',
                                                        v.total,
                                                        v.number,
                                                        ' $',
                                                        v.average)

        return(self.rep)

    def print_report(self):
        print(self.report)

    def write_letters(self):
        print("Sending letters to all donors...")
        for k, d in self.donors.items():
            d.write_letter()


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

    menu = """
        {:-^30}

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
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

