"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 2nd 2019
"""

#Why does testing client interaction seem nearly impossible?

"""
Functions Tested: Should contain no client interaction and simply called
by other functions.
    thank_you_specific(donor, amount, form)
    create_report(donor_table)
    get_donors_info()

Functions not Tested: Due to client interactions, these functions were not
unit tested but should be condensed enough that the interactions makes up
most of the function.
    donation_amount(name)
    thank_you()
    start_up()

Functions not Tested: These other have limited manipulation or work closely
with another function that 'was' tested.
    display_report() - related to create_report(donor_table)
    letters() - related to get_donors_info() + thank_you_specific(donor, donations, 'letter')
"""

from mailroom_4 import thank_you_specific, create_report, get_donors_info

note = ("\nTom, \n\n    Your donation of $194.55 "
        + "was received and we are forever grateful for your support."
        + "\n\nSincerely,\nDonation Center\n(555) 555-5555")

letter = ("Jerry, \n\n    Your donations of $2000.99"
        + " have gone a long way and we value your continued support."
        + "\n\nSincerely,\nDonation Center\n(555) 555-5555")

donor_table = [['Adam Alvarez', 1.25, 1, 1.25], ['Beth Bonnor', 2.73, 1, 2.73]]

donor_table_output = ("\n\n\nDonor Name        | Total Given | Num Gifts  | Average Gift"
                    + "\n-----------------------------------------------------------\n"
                    + "Beth Bonnor       $        2.73       1      $         2.73\n"
                    + "Adam Alvarez      $        1.25       1      $         1.25\n")

donors_info = {'Adam Alvarez': 1.25, 'Beth Bonnor': 2.73,
               'Cate Campbell': 7.77, 'Dave Don': 5691.33, 'Eric Ebron': 21.52}

def test_thank_you_specific1():
    assert thank_you_specific('Tom','194.55','note') == note

def test_thank_you_specific2():
    assert thank_you_specific('Jerry', '2000.99', 'letter') == letter

def test_create_report():
    assert create_report(donor_table) == donor_table_output

def test_get_donors_info():
    assert get_donors_info() == donors_info
