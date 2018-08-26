#!/usr/bin/env python3

class Donor:
    """
    An individual donor, consisting of a name, a list of donations and a set of properties for commonly used attributes
    including total donations, average donations, and number of donations
    """
    def __init__(self, name, donations=None):
        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = donations
        self._total_donations = 0
        for donation in self._donations:
            self._total_donations += donation

    @property
    def total_donations(self):
        return self._total_donations

    @property
    def name(self):
        return self._name

    @property
    def avg_donation(self):
        return self._total_donations/self.num_donations

    @property
    def num_donations(self):
        return len(self._donations)

    def challenge(self, factor, min=None, max=None):
        """
        Runs challenge projections on the donations and returns the list of filtered, scaled donations
        :param factor: scaling factor for donations
        :param min: minimum donation filter
        :param max: maximum donation filter
        """
        filter_list = self._donations
        if min is not None:
            filter_list = list(filter(lambda x: x >= min, filter_list))
        if max is not None:
            filter_list = list(filter(lambda x: x <= max, filter_list))
        return list(map(lambda x: x*factor, filter_list))

    def add_donation(self, donation):
        """
        Add a new donation entry for this donor
        :param donation: the new donation amount
        """
        self._donations.append(donation)
        self._total_donations += donation

    def create_thank_you(self, donation):
        """
        Prints a thank for you the given donor and amount
        :param donation: dictionary containing name of the donor to thank and the amount donated
        :returns: formatted thank you string
        """
        return f"Dear {self.name},\nThank you for your very generous donation of ${donation:.2f}.  It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n{'Sincerely':>40}\n{'Art Vandelay':>50}"

    def __lt__(self, other):
        return self.total_donations < other.total_donations

    def __eq__(self, other):
        return self.name == other.name and self._donations == other._donations

class Donors:
    """
    A collection of donors
    """
    def __init__(self, donors=None):
        if donors is None:
            self._donors = []
        else:
            self._donors = donors

    def add_donor(self, donor):
        """
        Add a new donor to the donors list
        :param donor: the new donor to add
        """
        self._donors.append(donor)

    def list_donors(self):
        """ Creates a list of the donors by name """
        return f"\n{'-'*10} Donors {'-'*10}\n" + '\n'.join([donor.name for donor in self._donors])

    def print_donors(self):
        """ Prints the list of donors """
        print(self.list_donors())

    def find_donor(self, name):
        """
        Find a donor by name
        :param name: the name of the donor to search for
        :return: The donor if found else None
        """
        for donor in self._donors:
            if donor.name == name:
                return donor
        return None

    def add_donation(self, name, amount):
        """
        Add a donation.
        :param name: the name of the donor.
        :param amount: the amount of the donation.the
        :returns: the list of donations for the donor
        """
        donor = self.find_donor(name)
        if donor is None:
            donor = Donor(name)
            self.add_donor(donor)
        donor.add_donation(amount)
        print("\n" + donor.create_thank_you(amount))
        return donor

    def challenge(self, factor, min=None, max=None):
        """
        Runs challenge projections on all donor donations and returns the sum
        :param factor: scaling factor for donations
        :param min: minimum donation filter
        :param max: maximum donation filter
        """
        return sum(map(lambda donor: sum(donor.challenge(factor, min, max)), self._donors))

    def create_report(self):
        """
        Handles the create report menu selection
        :returns: returns the report string
        """
        header = "\n{:<20}| Total Given | Num Gifts | Average Gift\n".format("Donor Name")
        result = header
        result += f"{'-' * (len(header) - 1)}"
        donors_list = sorted(self._donors, reverse=True)
        for donor in donors_list:
            result += "\n{:<20}| ${:>10.2f} | {:>9} | ${:>11.2f}".format(donor.name, donor.total_donations, donor.num_donations, donor.avg_donation)
        return result

    def print_report(self):
        """ Prints the report """
        print(self.create_report())

    def mail_everyone(self):
        """ Handles the mail to everyone menu selection """
        for donor in self._donors:
            with open(donor.name.lower().replace(' ', "_") + ".txt", 'w') as f:
                f.write(donor.create_thank_you(donor.total_donations))


# define a starting set of donors
donors_array = [
Donor("Bill Ted", [353.53, 348.1, 25.00]),
Donor("Frank Fred", [120.50, 56.76, 1.50]),
Donor("Laura Todd", [5.75]),
Donor("Steve Lincoln", [75.38, 89.9]),
Donor("Lisa Grant", [175.50, 34.20])
]

# A global donors object for use in the user input methods
donors = Donors(donors_array)

def quit_menu():
    """ Handles the menu quit selection """
    return "Quit"

def donation_entry(name):
    """
    Handles the donation entry and prints the thank you to the screen.
    :param name: the name of the donor
    """
    amount = number_input("Enter donation amount or 'q' to return to the main menu: ", skip_value="q")
    if amount is None:
        return
    donors.add_donation(name, amount)

def donor_entry():
    """ Handles donor entry menu selection """
    name = input("\nEnter donor's full name or 'q' to return to the previous menu: ")
    if(name == "q"):
        return
    donation_entry(name)

def send_thank_you():
    """ Handles the send thank you menu selection """
    # modify donor entry slightly (no more list) to reuse display prompt funtion
    thank_you_menu_prompt = "1. Enter donation\n2. See a list of donors\n3. Return to previous menu"
    thank_you_menu_dict = {'1':donor_entry, '2':donors.print_donors, '3':quit_menu}
    display_prompt(thank_you_menu_prompt, thank_you_menu_dict)

def number_input(display_text, skip_value=None):
    """
    Request numeric input from the user and continue asking until a number or an optional skip value is entered
    :param display_test: input prompt text
    :param skip_value: optional skip entry value
    """
    input_value = input(display_text)

    if skip_value == input_value:
        return None
    try:
        return float(input_value)
    except ValueError:
        print("Please enter a valid number.")
        return number_input(display_text, skip_value)

def challenge_projections():
    """ Request challenge values and displays the result """
    min = number_input("\nEnter minimum donation amount or 'n' for no minimum: ", skip_value="n")
    max = number_input("Enter maximum donation amount or 'n' for no maximum: ", skip_value="n")
    factor = number_input("Enter donation challenge factor: ")
    print("\nTotal potential donations: ${:.2f}".format(donors.challenge(factor, min=min, max=max)))

def display_prompt(menu_prompt, menu_dict):
    """
    Handles the user input loop for a menu of options by displaying the menu prompt and dispatching
    to the appropriate method based on the user selection

    :param menu_prompt: the menu prompt
    :param menu_dict: the mapping of menu selections to functions
    """
    while True :
        print("\nChoose from the following menu of options:")
        print(menu_prompt)
        selection = input("\nPlease enter your choice: ")
        try:
            if menu_dict[selection]() == "Quit":
                break
        except KeyError:
            print("Invalid selection")

if __name__ == '__main__':
    main_menu_prompt = "1. Send a Thank You\n2. Create a Report\n3. Send letters to everyone\n4. Challenge Projections\n5. Quit"
    main_menu_dict = {'1':send_thank_you, '2':donors.print_report, '3':donors.mail_everyone, '4':challenge_projections, '5':quit_menu}
    display_prompt(main_menu_prompt, main_menu_dict)