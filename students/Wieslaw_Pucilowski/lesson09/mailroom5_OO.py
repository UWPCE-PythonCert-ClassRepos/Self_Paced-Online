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
        self.wrong_option = "{:<20}".format(" - Wrong option !!!")
        self.main_prompt = """
        {:-^30}

        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        q - Quit
    """.format(' Main Menu ')
        self.sub_prompt = """
        {:-^30}

        1 - Add new donor, donation
        2 - List donors
        q - Go to Main Menu

    """.format(' Add/List donors ')
        self.main_dispatch = {
            '1': self.sub_menu,
            '2': self.print_report,
            '3': self.write_letters,
            'q': self.quit_menu, }
        self.sub_dispatch = {
            '1': self.add_donor,
            '2': self.display,
            'q': self.quit_menu, }

    def menu_selection(self, prompt, dispatch_dict):
        while True:
            response = input(prompt)
            try:
                if dispatch_dict[response]() == "exit menu":
                    break
            except KeyError:
                print(response, self.wrong_option)

    def main_menu(self):
        self.menu_selection(self.main_prompt, self.main_dispatch)

    def sub_menu(self):
        self.menu_selection(self.sub_prompt, self.sub_dispatch)

    def quit_menu(self):
        print("Goodbye...\n")
        return "exit menu"

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

    def add_donor(self):
        name = input("Type donor first and last name: ")
        donor_name = tuple(name.split())
        if donor_name in self.donors:
            self.donors[donor_name].donations = float(
                input(" Donation in USD: "))
        else:
            d = Donor(name)
            d.donations = float(input("Donation in USD: "))
            self.donors = d
        self.donors[donor_name].print_greetings

    def display_key(self, a):
        return a[-1]

    def display(self):
        for donor in sorted(self.donors, key=self.display_key):
            print("{} {},".format(donor[0], donor[1]))

    def custom_key(self, a):
        return(a[1].total)  # 2nd arg => dict value => Donor instance

    @property
    def report(self):
        self.rep = ""
        self.rep += "{:<30}| {:<18}| {:<8}| {:<18}\n".format('Donor Name',
                                                             'Total Given',
                                                             'Num Gifts',
                                                             'Average Gift')
        for k, v in sorted(self.donors.items(),
                           key=self.custom_key, reverse=True):
            self.rep += "{:<30}{}{:>18.2f} \
                        {:>11}{}{:>17.2f}\n".format(k[0]+' '
                                                    + k[1],
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


if __name__ == "__main__":

    d1 = Donor("Stephan LeClerc")
    d2 = Donor("Chris Ping")
    d3 = Donor("James Bond")
    for i in range(4):
        d1.donations, d2.donations, d3.donations = (10*i)+10, \
                                                   (10*i+2)+10, (10*i+3)+10
    dd = DonorsCollection()
    dd.donors = d1
    dd.donors = d2
    dd.donors = d3
    # start menu
    dd.main_menu()
