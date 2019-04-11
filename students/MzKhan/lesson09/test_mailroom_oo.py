'''
Name: Muhammad Khan
Date: 04/09/2019
Assignment09
'''
import os
from donor_models import Donor
from donor_models import DonorCollection

def test_init_():

    d = Donor("Benny", [2000])
    assert d.name == "Benny"
    assert d.donations == [2000]

    arg = [200, 300, 400, 100]
    d = Donor("Benny Huggins", arg)
    assert d.name == "Benny Huggins"
    assert d.donations == arg


def test_repr():

    d = Donor("Benny", [2000])
    assert repr(d) == 'Donor(Benny,[2000])'


def test_properties():

    d = Donor("John Adam", [307.9])
    assert d.name == "John Adam"
    assert d.donations == [307.9]
    assert d.total_donations == 1
    assert d.total_donations_amount == 307.9
    assert d.avg_donation == 307.9

    args = [200, 300, 400, 100]
    d = Donor("Ashley Wiggins", args)
    assert d.name == "Ashley Wiggins"
    assert d.donations == args
    assert d.total_donations == 4
    assert d.total_donations_amount == 1000
    assert d.avg_donation == 250


def test_add_donation():

    d = Donor("John Adam", [307.9])
    d.add_donation(200)
    assert d.donations[-1] == 200
    args = [200, 300, 400, 100]
    d = Donor("Ashley Wiggins", args)
    d.add_donation(500)
    assert d.donations[-1] == 500
    assert d.total_donations == 5
    assert d.total_donations_amount == 1500


donor_1 = Donor("Adam Johnson",[600, 2200])
donor_2 = Donor("Matt Marvin",[500,100])
donor_3 = Donor("Ashley Wiggins",[55])
dic = {"Adam Johnson":Donor("Adam Johnson",[600, 2200]),
     "Matt Marvin":Donor("Matt Marvin",[500,100]),
     "Ashley Wiggins":Donor("Ashley Wiggins",[55])}


def test__init__DonorCollection():

    d = DonorCollection(donor_1, donor_2, donor_3)
    assert d.donors.keys() == dic.keys()
    assert d.donors[donor_1.name].donations == [600, 2200]
    assert d.donors[donor_2.name].name == "Matt Marvin"


def test_aList():

    test_list=[["Adam Johnson",2800,2.,1400], ["Matt Marvin", 600,2,300 ],
                                                   ["Ashley Wiggins",55,1,55] ]
    d = DonorCollection(donor_1, donor_2, donor_3)
    assert d.a_list()[0] in test_list
    assert d.a_list()[1] in test_list
    assert d.a_list()[2] in test_list


def test_create_report():
    #It also tests the sort method.
    test_list=[["Adam Johnson",2800,2.,1400], ["Matt Marvin", 600,2,300 ],
                                                   ["Ashley Wiggins",55,1,55] ]
    d = DonorCollection(donor_1, donor_2, donor_3)
    assert d.create_report()[0] == ["Adam Johnson",2800,2.,1400]
    assert d.create_report()[2] == ["Ashley Wiggins",55,1,55]


def test_send_letter_everyone():

    d = DonorCollection(donor_1, donor_2, donor_3)
    d.send_letter_everyone()
    assert os.path.exists("Letters")
    donor_names = list(d.donors)
    for file in os.listdir(os.path.join("Letters")):
        donor = file[0:-15]
        assert donor in donor_names
