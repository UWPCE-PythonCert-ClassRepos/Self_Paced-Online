import mailroom4 as mr
import sys
import io
import random
import subprocess
import glob
import os

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
    except EOFError:
        # mailroom.py should continue prompting the user for a numerical input
        # so the above function call should raise an EOFError since we only
        # provide the one value: 'money'
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
    # don't include the newline character when reading in the names
    names_out = {name[:-1] for name in output if len(name[:-1]) > 0}

    # Loop through the donors in the global dictionary and verify that all
    # names are in the names_out set
    for donor in mr.donors:
        assert donor in names_out
    
    
def test_letters():
    """Test the send_letters() function to make sure a file containing an email
    exists. Also make sure the name, number of donations, and sum of donation 
    amounts is correct."""
    
    # Remove all text files
    subprocess.run('del *.txt',shell=True)
    mr.send_letters()
    
    for donor in mr.donors:
        
        # Check that a file with the email contents exists for each donor
        fname = donor.replace(' ','_') + '.txt'
        assert len(glob.glob(fname)) == 1
        
        # Read through the letter, and make sure the name, number of donations,
        # and total sum of donations is correct
        with open(fname,'r') as infile:
            for line in infile:
                # Check name
                if line.startswith('Dear'):
                    letter_name = line[len('Dear') : line.find(',')]
                    letter_name = letter_name.replace(' ','')
                    actual_name = donor.replace(' ','')
                    assert letter_name == actual_name
                    
                if line.startswith('Your'):
                    # Check number of donations    
                    n_donations = line[len('Your') : line.find('donation')]
                    n_donations = int(n_donations.replace(' ',''))
                    assert n_donations == len(mr.donors[donor])
                    
                    # Check the sum of donation amounts
                    d_sum = line[line.find('$') + 1 : line.find('help')]
                    d_sum = float(d_sum.replace(' ',''))
                    assert d_sum == round(sum(mr.donors[donor]),2)
        
    subprocess.run('del *.txt',shell=True)              
        
    
def test_report():
    "Test that the information in the printed table is correct"
 
    # Get the output from the write_report() function
    output = io.StringIO()
    sys.stdout = output
    mr.write_report()
    # Reset stdout
    sys.stdout = sys.__stdout__
    # Reset the position to the beginning of the stream
    output.seek(0)
    
    # Remove blank lines
    line = output.readline()
    while line.isspace():
        print(line)
        line = output.readline()
        
    # Remove line of dashes
    output.readline()
    
    # Verify the data printed in the table is consistent with the data in the
    # global dictionary
    for line in output:
        first, last, _, sum_donation, n_donation, _, avg_donation = line.split()
        name = f"{first} {last}"
        actual_sum = sum(mr.donors[name])
        actual_n =  len(mr.donors[name])
        assert float(sum_donation) == round(actual_sum,2)
        assert int(n_donation) == actual_n
        assert float(avg_donation) == round(actual_sum/actual_n,2)
        
      
def test_flow():
    """Test the "flow" of the interactive section. 
    
    This test runs a sequence of "user inputs" that should result in the
    interactive session being exited normally (through the 'quit' command). 
    If the interactive session does not exit normally after a given sequence of user 
    commands, an EOFError is raised since the interactive program will expect
    more commands, and this test will fail."""
    
    # Each string is a sequence of commands that a user might enter
    cmds = ["q", 
            "c  s  q",
            "t  l  q  q",
            "t  e  q  q  q",
            "t  e  Patrick Carrier  q  q  q"]
    
    for cmd in cmds:
        cmd_i = cmd.replace("  ", "\n")
        sys.stdin = io.StringIO(cmd_i)
    
        with open(os.devnull,'w') as output:
            sys.stdout = output
            # Run the mailroom program for the given sequence of commands
            mr.menu(mr.main_prompt, mr.main_disp_dict)

            
        
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    