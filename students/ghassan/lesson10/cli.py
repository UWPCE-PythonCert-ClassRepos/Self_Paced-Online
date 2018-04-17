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


def projections():
    total1 = 0
    total2 = 0
    for donor in mr.donors:
        total1 += sum(donor.mult_donations_by(2, max_donation=100))
        total2 += sum(donor.mult_donations_by(3, min_donation=50))
    print('total contribution would come to in dollars if they were to double contributions under $100: {}'.format(total1))  # noqa: E501
    print('total contribution would come to if they were to triple contributions over $50: {}'.format(total2))


def main():
    while True:
        users_choice = main_menu()
        selection = {
            '1': thankyou_procedure,
            '2': mr.create_report,
            '3': mr.save_report,
            '4': projections,
            '5': sys.exit
        }
        try:
            selection[users_choice]()
        except KeyError:
            print('Choose 1 to 5')
            pass
