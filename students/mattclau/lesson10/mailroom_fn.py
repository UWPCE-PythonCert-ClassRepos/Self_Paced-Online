#Mailroom script that creates canned responses for donations and prints a report of all donations
from cli_main import *
from donor_models import *

def main():
    #initialize donors list
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [9876.55])
    d3 = Donor("Charles Barkley",donations = [999999.99,55555.55,7777.77])
    d4 = Donor("Scottie Pippen",donations = [1, 5])
    d5 = Donor("Ursula K Le Guin",donations = [534567.89])

    donors = DonorCollection([d1, d2, d3, d4, d5])

    #initialize CLI interface with the donors list
    cli = CLIMain(donors)

    #call CLI menu
    cli.show_menu()

#Main program
if __name__ == '__main__':
    main()



