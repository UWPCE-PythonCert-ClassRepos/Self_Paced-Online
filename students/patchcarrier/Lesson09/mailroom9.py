import sys
import os

class Donor:
    """Representation of a single donor.
    
    A Donor has a name and a record is kept for the previous donations made
    by the individual.
    """
    
    def __init__(self, name, donation_amount=None):
        """Create an instance of a Donor."""
        # Name of the donor
        self._name = name
        # Use a list to track the donation record of this particular donor
        self._donor_record = []
        if not (donation_amount is None):
            self.add_donation(donation_amount)
    
    @property
    def name(self):
        """The name of this donor."""
        return self._name
    
    def add_donation(self, donation_amount):
        """Add a donation of the specified amount to the record of this donor, 
        and send a thank you email."""
        self._donor_record.append(donation_amount)
        self.thankyou_email(donation_amount)
        
    @property
    def n_donations(self):
        """The number of donations made by this individual."""
        return len(self._donor_record)
    
    @property
    def sum_donations(self):
        """The total sum of donations made by this individual."""
        return sum(self._donor_record)
    
    def thankyou_email(self, amount):
        """Send a thank you email to donor for the specified amount."""
        body = ("\n\nThank you {name} for your generous donation of ${amount:.2f} to "
          "Vertical Generation.\n\nWe greatly appreciate your support for our cause."
          "\n\n-patchcarrier")
        print(body.format(name=self.name, amount=amount))        
    

class DonorDatabase:
    """Collection of individual Donor objects."""
    
    EMAIL_TEXT = """Dear {name},
        
Thank you for your continued support of Vertical Generation. 

Your {num_donations:d} donation{s_string1} totaling ${donation_sum:.2f} help{s_string2} us continue to share rock climbing
with the underserved youth in Seattle.

Sincerely,
-patchcarrier
""" 
    
    def __init__(self, initial_db=None):
        """Create an instance of a Donor Database.
        Inputs:
        initial_db- A dictionary of the form {"donor_name",[donation1_amount,
                    donation2_amount, ... donationN_amount]} to initialize the 
                    donor database with
        """
        # The donor database is represented as a dicitonary of (key,value)
        # pairs where key is the name of each donor and value is a Donor
        # instance
        self._donor_dict = {}
        
        if not (initial_db is None):
            # Initialize this database with existing donor information specified
            # by initial_db
            stdout_orig = sys.stdout
            with open(os.devnull,'w') as output:
                sys.stdout = output
                for name_i in initial_db:
                    for donation_i in initial_db[name_i]:
                        self.add_donation(name_i, donation_i)
            sys.stdout = stdout_orig
            
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

class Menu:
    """A menu object represents a given prompt that a user will see.
    
    A menu has a prompt and a reference to the same DonorDatabase object
    as the InteractiveSession instance to which a Menu object belongs. 
    
    It also has a dispatch dictionary which maps user inputs to their corresponding
    methods. The following convention is expected for the return value of methods
    in the dispatch dictionary of a Menu object:
        
        -methods which add a new Menu to the Menu stack of the InteractiveSession
        instance should return the class object of the menu they wish to add
        
        -all other methods (e.g. ones that print to the screen or modify
        the DonorDatabase instance) should return None
    """
    
    def __init__(self, session):
        """Create a menu object.
        
        Inputs:
        session- The instance of an InteractiveSession to which this Menu instance
                 belongs
        """
        # A dispatch dictionary that maps user input characters to their 
        # corresponding functions
        self._dispatch_dict = {'q':Menu._quit}
        # Reference to the InteractiveSession instance's DonorDatabase instance
        self._donor_db = session._donor_db
    
    def prompt_user(self):
        """Get input from the user and attempt to execute the method corresponding
        to their input."""
        # Get user input and return the value (to the InteractiveSession instance)
        user_input = input(self._prompt)
        try:
            return self._dispatch_dict[user_input](self)
        except KeyError:
            print("\nInput character '{}' not recognized".format(user_input))
            return None 
        
    def _quit(self):
        """Tell the InteractiveSession instance to remove the current Menu from 
        the stack. All instances of Menu of a Menu subclass have this method in 
        the dispatch dictinoary."""
        return 'q'
 
    
