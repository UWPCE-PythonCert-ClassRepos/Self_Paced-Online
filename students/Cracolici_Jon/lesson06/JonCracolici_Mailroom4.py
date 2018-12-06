# Jon Cracolici
# Lesson 06 Mailroom 4
# UW Python Cert
# import statements
from collections import OrderedDict


# database set up
def initialize_database():
    """This function intializes the database when called."""
    william_gates_iii = {'f_name': 'William_Gates_III', 'donor': 'William Gates, III', 'total_donated': 653784.49,
                         'num_donations': 2, 'avg_donated': 326892.24, 'last_donation': 30000.00}
    mark_zuckerberg = {'f_name': 'Mark_Zuckerberg', 'donor': 'Mark Zuckerberg', 'total_donated': 16396.10,
                       'num_donations': 3, 'avg_donated': 5465.37, 'last_donation': 5000.25}
    jeff_bezos = {'f_name': 'Jeff_Bezos', 'donor': 'Jeff Bezos', 'total_donated': 877.33, 'num_donations': 1,
                  'avg_donated': 877.33, 'last_donation': 877.33}
    paul_allen = {'f_name': 'Paul_Allen', 'donor': 'Paul Allen', 'total_donated': 708.42, 'num_donations': 3,
                  'avg_donated': 236.14, 'last_donation': 100.95}

    dB = {'william_gates_iii': william_gates_iii, 'mark_zuckerberg': mark_zuckerberg, 'jeff_bezos': jeff_bezos,
          'paul_allen': paul_allen}
    return dB


# Functions relating to the start menu
def start_control(dB):
    """Creates the control flow for the start menu."""
    start_menu_display()
    response = start_user_input()
    try:
        return start_menu_logic[response](dB)
    except KeyError:
        print("You have input an invalid instruction. Please enter 1, 2, 3, or 4")
        return


def saty_control(dB):
    """Creates the control flow for the send a thank you menu."""
    saty_menu_display()
    response = saty_user_input()
    try:
        return saty_menu_logic[response](dB)
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


def new_donor(new_donor_dict, dB):
    """Creates a new donor in the database and requests donation ammount."""
    up_dict = {new_donor_dict['donor_name_key']: {'f_name': new_donor_dict['donor_name_key'].title(),
                                                  'donor': new_donor_dict['donor'],
                                                  'total_donated': new_donor_dict['donation'], 'num_donations': 1,
                                                  'avg_donated': new_donor_dict['donation'],
                                                  'last_donation': new_donor_dict['donation']}}
    dB.update(up_dict)
    return dB


def update_donor(new_don_dict, dB):
    """Updates an existing donor in the database with a new donation."""
    dB[new_don_dict['donor_name_key']]['total_donated'] += new_don_dict['donation']
    dB[new_don_dict['donor_name_key']]['num_donations'] += 1
    dB[new_don_dict['donor_name_key']]['avg_donated'] = dB[new_don_dict['donor_name_key']]['total_donated'] / \
                                                        dB[new_don_dict['donor_name_key']]['num_donations']
    dB[new_don_dict['donor_name_key']]['last_donation'] = new_don_dict['donation']
    return dB


def show_current_names(dB):
    """Displays the names of all previous donors."""
    names = [item['donor'] for item in dB.values()]
    # for item in dB.values():
    #    names.append(item['donor'])
    last_name = names.pop(len(names) - 1)
    l = len(names)
    display = "The current donors are" + (l * " {},").format(*names) + " and {}.".format(last_name)
    print(display)
    return  # Returns you to the send a thank you menu
    # return display #, saty_control(dB)


def create_report(dB):
    """Creates a summary report for all current donors."""
    dict_list = OrderedDict(sorted(dB.items(), key=lambda x: x[1]['total_donated'], reverse=True))
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    for i in dict_list:
        print('{donor:26}${total_donated:>13.2f}{num_donations:>12} ${avg_donated:>12.2f}'.format(**dB[i]))
    return


def mass_mail(dB):
    for item in dB.values():
        print_letters(item)
    return start_control(dB)


def ud_name_handle(a, dB, io='out'):
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
        x = [a.title() in dB[key].values() for key in dB.keys()].count(True)
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


def nd_control(dB):
    """Function that calls functions to create and add a new donor to database, print letter to screen."""
    name = ud_name_handle(q_check(name_input()),dB, io = 'out')
    if name == False:
        return False
    name = str(name)
    donation = ud_don_handle(q_check(don_input()))
    if donation == False:
        return False
    donor_name_key = name.lower()
    donor_name_key = donor_name_key.replace(' ', '_')
    donor = name.title()
    new_donor_dict = {'donor_name_key': donor_name_key, 'donor': donor, 'donation': donation}
    #will add try except to check for donor actually being new in L5
    new_donor(new_donor_dict, dB)
    note_gen(dB[new_donor_dict['donor_name_key']])
    return dB


def ud_control(dB):
    """Function that calls functions to update a donor in the database, print letter to screen."""
    name = ud_name_handle(q_check(name_input()),dB, io = 'in')
    if name == False:
        return False
    name = str(name)
    donation = ud_don_handle(q_check(don_input()))
    if donation == False:
        return False
    #will add try except to check for donor actually being new in L5
    donor_name_key = name.lower()
    donor_name_key = donor_name_key.replace(' ', '_')
    donor = name.title()
    up_donor_dict = {'donor_name_key': donor_name_key, 'donor': donor, 'donation': donation}
    update_donor(up_donor_dict, dB)
    note_gen(dB[up_donor_dict['donor_name_key']])
    return dB


def print_letters(donor_dict):
    """This function takes a string and makes a document with it."""
    letter_name = donor_dict['f_name']+'.txt'
    with open(letter_name, 'w') as out_file:
        out_file.write(note_gen(donor_dict, dest='f'))
        out_file.close()


def note_gen(person_dict, dest = 's'):
    """Creates a thank you note. Includes a required positional argument of the intended recipient's info,
    and a kwarg "dest" that defaults to printing to screen but may be set to generate a file."""
    message = "Dear {donor}, \nThank you for your generous donation of ${last_donation:.02f}. Please rest assured" \
              " that we will use at least \n95% of your contribution to feed the homeless to wolves. We could not do " \
              "this work without you. \nSincerely, \nThe Billionaires' Club".format(**person_dict)
    if dest == 's':
        print(message)
    elif dest == 'f':
        return message


def quit_program(db):
    print("Goodbye dear User!")
    return False
    #sys.exit()


def quit_saty(db):
    print("Bye bye!")
    return False


# This is the beginning of the executed program.

if __name__ == "__main__":
    start_menu_logic = {'1': main_2, '2': create_report, '3': mass_mail, '4': quit_program}
    saty_menu_logic = {'1': show_current_names, '2': ud_control, '3': nd_control, '4': quit_saty}
    main()