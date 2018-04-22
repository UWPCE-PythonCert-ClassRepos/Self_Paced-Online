from mailroom_oo import Donor, Mailroom
from helpers import main_menu, set_donor_name
import sys


donor1 = Donor('Ghassan', [100, 200, 300])
donor2 = Donor('Miles', [52, 241, 736])
donor3 = Donor('Jack', [425, 100, 245])
donor4 = Donor('Tony', [55, 342, 765])
mr = Mailroom([donor1, donor2, donor3, donor4])


def thankyou_procedure():
    donor_name = set_donor_name()
    if donor_name.lower() == 'list':
        all_donors = mr.list_donors()
        print(all_donors)
    elif donor_name in mr.all_donors():
        thx = mr.send_thankyou(donor_name)
        print(thx)
    else:
        mr.add_donor(Donor(donor_name, []))


def main():
    while True:
        users_choice = main_menu()
        selection = {
            '1': thankyou_procedure,
            '2': mr.create_report,
            '3': mr.save_report,
            '4': sys.exit
        }
        try:
            selection[users_choice]()
        except KeyError:
            print('Choose 1 to 4')
            pass
