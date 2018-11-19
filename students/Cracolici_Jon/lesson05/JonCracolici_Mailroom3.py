#Jon Cracolici
#Lesson 05 Mailroom 3
#UW Python Cert
#import statements
from collections import OrderedDict
#database set up
def initialize_database():
    """This function intializes the database when called."""
    william_gates_iii = {'fname': 'William_Gates_III', 'donor': 'William Gates, III', 'totaldonated': 653784.49, 'numdonations': 2, 'avgdonated': 326892.24, 'lastdonation': 30000.00}
    mark_zuckerberg = {'fname': 'Mark_Zuckerberg', 'donor': 'Mark Zuckerberg', 'totaldonated': 16396.10 , 'numdonations': 3, 'avgdonated': 5465.37, 'lastdonation': 5000.25}
    jeff_bezos = {'fname': 'Jeff_Bezos', 'donor': 'Jeff Bezos', 'totaldonated': 877.33, 'numdonations': 1, 'avgdonated': 877.33, 'lastdonation': 877.33}
    paul_allen = {'fname': 'Paul_Allen', 'donor': 'Paul Allen', 'totaldonated': 708.42, 'numdonations': 3, 'avgdonated': 236.14, 'lastdonation': 100.95}
    
    dB = {'william_gates_iii': william_gates_iii,'mark_zuckerberg': mark_zuckerberg,'jeff_bezos': jeff_bezos, 'paul_allen': paul_allen}
    return dB
#Functions relating to the start menu
def start_control(dB):
    """Creates the control flow for the start menu."""
    start_menu_display()
    response = start_user_input()
    try:
        return startmenulogic[response](dB)
    except KeyError:
        print("You have input an invalid instruction. Please enter 1, 2, 3, or 4")
        return
def saty_control(dB):
    """Creates the control flow for the send a thank you menu."""
    saty_menu_display()
    response = saty_user_input()
    try:
        return satymenulogic[response](dB)
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
def new_donor(newdonordict, dB):
    """Creates a new donor in the database and requests donation ammount."""
    updict = {newdonordict['donornamekey']:{'fname':newdonordict['donornamekey'].title(), 'donor': newdonordict['donor'], 'totaldonated': newdonordict['donation'], 'numdonations': 1, 'avgdonated': newdonordict['donation'], 'lastdonation': newdonordict['donation']}}
    dB.update(updict)
    return dB
def update_donor(newdondict, dB):
    """Updates an existing donor in the database with a new donation."""
    dB[newdondict['donornamekey']]['totaldonated'] += newdondict['donation']
    dB[newdondict['donornamekey']]['numdonations']+=1
    dB[newdondict['donornamekey']]['avgdonated'] = dB[newdondict['donornamekey']]['totaldonated']/dB[newdondict['donornamekey']]['numdonations']
    dB[newdondict['donornamekey']]['lastdonation'] = newdondict['donation']
    return dB
def show_current_names(dB):
    """Displays the names of all previous donors."""
    names = [item['donor'] for item in dB.values()]
    #for item in dB.values():
    #    names.append(item['donor'])
    lastname = names.pop(len(names)-1)
    l = len(names)
    display = "The current donors are"+(l*" {},").format(*names)+" and {}.".format(lastname)
    print(display)
    return #Returns you to the send a thank you menu
    #return display #, saty_control(dB)

def create_report(dB):
    """Creates a summary report for all current donors."""
    dictlist = OrderedDict(sorted(dB.items(), key=lambda x: x[1]['totaldonated'], reverse=True))
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    for i in dictlist:
        print('{donor:26}${totaldonated:>13.2f}{numdonations:>12} ${avgdonated:>12.2f}'.format(**dB[i]))
    return
def mass_mail(dB):
    for item in dB.values():
        print_letters(item)
    return start_control(dB)
def nd_control(dB):
    """Function that calls functions to create and add a new donor to database, print letter to screen."""
    newdonordict = donor_input(dB)
    if newdonordict == False:
        return False
    elif newdonordict['donornamekey'] in dB.keys():
        print("It appears that donor is already in our system.\n Perhaps you would like to select the 'Update Donor' option instead?")
        return False
    #will add try except to check for donor actually being new in L5
    new_donor(newdonordict, dB)
    note_gen(dB[newdonordict['donornamekey']])
    return dB#, start_control(dB)
def ud_control(dB):
    """Function that calls functions to update a donor in the database, print letter to screen."""
    updonordict = donor_input(dB)
    if updonordict == False:
        return False
    elif updonordict['donornamekey'] not in dB.keys():
        print("It appears that you are attempting t update a donor not already in our system.\n Perhaps you would like to select the 'New Donor' option instead?")
        return False
    #will add try except to check for donor actually being new in L5
    update_donor(updonordict, dB)
    note_gen(dB[updonordict['donornamekey']])
    return dB#, start_control(dB)
def donor_input(dB):
    """This function collects user input about the donation."""
    #create a set of quit criteria
    quitset = set(['quit', 'q'])
    donorname = input('Who is the donor?')
    #Check if user wants to exit to previous menu
    if donorname.lower() in quitset:
        return False
    newdonation = input('How much did they donate?')
    #Check if user wants to exit to previous menu
    if newdonation.lower() in quitset:
        return False
        
    else:#this section creates the keys and values for the outputted dict
        donornamekey = donorname.lower()
        donornamekey = donornamekey.replace(' ', '_')
        donor = donorname.title()
        try:
            donation = float(newdonation)
        except ValueError:
            print("Use numbers for the donation amount. NUMBERS!")
            return False
        newdondict = {'donornamekey': donornamekey, 'donor': donor, 'donation': donation}
        return newdondict
def print_letters(donordict):
    """This function takes a string and makes a document with it."""
    lettername = donordict['fname']+'.txt'
    outfile = open(lettername, 'w')
    outfile.write(note_gen(donordict, dest = 'f'))
    outfile.close()
def note_gen(persondict, dest = 's'):
    """Creates a thank you note. Includes a required positional argument of the intended recipient's info,
    and a kwarg "dest" that defaults to printing to screen but may be set to generate a file."""
    message = "Dear {donor}, \nThank you for your generous donation of ${lastdonation:.02f}. Please rest assured that we will use at least \n95% of your contribution to feed the homeless to wolves. We could not do this work without you. \nSincerely, \nThe Billionaires' Club".format(**persondict)
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
def main():
    db = initialize_database()
    while True:
        x = start_control(db)
        if x == False:
            break
def main_2(db):
    while True:
        x = saty_control(db)
        if x == False:
            break
#### This is the beginning of the executed program.
if __name__=="__main__":

    startmenulogic = {'1': main_2, '2': create_report, '3': mass_mail, '4': quit_program}
    satymenulogic = {'1': show_current_names, '2': ud_control, '3': nd_control, '4': quit_saty}
    main()