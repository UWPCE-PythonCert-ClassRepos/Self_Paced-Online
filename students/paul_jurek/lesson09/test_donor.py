"""tests the donor class"""

import pytest

from Donor import Donor

@pytest.fixture
def example_donor():
        return Donor(id=1, firstname='Bob', lastname='Dod')

@pytest.mark.parametrize("new_donor", [Donor(firstname='Santa', lastname='Claus', id=1),
                                       Donor(id=2, firstname='', lastname='Jeff'),
                                       Donor(id=4, firstname=123, lastname=123),
                                       Donor(firstname='A', lastname='B', id=123)])
def test_donor_initiaztion(new_donor):
    """when donor is initiated
    the object is avaliable"""
    assert isinstance(new_donor, Donor)


def test_id_must_be_int():
    """when donor initiated with non-int id
    valueerror is raised"""
    with pytest.raises(ValueError):
        Donor(id='ss')

def test_donation_added(example_donor):
        """given empty donor
        when donation added
        total donation amount increases by amount"""
        assert example_donor.donation_total() == 0
        donation_amount = 10
        example_donor.add_donation(donation_amount)
        assert example_donor.donation_total() == donation_amount
        example_donor.add_donation(donation_amount)
        assert example_donor.donation_total() == 2 * donation_amount

def test_donation_count(example_donor):
        """given empty donor
        when 3 donations are added
        correct number of donations are returned"""
        # no donations yet
        assert example_donor.donation_count() == 0
        example_donor.add_donation(10)
        assert example_donor.donation_count() == 1
        example_donor.add_donation(10)
        example_donor.add_donation(10)
        assert example_donor.donation_count() == 3

def test_summarize_donor(example_donor):
        """given an empty donor
        when 4 donations are added and user calls summarize_donor
        a tuple is returned with id, name, total gifts, number of gifts, avg donation"""
        example_donor.add_donation(2)
        example_donor.add_donation(4)
        example_donor.add_donation(6)
        assert example_donor.summarize_donor() == (1, 'Bob Dod', 12, 3, 4)
