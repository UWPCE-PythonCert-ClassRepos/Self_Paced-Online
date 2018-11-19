"""test suite for mailroom exercise"""
import os

import mock
import pytest

from mailroom import *


@pytest.fixture
def donors():
    return {'Doug F': [100.00, 5.00],
            'Patty P': [1.00, 1000.00],
            'Warren B': [3000.00],
           }

def test_create_new_donor(donors):
    """given donors dict
    when user creates new donor not in dict
    the user then shows up in dict with blank donations"""
    new_donor = 'Fisher Price'
    assert new_donor not in donors
    create_donor(new_donor, donors)
    assert new_donor in donors

def test_create_new_donor_creates_error_if_exists(donors):
    new_donor = 'Warren B'
    assert new_donor in donors

    with pytest.raises(KeyError) as e:
        create_donor(new_donor, donors)

def test_create_valid_donation(donors):
    """tests that value added to specific donor
    when create donation called"""
    assert donors['Warren B'] == [3000.00]

    create_donation('Warren B', 10, donors)
    assert donors['Warren B'] == [3000.00, 10]

def test_error_on_missing_donor(donors):
    """give user tries to add donation for non-existanant donor
    when the amount is applied
    an exception is returned"""
    assert 'The Bears' not in donors
    with pytest.raises(KeyError) as e:
        create_donation('The Bears', 10, donors)

def test_summarize_donor(donors):
        assert summarize_donor('Doug F', donors) == ('Doug F', 105.00, 2, 52.50)

def test_send_letters(donors, tmpdir):
        assert len(tmpdir.listdir())==0
        send_letters_to_everyone(donors=donors, thank_you_directory=tmpdir)
        assert len(tmpdir.listdir()) > 0

test_data = [(100, 100.00),
             (100.123123, 100.12),
             (1, 1.00),
             (0.5, 0.50)]
@pytest.mark.parametrize("input, expected", test_data)
def test_formatting_of_thankyou(input, expected):
        fullname = 'Paul Jurek'
        expected_string = f"""Dear {fullname},

        Thank you for your very kind donation of ${expected:.2f}.

        It will be put to very good use.

                       Sincerely,
                          -The Team"""
        assert create_donation_thank_you(fullname=fullname, amount=input) ==

def test_thank_you_creates_donor():
        """given user selects thank you and enters valid donor and amount
        the donors object is updated to have new input"""
        pass