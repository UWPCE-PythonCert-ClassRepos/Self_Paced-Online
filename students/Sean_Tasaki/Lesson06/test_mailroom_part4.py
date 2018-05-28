#!/usr/bin/env python3
import mailroom_part4 as mailroom 
from collections import defaultdict
import pytest

@pytest.fixture()
def resource_a():
    s = 'Sean'
    return s

    

def test_add_donor_to_dict(resource_a):
    mailroom.add_donor_to_dict(resource_a)
    assert 'Sean' in mailroom.donor_dict
    assert 'Bob Dylan' in mailroom.donor_dict
    assert 'Leonard Cohen' in mailroom.donor_dict
    assert 'Soren Kierkegaard' in mailroom.donor_dict

def test_add_donor_amount():
    mailroom.add_donor_amount('Sean', 5)
    assert mailroom.donor_dict.get('Sean') == [5.00, 1, 5.00]
