#!/usr/bin/env python3

from mailroom import Donor, Donor_list
import run_mailroom


def test_donor_name():
    alex = Donor('Alex', [100])
    assert alex.name == 'Alex'


def test_donor_amounts():
    alex = Donor('Alex', [100])
    assert alex.donations == [100]


def test_donor_new_donation():
    alex = Donor('Alex', [100])
    alex.new_donation(300)
    assert alex.donations == [100, 300]


def test_donor_letter_with():
    '''test the note writing function with a current donation'''
    alex = Donor('Alex', [100])
    alex.new_donation(500)
    output = ("Dear Alex,\n\nThank you for your generosity to our cause.\nYour"
              " recent gift of $500 is very helpful. You have now given a "
              "total of $600.\nWe greatly appreciate your contributions!"
              "\n\nThank you!\nAlex Laws")
    assert alex.write_note(500) == output


def test_donor_letter_witout():
    '''test the note writing function without a current donation'''
    alex = Donor('Alex', [100])
    output = ("Dear Alex,\n\nThank you for your generosity to our cause.\nYou "
              "have now given a total of $100.\nWe greatly appreciate "
              "your contributions!\n\nThank you!\nAlex Laws")
    assert alex.write_note() == output


def test_tot_given():
    alex = Donor('Alex', [100, 600, 200])
    assert alex.tot_given == 900


def test_num_donations():
    alex = Donor('Alex', [100, 600, 200])
    assert alex.num_donations == 3


def test_avg_donation():
    alex = Donor('Alex', [100, 600, 200])
    assert alex.avg_donation == 300


def test_str_fun():
    alex = Donor('Alex', [100, 600, 200])
    report = alex.__str__()
    assert report == ("Alex              $        900.00             "
                      "3 $       300.00")


def test_repr_fun():
    alex = Donor('Alex', [100, 600, 200])
    what_is_it = alex.__repr__()
    assert what_is_it == ('Donor(\'Alex\', [100, 600, 200])')


def test_lt():
    a = Donor('a', [10])
    b = Donor('b', [20])
    assert (a < b) is True


def test_gt():
    a = Donor('a', [10])
    b = Donor('b', [20])
    assert (a > b) is False


def test_equal_to():
    a = Donor('a', [10])
    b = Donor('b', [20])
    assert (a == b) is False


def test_not_equal_to():
    a = Donor('a', [10])
    b = Donor('b', [20])
    assert (a != b) is True


def test_donor_list():
    alex = Donor('Alex', [100])
    a = Donor_list(alex)
    assert a.donor_dictionary == [alex]


def test_donor_list_add_donor():
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    a = Donor_list(alex)
    a.add_donor(ryan)
    assert a.donor_dictionary == [alex, ryan]


def test_check_donor_list():
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    a = Donor_list(alex, ryan)
    is_alex = a.check_donor(alex.name)
    assert is_alex is True


def test_donor_list_get():
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    a = Donor_list(alex, ryan)
    alex_donor = a.get_donor(alex.name)
    assert alex_donor == alex


def test_donor_list_get():
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    a = Donor_list(alex, ryan)
    b = a.sort_donors()
    assert b == [ryan, alex]


def test_donor_list_str():
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    a = Donor_list(alex, ryan)
    assert a.__str__() == 'Alex\nRyan'


def test_gen_dest():
    '''test destination creation without giving a directory (user input req)'''
    alex = Donor('Alex', [100])
    output = "Alex.txt"
    assert run_mailroom.generate_destination(alex, 'n') == output


def test_add_donation_existing_donor():
    '''test function that adds donations to existing person'''
    alex = Donor('Alex', [100])
    ryan = Donor('Ryan', [300])
    donor_list_obj = Donor_list(alex, ryan)
    run_mailroom.add_donation('Ryan', 500, donor_list_obj)
    assert donor_list_obj.get_donor('Ryan').donations == [300, 500]


def test_add_donation_new_donor():
    '''test function that adds donations to new person'''
    alex = Donor('Alex', [100])
    donor_list_obj = Donor_list(alex)
    run_mailroom.add_donation('Ryan', 500, donor_list_obj)
    assert donor_list_obj.get_donor('Ryan').donations == [500]
