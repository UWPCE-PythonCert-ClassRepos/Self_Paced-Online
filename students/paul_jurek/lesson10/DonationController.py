"""donation organization congroller

Expected to have one controller created for each non-profit organization.
This controller contains information about organization and manages creation
and management of donations"""

import copy
from pathlib import Path
import pickle
from Donor import Donor, Donation


class DonationController:
    """organization controller for donations"""

    def __init__(self, name: str):
        """args:
            name : organzational name
            """
        self.name = name
        self.donors = {}

    def find_donor(self, donor: Donor):
        """searches through donor list and returns donor
        returns none if not found.  Setup to first check for donor id
        if this fails, assumes integer and will check for that"""
        # TODO: refactor and add int method to donor to allow int(donor)
            # to return same as donor.id
        try:
            return self.donors.get(donor.id)
        except AttributeError:
            return self.donors.get(int(donor))

    def create_donor(self, donor):
        """creates donor"""
        if self.find_donor(donor):
            raise KeyError('donor already exists')
        if isinstance(donor,Donor):
            try:
                self.donors[donor.id] = donor
            except AttributeError:
                raise AttributeError('Donor object needs id')
    
    def build_donor_from_name(self, firstname, lastname):
        """interface to build donor from just name and automatically assign id"""
        self.create_donor(Donor(id=self.next_id, firstname=firstname, lastname=lastname))

    def get_total_donations(self):
        """returns total donations in controller"""
        return sum([k.donation_total() for i, k in self.donors.items() if k.donations])

    def create_donation(self, donor, amount):
        """creates donation in input donor"""

        if self.find_donor(donor) is None:
            raise IndexError('Donor does not exist')
        self.find_donor(donor).add_donation(amount)

    @property
    def next_id(self):
        """returns the next avaliable int id from list
        used to asign donor ids"""
        donor_id_list = {i for i in self.donors}
        if self.donors:
            max_id = max(donor_id_list)
        else:
            max_id = 1
        
        # create range of ints
        non_used_ids = set(range(1,max_id+1)) - donor_id_list
        if non_used_ids:
            return min(non_used_ids)
        else:
            return max_id + 1

    def display_donors(self):
        """displays a list of donors in printed format"""
        donor_list = [":".join([str(donor_id), donor.fullname]) for donor_id, donor in self.donors.items()]
        print("\n".join(donor_list))

    def donor_report(self):
        """handles process for main screens report selection

        If the user (you) selected “Create a Report”, print a list of your donors,
        sorted by total historical donation amount.
        Include Donor Name, total donated, number of donations and average
        donation amount as values in each row. You do not need to print out all
        their donations, just the summary info.
        Using string formatting, format the output rows as nicely as possible.
        The end result should be tabular (values in each column should align
        with those above and below)
        After printing this report, return to the original prompt.
        At any point, the user should be able to quit their current task and
        return to the original prompt.
        From the original prompt, the user should be able to quit the script
        cleanly.
        Your report should look something like this:
        Donor Name                | Total Given | Num Gifts | Average Gift
        ------------------------------------------------------------------
        William Gates, III         $  653784.49           2  $   326892.24
        Mark Zuckerberg            $   16396.10           3  $     5465.37
        Jeff Bezos                 $     877.33           1  $      877.33
        Paul Allen                 $     708.42           3  $      236.14
        """
        print(f"{'Donor Name':<26}|{'Total Given':^15}|"
            f"{'Num Gifts':^11}|{'Average Gift':^15}")
        print('-'*70)
        donor_stats = [donor.summarize_donor() for id, donor in self.donors.items()]
        donor_stats.sort(key=lambda tup: tup[2], reverse=True)
        for summary in donor_stats:
            print(f"{summary[1]:<26} ${summary[2]:>13.2f}  "
                f"{summary[3]:>10}  ${summary[4]:>14.2f}")

    def send_letters_to_everyone(self, 
                                 thank_you_directory=Path('/mailroom_thankyou_letters')):
        """creates thank yous for all donors and sends out"""
        # iterate through donors and donations to send thank yous
        for id, donor in self.donors.items():
            file_name = "".join([str(id), '.txt'])
            full_path = thank_you_directory / file_name
            donor_info = donor.summarize_donor()
            thank_you_text = self.create_donation_thank_you(donor=donor, amount=donor_info[2])
            try:
                print(full_path)
                with open(full_path, 'w') as f:
                    f.write(thank_you_text)
            except FileNotFoundError:
                print('Mailroom thank you directory not found.  Please create this directory first.')
                break
            else:
                print(f'Thank you letter for {id} created in "{thank_you_directory}"')

    def create_donation_thank_you(self, donor, amount):
        """prints thank you message to terminal for donation"""
        return f"""Dear {donor.fullname},

            Thank you for your very kind donation of ${amount:.2f}.

            It will be put to very good use.

                        Sincerely,
                            -The Team"""

    def challenge(self, factor, min_donation=0, max_donation=1e9):
        """increases donations due to nice donor
        returns copy of donation controller with multiplied input"""

        if factor < 1:
            raise ValueError('Donors are not allowed to take $ from our cause.  Please consider factor of 10 ;)')
        # copy generated to avoid messing with old database
        new_db = copy.deepcopy(self)
        mod_func = modifying_fun_generator(factor)
        mod_filter = filter_fun_generator(min_donation=min_donation, max_donation=max_donation)
        # seperate list made to simplify code as we need to regenerate dict
        donor_list = map(mod_func, filter(mod_filter, new_db.donors.values()))
        # rebuilds donors dict
        new_db.donors = {i.id:i for i in donor_list}        
        return new_db

def modify_donor_donations(factor, donor):
    """returns a modified donor with their donations matched by nice donor"""
    new_donations = [Donation(amount=i.amount*factor, date=i.date, id=i.id) for i in donor.donations]
    donor._donations = new_donations
    return donor

def modifying_fun_generator(factor):
    """returns function with factor applied.  This increases donation amount  by factor"""
    return lambda x: modify_donor_donations(factor=factor, donor=x)

def filter_donor_donations(donor, min_donation=0, max_donation = 1.0e9):
    """filters donor donations to just those meeting criteria"""
    filtered_donations = [Donation(amount=i.amount, date=i.date, id=i.id) for i in donor.donations if (i.amount>=min_donation and i.amount <= max_donation) ]
    donor._donations = filtered_donations
    return donor

def filter_fun_generator(min_donation=0, max_donation=1.0e9):
    """returns function with factor applied.  This increases donation amount  by factor"""
    return lambda x: filter_donor_donations(min_donation=min_donation, max_donation=max_donation, donor=x)


def load_donation_controller(database):
    """loads database controller"""
    return pickle.load(open(database, "rb"))

def save_donation_controller(controller, database):
    """save database controller"""
    pickle.dump(controller, open(database, 'wb'))

def multiply_donation(original, factor):
    """returns multiplied donation"""
    return orginal * factor