class Donor(object):
    def __init__(self, donor=None, donation=None):
        self._donor = donor
        if type(donation) is list:
            self._donation = donation
        else:
            self._donation = [donation]

    @property
    def donor(self):
        return self._donor

    # @donor.Setter
    # def donor(self, donor):
    #     self._donor = donor.title()

    @property
    def donation(self):
        return self._donation

    @donation.setter
    def donation(self, donation=None):
        if donation is None:
            self._donation = []
        else:
            self._donation.append(donation)

    @property
    def total_donations(self):
        self._total_donations = sum(self._donation)
        return self._total_donations

    @property
    def donation_count(self):
        self._donation_count = len(self._donation)
        return self._donation_count

    @property
    def adv_donation(self):
        total = self.total_donations
        count = self.donation_count
        self._adv_donation = total / count
        return self._adv_donation

    def thank_you(self):
        file_name = "{}.txt".format(self.donor.replace(" ", "_"))
        donation = self.total_donations
        header = "Dear {},".format(self.donor)
        body = "Thank you for your donation of ${:.2f}.".format(donation)
        close = "\tSincerely,\n\t\t-The Team"
        letter = "{}\n{}\n\n{}".format(header, body, close)
        with open(file_name, 'w+') as f:
            f.write(letter)
        print("Thank you letter for {} created.".format(self.donor))

#================================
#================================


class Donors():
    def __init__(self):
        self._donor_list = []

    @property
    def donors(self):
        return self._donor_list

    def add_donor_donation(self, donor=None, donation=None):
        if self.is_donor(donor) is False:
            obj = Donor(donor, donation)
            self._donor_list.append(obj)
        else:
            d = self.instance_of(donor)
            d.donation = donation

    def donor_names(self):
        donor_names = []
        for d in self._donor_list:
            donor_names.append(d.donor)
        return donor_names

    def is_donor(self, donor):
        donor_names = self.donor_names()
        if donor in donor_names:
            return True
        else:
            return False

    def instance_of(self, donor):
        instance = None
        for d in self._donor_list:
            if donor == d.donor:
                instance = d
        return instance

    def thank_you(self, donor_name):
        if self.is_donor(donor_name) is True:
            d = self.instance_of(donor_name)
            file_name = "{}.txt".format(d.donor.replace(" ", "_"))
            donation = d.total_donations
            header = "Dear {},".format(d.donor)
            body = "Thank you for your donation of ${:.2f}.".format(donation)
            close = "\tSincerely,\n\t\t-The Team"
            letter = "{}\n{}\n\n{}".format(header, body, close)
            with open(file_name, 'w+') as f:
                f.write(letter)
            print("Thank you letter for {} created.".format(d.donor))
        else:
            print("{} is not in the list of donors.".format(donor_name))

    def report(self):
        print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
        print("-" * 68)
        for d in self._donor_list:
            n = d.donor
            tg = d.total_donations
            c = d.donation_count
            ave = d.adv_donation
            s = f'{n:<21}{"$":<1}{tg:>14.2f}{" ":<1}{c:>15}{" ":<1}{"$":<1}{ave:>14.2f}'
            print(s)



################


def menu():
    while True:
        try:
            print("\n==========================================")
            print("Would you like to:")
            print("\t1 - Send a thank you letter.")
            print("\t2 - Send thank you letters to everyone.")
            print("\t3 - Add a donation.")
            print("\t4 - Create a report.")
            print("\t5 - Search for a donor.")
            print("\t6 - Quit.")
            response = int(input(">>> "))
            return response
            break
        except ValueError:
            print("Oops: Please select an option (1-5):")
            pass


def run_func():
    while True:
        response = menu()
        if response == 1:
            name = input("Who would you like to thank? ").title()
            d1.thank_you(name)
        elif response == 2:
            for name in d1.donor_names():
                d1.thank_you(name)
        elif response == 3:
            name = input("Who has made the donation? ").title()
            amount = int(input("How much was donated? "))
            d1.add_donor_donation(name, amount)
        elif response == 4:
            d1.report()
        elif response == 5:
            name = input("Who are you looking for? ").title()
            if d1.is_donor(name) is True:
                print("{} is a donor.".format(name))
            else:
                print("{} is not a donor.".format(name))
        elif response == 6:
            break


if __name__ == '__main__':
    d1 = Donors()
    d1.add_donor_donation("Anita Bath", [200, 150])
    d1.add_donor_donation("Isabelle Ringing", [101])
    d1.add_donor_donation("John Smith", [100])
    d1.add_donor_donation("Seymour Butz", [95, 500])
    run_func()



