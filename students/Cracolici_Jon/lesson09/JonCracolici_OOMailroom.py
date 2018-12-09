# Jon Cracolici
# Lesson 09 OO Mailroom
# UW Python Cert
# import statements
from collections import OrderedDict


class Donor:
    """This is the donor class, which holds info for individual donors.
    """
    def __init__(self, *args, name=None,):
        self._name = name.title()
        self._donations = [x for x in args]

    def new_don(self, new_donation):
        self._donations.append(new_donation)

    @property
    def name(self):
        return self._name

    @property
    def f_name(self):
        """File name."""
        f_name = self.name.replace(' ', '_')
        return f_name

    @property
    def donations(self):
        return self._donations

    def total_dons(self):
        total_dons = sum(self._donations)
        return total_dons

    def num_dons(self):
        num_dons = len(self._donations)
        return num_dons

    def last_don(self):
        last_don = self._donations[-1:]
        return last_don

    def avg_don(self):
        avg_don = sum(self._donations) / len(self._donations)
        return avg_don

    def note_gen(self, dest='s'):
        """Creates a thank you note. Includes a required positional argument of the intended recipient's info,
        and a kwarg "dest" that defaults to printing to screen but may be set to generate a file."""
        message = "Dear {}, \nThank you for your generous donation of ${:.02f}. Please rest assured" \
                  " that we will use at least \n95% of your contribution to feed the homeless to wolves." \
                  " We could not do this work without you. \nSincerely, \nThe Billionaires' Club".format(self._name,
                                                                                                        self.last_don())
        if dest == 's':
            print(message)
        elif dest == 'f':
            return message


class DataBase:
    """This is the database class that stores all the donor info together."""

    def __init__(self, db):
        """Initialize the database."""
        self.data = db

    def add_donor(self, other):
        """Adds a donor to the database"""
        self.data.append(other)

    def data_report(self):
        """Prints a summary data report about past donors to screen."""
        for i in self.data:
            print('{i.name():26}${i.total_dons:>13.2f}{i.num_dons:>12} ${i.avg_don:>12.2f}'.format(**i))

    def mass_mail(self):
        """Sends a thank you note to all past donors, prints them to file."""
        for donor in self.data:
            letter_name = donor.f_name + '.txt'
            with open(letter_name, 'w') as out_file:
                out_file.write(donor.note_gen(self, dest='f'))
                out_file.close()

    def update_donor(self, name=None, donation=None):
        """Updates a donor currently in the database."""
        for donor in self.data:
            if donor.name == name:
                donor.new_don(donation)

    def current_donors(self, *args):
        """Displays a list of current donors."""
        names = [item.name for item in self.data]
        last_name = names.pop(len(names) - 1)
        l = len(names)
        display = "The current donors are" + (l * " {},").format(*names) + " and {}.".format(last_name)
        print(display)
        return


# Functions that I want to keep outside of the classes.

def initialize_database():
    """This function intializes the database when called."""
    donor1 = Donor(20000,3000, name='William Gates, III')
    donor2 = Donor(100, 776.21, name='Mark Zuckerberg')
    donor3 = Donor(100, 253.43, name='Jeff Bezos')
    donor4 = Donor(100.95, name='Paul Allen')

    temp_db = [donor1, donor2, donor3, donor4]
    db = DataBase(temp_db)
    return db


# Functions relating to the start menu

def saty_control(db):
    """Creates the control flow for the send a thank you menu."""
    saty_menu_display()
    response1 = saty_user_input()
    try:
        return saty_menu_logic[response1](db)
    except KeyError:
        print("You have input an invalid instruction. Please enter 1, 2, 3, or 4")
        return


def start_menu_display():
    """Prints the start menu to the screen."""
    print('Welcome to our mailroom app!')
    print('Please select the number of your choice from the following options')
    print('1) Send a Thank You')
    print('2) Create a Report')
    print('3) Send Letters to Everyone')
    print('4) Quit')


def saty_menu_display():
    """Prints the send a thank you menu to the screen."""
    print('You have chosen to send a thank you note to a donor')
    print('Please select the number of you choice from the following options')
    print('1) See a list of current donors')
    print('2) Send a thank you to a current donor for a new gift')
    print('3) Send a thank you to a first time donor')
    print('4) Return to the start menu')


