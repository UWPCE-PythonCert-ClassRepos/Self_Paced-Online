#!/usr/bin/env python

"""
Testing unit for mailroom.python
"""

donor_dict = {'Mickey Mouse': [100.00, 150.00, 100.00], 'Minnie Mouse': [50.00, 50.00], 'Ron Jones': [100.00], 'Donald Duck': [25.00], 'Busy Bear': [250.00, 10.00, 10.00]}

# you can change this import to test different versions
#import mailroom
from mailroom import print_donors
#from mailroom import print_donors, send_thankyou
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party

# test donor list function
def test_1():
    assert print_donors() == ['Mickey Mouse\n', 'Minnie Mouse\n', 'Ron Jones\n', 'Donald Duck\n', 'Busy Bear\n']

"""
def test_2():
    assert cigar_party(50, False) is True


def test_3():
    assert cigar_party(70, True) is True


def test_4():
    assert cigar_party(30, True) is False


def test_5():
    assert cigar_party(50, True) is True


def test_6():
    assert cigar_party(60, False) is True


def test_7():
    assert cigar_party(61, False) is False


def test_8():
    assert cigar_party(40, False) is True


def test_9():
    assert cigar_party(39, False) is False


def test_10():
    assert cigar_party(40, True) is True


def test_11():
    assert cigar_party(39, True) is False
    
"""   