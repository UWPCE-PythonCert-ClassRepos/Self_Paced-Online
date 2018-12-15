import mailroom4 as mr
import sys
import io
import random

def donor_entry_help(name, amount):
    """Add the donor with the specified name and donation amount to the global
    dictionary using the mr.enter_donor() function."""
    
    # The enter_donor() function expects two inputs from stdin
    cmds = f"{name}  {amount}".replace("  ", "\n")
    sys.stdin = io.StringIO(cmds)
    mr.enter_donor()


def test_donor_entry_1():
    "Test adding a donation to an existing donor."
    
    # loop through each existing donor and add a new random ammount
    for donor in mr.donors:
        n_donations = len(mr.donors[donor])
        donation_amount = random.uniform(0,100)
        donor_entry_help(donor,donation_amount)
        
        # Check that the previous donations are still recorded in the global 
        # dictionary, and that the new donation got recorded
        assert len(mr.donors[donor]) == n_donations + 1
        # Check that the correct donation ammount got added to the global dictionary
        assert mr.donors[donor][-1] == donation_amount
    
    
def test_donor_entry_2():
    "Test adding a donation amount for a new donor."
    pyt)
    new_names = ("Patrick Carrier", "Jim Harbaugh", "Kelly Johnson")
    
    for name in new_names:
        donation_amount = random.uniform(0,100)
        donor_entry_help(name, donation_amount)
        
        # Ensure that each new donor only has one donation recorded and 
        # that the correct value got recorded in the global dictionary
        assert len(mr.donors.get(name)) == 1
        assert mr.donors.get(name)[-1] == donation_amount
    

def test_donor_entry_3():
    "Test non-numerical input for donation amount being handled."
    
    try:
        # Attempt to add the non-numerical donation amount 'money'
        donor_entry_help("Pablo Picasso", 'money')
    except ValueError:
        # mailroom.py should handle the ValueError if a bad (non-numerical) input is given
        assert 0
    except EOFError:
        # mailroom.py should continue prompting the user for a numerical input
        # so the above function call should raise an EOFError since we only
        # provide the one value: 'money'
        pass
        
    
def test_donor_entry_4():
    "Test premature exit after donor name prompt"
    #no chage to dict and nothing sent to stdout
    pass


def test_donor_entry_5():
    "Test premature exit after donoation amount prompt"
   #no change to dict and nothing send to stdout
    pass


def test_list_donors():
    "Verify that all of the donor names are printed to stdout"
    
    # Re-direct output to the terminal to the StringIO object output
    output = io.StringIO()
    sys.stdout = output
    mr.list_donors()
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # change the position to the begginning of the stream:
    output.seek(0)  
    # Read all of the names output by the list_donors() function into a set
    names_out = {name for name in output}

    # Loop through the donors in the global dictionary and verify that all
    # names are in the names_out set
    for donor in mr.donors:
        assert donor in names_out
    
    
def test_letters():
    "Test of the send_letters function"
    # check that a file exists for each donor (remove all *.txt files before)
    # check that the number of donations and total amount donated are correct
    # for each donor
    
def test_report():
    "Test that the information in the printed table is correct"
 