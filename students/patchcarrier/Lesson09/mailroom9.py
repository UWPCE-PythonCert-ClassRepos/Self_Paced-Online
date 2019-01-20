import copy

class Donor:
    
    def __init__(self, name, donation_amount=None):
        """Create an instance of a Donor.
        
        A Donor has a name and a record is kept for the previous donations made
        by the individual.
        """
        self._name = name
        self._donor_record = []
        if not (donation_amount is None):
            self.add_donation(donation_amount)
    
    @property
    def name(self):
        return self._name
    
    def add_donation(self, donation_amount):
        """Add a donation of the specified amount to the record of this donor, 
        and send a thank you email."""
        self._donor_record.append(donation_amount)
        self.thankyou_email(donation_amount)
        
    @property
    def n_donations(self):
        return len(self._donor_record)
    
    @property
    def sum_donations(self):
        return sum(self._donor_record)
    
    def thankyou_email(self, amount):
        """Send a thank you email to donor for the specified amount."""
        
        body = ("\n\nThank you {name} for your generous donation of ${amount:.2f} to "
          "Vertical Generation.\n\nWe greatly appreciate your support for our cause."
          "\n\n-patchcarrier")
        print(body.format(name=self.name, amount=amount))        
    

class DonorDatabase:
    
    EMAIL_TEXT = """Dear {name},
        
Thank you for your continued support of Vertical Generation. 

Your {num_donations:d} donation{s_string1} totaling ${donation_sum:.2f} help{s_string2} us continue to share rock climbing
with the underserved youth in Seattle.

Sincerely,
-patchcarrier
""" 
    
    def __init__(self, initial_db=None):
        
        self._donor_dict = {}
        if not (initial_db is None):
            # Make this another DonorDatabase instance rather than a dictionary
            #self._donor_dict = copy.deepcopy(initial_db)
            for name_i in initial_db:
                for donation_i in initial_db[name_i]:
                    self.add_donation(name_i, donation_i)
           
            
    def list_donors(self):
        """List all of the donors in the donor database."""
        print()
        for donor_i in self._donor_dict:
            print(donor_i)       
    
    
    def add_donation(self, name, amount):
        """Add the specified ammount to the donation record of the donor with 
        the specified name."""
        if name in self._donor_dict:
            self._donor_dict[name].add_donation(amount)
        else:
            self._donor_dict[name] = Donor(name, amount)
    
    
    def write_report(self):
        """Print a tabulated summary of all donors and donations in the 
        database to the screen."""
        # Header
        print("\n{:<25s}|{:^13s}|{:^11s}|{:^14s}".format("Donor Name", 
              "Total Given","Num Gifts","Average Gift"))
        print("-" * (25 + 13 + 11 + 14 + 3))
        fstring = "{:<25s} ${:>12.2f} {:>11d} ${:>13.2f}"
        
        # Sort the global data structure by donation amount
        donor_names = list(self._donor_dict.keys())
        donor_names.sort(reverse=True, 
                         key=lambda name_i: self._donor_dict[name_i].sum_donations)
        
        # Print the summary of donation data
        for name_i in donor_names:
            total_given = self._donor_dict[name_i].sum_donations
            n_gifts = self._donor_dict[name_i].n_donations
            print(fstring.format(name_i, total_given, n_gifts, total_given/n_gifts))
    
    
    def send_letters(self):
        """Send thank you letters to all of the donors in the database personalized
        with the number of donations they've made and the total amount given."""

        for name_i, donor_i in self._donor_dict.items():
            filename_i = name_i + '.txt'
            filename_i = filename_i.replace(' ','_')
            
            with open(filename_i,'w') as outfile:
                #check the number of donations for the current donor, if it's only
                #one, donations should not be plural
                if donor_i.n_donations > 1:
                    s_string1 = 's'
                    s_string2 = ''
                else:
                    s_string1 = ''
                    s_string2 = 's'               
                    
                outfile.write(self.EMAIL_TEXT.format(name=name_i,
                                                num_donations=donor_i.n_donations,
                                                s_string1=s_string1,
                                                s_string2=s_string2,
                                                donation_sum=donor_i.sum_donations))
