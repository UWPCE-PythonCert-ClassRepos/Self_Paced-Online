#Mailroom script that creates canned responses for donations and prints a report of all donations
from cli_main import *
from donor_models import *

def main():
    #initialize donors list
    donors = DonorCollection()

    #initialize CLI interface with the donors list
    cli = CLI_main(donors)

    #call CLI menu
    cli.show_menu()

#Main program
if __name__ == '__main__':
    main()