class MainMenu(Menu):
    """Class representing the main menu screen."""
    
    _prompt = """\nMain Menu
Enter:
(t) to send a thank you letter
(c) to create a report
(s) to send letters to everyone
(q) to quit
>>> """
        
    def __init__(self, session):
        Menu.__init__(self, session)
        self._dispatch_dict = dict(self._dispatch_dict,
                                   t=MainMenu._enter_thankyou_menu,
                                   c=MainMenu._create_report,
                                   s=MainMenu._send_letters_everyone)
    
    def _enter_thankyou_menu(self):
        return ThankYouMenu
    
    def _create_report(self):
        self._donor_db.write_report()
    
    def _send_letters_everyone(self):
        self._donor_db.send_letters()
         
        
class ThankYouMenu(Menu):
    """Class representing the donation entry menu."""
    
    _prompt = """\nSpecify Donation Menu
Enter:
(l) to list the names of previous donors
(e) to create a new donation entry and send a thank you email
(q) to quit and return to the main menu
>>> """
    
    def __init__(self, session):
        Menu.__init__(self, session)
        self._dispatch_dict = dict(self._dispatch_dict,
                                   l=ThankYouMenu._list_donors,
                                   e=ThankYouMenu._create_entry)
        
    def _list_donors(self):
        self._donor_db.list_donors()
    
    def _create_entry(self):
        
        name_in = input("\nEnter the full name of the donor (or 'q' to quit)"
                        "\n>>>")
        if name_in == 'q': return Menu._quit(self)
        amount_in = input("\nEnter the donation amount (or 'q' to quit)"
                  "\nEnter numbers only, do not enter special characters"
                  "\n>>> ")
        if amount_in == 'q': return Menu._quit(self)
        
        while True:
            try:
                amount_in = float(amount_in)
                break
            except ValueError:
                print('Error: Input must be numeric')
                amount_in = input("\nEnter the donation amount (or 'q' to quit)"
                          "\nEnter numbers only, do not enter special characters"
                          "\n>>> ")
                if amount_in == 'q': return Menu._quit(self)
        
        self._donor_db.add_donation(name_in, amount_in)
        
        
class InteractiveSession:
    
    def __init__(self, initial_menutype, donor_db=None):
        """Initialize a user-interactive session object.
        
        Inputs:
        initial_menu - Menu class object for the first menu screen seen by the user
        donor_db - A dictionary of the form {"donor_name",[donation1_amount,
                   donation2_amount, ... donationN_amount]} to initialize the 
                   donor database with
        """
        # The DonorDatabase constructor handles the case when donor_db is none.
        # If an initial database is specified, the contents are copied.
        self._donor_db = DonorDatabase(donor_db)
        # self._menu_stack is a stack of Menu objects
        self._menu_stack = [initial_menutype(self)]

        
    def run_session(self):
        """Start and run a user interactive session."""
        # While there are still Menu objects in the menu stack
        while len(self._menu_stack) > 0:
            # If the Menu.prompt_user() function returns a class object,
            # it is a new Menu object that should be added to the Menu stack
            return_val = self._menu_stack[-1].prompt_user()
            try:
                self._menu_stack.append(return_val(self))
            # If the return value is not callable, catch the TypeError. If the
            # return value is 'q', remove the current Menu from the stack.
            except TypeError:
                if return_val == 'q': self._menu_stack.pop()

            # If the return value is anything other than a Menu object of the 
            # character 'q', the loop continues and the user is re-prompted for input

                
if __name__ == "__main__":
    # Start a user-interactive session with an existing "database" of donors
    donors = {"Conrad Anker":[550, 1200, 0.02], 
          "Tommy Caldwell":[600.50, 80], 
          "Margo Hayes":[200, 550.50], 
          "Alex Honnold":[0.01],
          "Paige Claassen":[750, 800, 150.25]}
    session = InteractiveSession(MainMenu, donors)
    session.run_session()       
            