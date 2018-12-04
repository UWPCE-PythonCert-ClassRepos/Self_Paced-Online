import io
import pytest

from mailroom_lesson_09 import *

def test_show_list(capsys):
    c = DonorCollection()
    c.show_list()
    captured = capsys.readouterr()
    expected = '\nJosh Hoff\nTatsiana Kisel\n'
    assert captured.out == expected
    
def test_add_new_donor():
    c = DonorCollection()
    c.add_donor('Andrew', 300)
    assert 'Andrew' in c._donors.keys()
    assert c._donors['Andrew'] == [300]
    
def test_show_list_after_adding_donor(capsys):
    c = DonorCollection()
    c.add_donor('Andrew', 300)
    c.show_list()
    captured = capsys.readouterr()
    expected = '\nJosh Hoff\nTatsiana Kisel\nAndrew\n'
    assert captured.out == expected
    
def test_add_donation_to_existing_donor():
    c = DonorCollection()
    c.add_donor('Josh Hoff', 250)
    assert 'Josh Hoff' in c._donors.keys()
#NOTE: 25 and 75 are existing values for Josh Hoff
    assert c._donors['Josh Hoff'] == [25, 75, 250]
    
def test_report(capsys):
    c = DonorCollection()
    c.report()
    expected = '\nDonor Name             | Total Given | Num Gifts | Average Gift\n\
---------------------------------------------------------------\n\
Tatsiana Kisel          $      140.55           2       70.28\n\
Josh Hoff               $      100.00           2       50.00\n'
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == expected

    
def test_create_report_after_adding_donor(capsys):
    c = DonorCollection()    
    c.add_donor('Andrew', 300)
    c.add_donor('Josh Hoff', 250)
    c.report()
    expected = '\nDonor Name             | Total Given | Num Gifts | Average Gift\n\
---------------------------------------------------------------\n\
Josh Hoff               $      350.00           3      116.67\n\
Andrew                  $      300.00           1      300.00\n\
Tatsiana Kisel          $      140.55           2       70.28\n'
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == expected
    
def test_letters_to_everyone_files():
    c = DonorCollection()
    c.letters()
    tab = '    '
    for i, val in c._donors.items():
        with open(f'{i}.txt', 'r') as outfile:
            donation = sum(val)
            check_text = f'Dear {i}, \n\n{tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company'
            expected = outfile.read()
            assert check_text == expected
                
def test_donor_average():
    d = DonorCollection()
    c = Donor('Josh Hoff', d.donors['Josh Hoff'])
    d.add_donor('Andrew', 300)
    d.add_donor('Josh Hoff', 250)
    assert c.average == 116.67
    
def test_donor_number_of_gifts():
    d = DonorCollection()
    c = Donor('Tatsiana Kisel', d.donors['Tatsiana Kisel'])
    assert c.gifts == 2

def test_donor_total_donations():
    d = DonorCollection()
    c = Donor('Josh Hoff', d.donors['Josh Hoff'])
    d.add_donor('Josh Hoff', 250)
    assert c.total_donations == 350
    
def test_most_recent_gift():
    d = DonorCollection()
    c = Donor('Josh Hoff', d.donors['Josh Hoff'])
    d.add_donor('Josh Hoff', 400)
    assert c.recent_gift == 400
    
def test_first_gift():
    d = DonorCollection()
    c = Donor('Josh Hoff', d.donors['Josh Hoff'])
    assert c.first_gift == 25