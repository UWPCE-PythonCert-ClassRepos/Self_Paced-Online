"""donation organization congroller

Expected to have one controller created for each non-profit organization.
This controller contains information about organization and manages creation
and management of donations"""

from Donor import Donor


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
        return sum([k.donation_total() for i, k in self.donors.items()])

    def create_donation(self, donor, amount):
        """creates donation in input donor"""

        if self.find_donor(donor) is None:
            raise IndexError('Donor does not exist')
        self.find_donor(donor).add_donation(amount)

    def send_thank_you_letters(self):
        """process to evaluate all donors and create letter to send to
        donors."""
        # TODO: need to fix this as this is jsut copy and paste from mailroom
        # iterate through donors and donations to send thank yous
        for donor in donors:
            file_name = "".join([donor.replace(" ", "_").lower(), '.txt'])
            full_path = thank_you_directory / file_name
            print(file_name)
            donor_info = summarize_donor(donor, donors)
            thank_you_text = create_donation_thank_you(fullname=donor,
                                                    amount=donor_info[1])
            try:
                with open(full_path, 'w') as f:
                    f.write(thank_you_text)
            except FileNotFoundError:
                print('Mailroom thank you directory not found.  Please create this directory first.')
                break
            else:
                print(f'Thank you letter for {donor} created in "{thank_you_directory}"')

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

        

        
