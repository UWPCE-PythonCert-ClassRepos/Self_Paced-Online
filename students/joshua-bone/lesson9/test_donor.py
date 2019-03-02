import math
import pytest
from donor import Donor


def floating_equals(f1, f2):
    return math.fabs(f1 - f2) < 0.0000001


def test_init():
    d = Donor("Mark", 10)
    assert d._name == "Mark"
    assert d._donations == [10]


def test_name():
    d = Donor("Mark", 10)
    assert d.name == "Mark"


def test_donations():
    d = Donor("Mark", 10)
    assert d.donations == (10,)


def test_add_donation():
    d = Donor("Mark", 10)
    d.add_donation(20)
    assert d.donations == (10, 20)


def test_num_donations():
    d = Donor("Mark", 10)
    assert d.num_donations == 1
    d.add_donation(20)
    assert d.num_donations == 2


def test_avg_donations():
    d = Donor("Mark", 10)
    assert floating_equals(d.avg_donation, 10.0)
    d.add_donation(20)
    assert floating_equals(d.avg_donation, 15.0)


def test_total_amt():
    d = Donor("Mark", 10)
    assert d.total_amt == 10
    d.add_donation(2.34)
    assert floating_equals(d.total_amt, 12.34)


def test_eq():
    d1 = Donor("Mark", 10)
    assert d1 == Donor("Mark", 10)
    assert d1 != Donor("Mark", 20)
    assert d1 != Donor("Mary", 10)
