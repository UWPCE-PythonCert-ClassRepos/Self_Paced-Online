
from mailroom_oo import *


def test_donor_name():
    d = Donor("Alejandro Guardia")
    assert d.name == "Alejandro Guardia"


def test_donations_init():
    d = Donor("Alejandro Guardia")
    assert d.donations == []


def test_add_donation():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    assert d.donations == [25]
    d.add_donation(50)
    assert d.donations == [25,50]


def test_total_donations():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    d.add_donation(50)
    d2 = Donor("Inge")
    assert d.total_donations() == 75
    assert d2.total_donations() == 0


def test_average_donation():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    d.add_donation(50)
    assert d.average_donation() == 37.5