def start_user_input():
    """Collects user input. I separate this for easier error handling in future."""
    task = input('Please type the number of your selection.')
    return task


def saty_user_input():
    """Collects user input. I separate this for easier error handling in future."""
    task = input('Please type the number of your selection.')
    return task


def ud_name_handle(a, names, io='out'):
    """This function tests whether or not you selected the appropriate database operation by checking to see if
       the donor is already in the database. Whether or not that is a problem is handled by the io kwarg.
       args:
       a = string passed to function by the quit case handler
       dB = database of donors, a dict of dicts
       kwargs:
       io = in or out checker. Defaults to out. Out means that you should not already have the donor.
       In means you should have the donor. Will exit your task if the check is wrong."""
    # validioset = (['in', 'out'])

    if io == 'out':
        count = 0
        message = 'It appears that donor is already in our system.\n Perhaps you would like to select the Update' \
                  ' Donor option instead?'
    elif io == 'in':
        count = 1
        message = 'It appears that you are attempting to update a donor not already in our system.\n Perhaps you ' \
                  'would like to select the New Donor option instead?'
    if a == False:
        return False
    try:
        if a in names:
            x = 1
        else:
            x = 0
        if count == x:
            return a
        elif count != x:
            print(message)
            return False
    except:
        print('something is strangely wrong. break up')
        return False


def don_input():
    """This function collects money input about the donation."""
    return input('How much did they donate?')


def name_input():
    """This function collects name input about the donation."""
    return input('Who is the donor?')


def ud_don_handle(s):
    try:
        if s == False:
            return False
        else:
            donation = float(s)
            return donation
    except AttributeError:
        print('You have entered a non-numeric value in the donation prompt. Please use a number.')
        return False
    except ValueError:
        print('You have entered a non-numeric value in the donation prompt. Please use a number.')
        return False


def q_check(a):
    q_set = ['quit', 'q']
    try:
        if (a.lower() in q_set) is True:
            # print('did need to quit')
            return False
        else:
            # print('did not need to quit')
            return a
    except AttributeError:
        print('Something is wrong with the user input call.')
        return False


def nd_control(db):
    """Function that calls functions to create and add a new donor to database, print letter to screen."""
    current_names = [item.name for item in db.data]
    name = ud_name_handle(q_check(name_input()),current_names, io = 'out')
    if name == False:
        return False
    name = str(name)
    donation = ud_don_handle(q_check(don_input()))
    if donation == False:
        return False
    new_don = Donor(name=name, donation=donation)
    new_don.note_gen(dest='s')
    db.add_donor(new_don)
    return db


def ud_control(db):
    """Function that calls functions to update a donor in the database, print letter to screen."""
    current_names = [item.name for item in db.data]
    name = ud_name_handle(q_check(name_input()),current_names, io = 'in')
    if name == False:
        return False
    name = str(name)
    donation = ud_don_handle(q_check(don_input()))
    if donation == False:
        return False
    #will add try except to check for donor actually being new in L5
    db.update_donor(name=name, donation=donation)
    for donor in db.data:
        if donor.name == name:
            donor.note_gen(dest='s')
    return db


def quit_program(db):
    print("Goodbye dear User!")
    return False
    #sys.exit()


def quit_saty(db):
    print("Bye bye!")
    return False

def main_2(db):
    while True:
        x = saty_control(db)
        if x == False:
            break

# This is the beginning of the executed program.

if __name__ == "__main__":
    """Actual program."""
    # Initialize database
    db = initialize_database()

    # Set up the switch dicts
    start_menu_logic = {'1': main_2, '2': db.data_report, '3': db.mass_mail, '4': quit_program}
    saty_menu_logic = {'1': db.current_donors, '2': ud_control, '3': nd_control, '4': quit_saty}

    # Initialize database
    db = initialize_database()

    # Enter control flow
    while True:

        start_menu_display()
        response = start_user_input()
        try:
            start_menu_logic[response](db)
        except KeyError:
            print("You have input an invalid instruction. Please enter 1, 2, 3, or 4")


