







from pathlib import Path


class Donor(object):
    """
    This donor class will hold private information about a donor.
    """
    def __init__(self, name, donation_amount=None):
        """
        Initializes a donor.
        :param name: Name of the donor
        :param donation_amount: Single donation amount or list of donation amount
        """
        self.name = name
        if isinstance(donation_amount, float):
            self.donations = [donation_amount]
        elif isinstance(donation_amount, list):
            self.donations = donation_amount
        elif donation_amount is None:
            self.donations = []
        else:
            print('Please enter a valid amount.')

    @property
    def total_donation(self):
        return sum(self.donations)

    @property
    def number_of_gifts(self):
        return len(self.donations)

    @property
    def average_donation(self):
        return self.total_donation / self.number_of_gifts

    @property
    def thank_you_note(self):
        return f'Dear {self.name}, we want to thank you for your total donation amount of ${self.total_donation}.' \
            f' Have a nice day!'

    def add_donations(self, donation_amount):
        """
        Add a donation.
        :param donation_amount: Donation amount
        :return: Donor object
        """
        self.donations.append(donation_amount)
        return self


class Database(object):
    """
    A collection of donor objects that holds summarized information about the fund.
    """
    def __init__(self, donors=None):
        """
        Initializes a database.
        :param donors: List of donors to initialize the database with.
        """
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        """
        Add a donor to the collection.
        :param donor: Donor object to be added.
        :return: None
        """
        if isinstance(donor, Donor):
            self.donors.append(donor)
        else:
            print('Please add a valid donor.')

    @property
    def all_names(self):
        return [d.name for d in self.donors]

    def create_report(self):
        """
        Create a tabular report of the current donation status.
        :return: A formatted string of the table.
        """
        result = '{:<26} | {:^11} | {:^8} | {:>12}\n'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        result += '-' * len(result) + '\n'
        for d in self.donors:
            name = d.name
            total_donation = d.total_donation
            number_of_gifts = d.number_of_gifts
            average_donation = d.average_donation

            result += '{:<27} ${:>11.2f} {:>12} ${:>13.2f}\n'.format(name, total_donation, number_of_gifts,
                                                                     average_donation)

        return result

    def thank_all(self, folder='letters/'):
        """
        Outputs files with grateful notes for each donor.
        :param folder: Output folder of the files.
        :return: None
        """
        for donor in self.donors:
            filename = Path(f'./{folder}{donor.name}.txt')
            filename.parent.mkdir(parents=True, exist_ok=True)
            with filename.open('w') as outfile:
                outfile.write(donor.thank_you_note)


if __name__ == '__main__':
    def initialize_donors():
        """
        Initialize default donors.
        :return: List of default donors
        """
        don_1 = Donor('Amy Walker', [18900.90, 4500])
        don_2 = Donor('Peter Thomson', [9999.99, 500, 6000.88])
        don_3 = Donor('July Jensen', [5300.00, 200])
        don_4 = Donor('Paul Allen', [320.57])
        don_5 = Donor('Jenny Palmer', [66.89])
        return [don_1, don_2, don_3, don_4, don_5]

    db = Database(initialize_donors())


    def donate(donor):
        """
        Show interface to add donation from a donor and show gratitude.
        :param donor: Subject donor.
        :return: Updated donor object.
        """
        # Once a name has been selected, prompt for a donation amount
        try:
            donation_amount = float(input('Enter the amount you want to donate: $'))
            donor = donor.add_donations(donation_amount)
            while True:
                more = input('Is there another gift amount you want to enter? (y/n) ')
                if more[0].lower() == 'y':
                    donation_amount = float(input('That\'s so nice of you! Enter the amount you want to donate: $'))
                    # Once an amount has been given, add that amount to the donation history of the selected user
                    donor = donor.add_donations(donation_amount)

                # Use string formatting to compose an email thanking the donor for their generous donation.
                elif more.lower() == 'n':
                    print(donor.thank_you_note)
                    break
        except ValueError:
            print("please enter a valid number")
            donate(donor)

        return donor


    def send_thank():
        """
        Select donor to accept donation.
        :return: None
        """
        while True:
            # If the user types ‘list’, show them a list of the donor names and re-prompt

            user_input = input(
                'Please enter a full name, type "list" to see the list of donors, type "back" to go back: ')
            if user_input.lower() == 'list':
                for name in db.all_names:
                    print(name)
                continue

            elif user_input.lower() == 'back':
                # back to the main menu
                return
            # If the user types a name in the list, use it.
            elif user_input.lower() in [d.name.lower() for d in db.donors]:
                for d in db.donors:
                    if d.name.lower() == user_input.lower():
                        donate(d)
                        # exit for loop on name match
                        break
            else:
                # If the user types a name not in the list, add that name to the data structure and use it
                d = donate(Donor(user_input))
                db.add_donor(d)
                break


    def menu_selection(prompt, dispatch_dict):
        """
        List options for user inputs.
        :param prompt: Instruction for user input.
        :param dispatch_dict: User input and corresponding behaviors
        :return: None
        """
        while True:
            response = input(prompt)
            result = dispatch_dict[response]()
            if result == "exit":
                break


    def create_report():
        """
        Print a tabular report of the current donation status.
        :return: None
        """
        print(db.create_report())

    # quote menu function
    def quit_program():
        """
        Terminate program.
        :return: Exit code
        """
        print('Bye.')
        return "exit"


    main_prompt = ("Please choose one of the actions in menu:\n1. Send a Thank you.\n2. Create a report.\n"
                   "3. Send thank you letter to everyone.\n4. Quit.\nEnter the number of the action you want to make: ")

    main_dispatch = {'1': send_thank,
                     '2': create_report,
                     '3': db.thank_all,
                     '4': quit_program}
    try:
        menu_selection(main_prompt, main_dispatch)
    except KeyError:
        print("The action you take is not valid.")
        menu_selection(main_prompt, main_dispatch)












