from mailroom import *
import os

'''
Items to Test:
    sum_gifts
    count_gifts
    sorted donors
    list_donors
    *thanks letter
    *send_thanks_all

Items with user interaction: (can pytest test/simulate user imput?)
    rec_donation
    send_thanks_one
    menu

Not sure how to test w/ pytest:
    create_report
    run_func
    __name__ == __main__
'''

def test_1():
    assert sum_gifts("Anita Bath") == 350


def test_2():
    assert count_gifts("Seymour Butz") is 2


def test_3():
    name_list = ['Seymour Butz',
                 'Anita Bath',
                 'Isabelle Ringing',
                 'John Smith']
    name_list_sorted = sorted_donors()
    for n in name_list:
        assert n in name_list_sorted


sample_dict = {"Tom": [100, 200], "Jane": [500]}


def test_4():
    assert list_donors(sample_dict) is ['Tom', 'Jane'] or ['Jane', 'Tom']


dnr_name = "Anita Bath"

# Tested by send_thanks_all
# def test_6():
#     thanks_letter()
#     tf = os.path.isfile('./Anita_Bath.txt')
#     assert tf is True


def test_5():
    send_thanks_all()
    ab = os.path.isfile('./Anita_Bath.txt')
    ir = os.path.isfile('./Isabelle_Ringing.txt')
    js = os.path.isfile('./John_Smith.txt')
    sb = os.path.isfile('./Seymour_Butz.txt')
    assert ab is True
    assert ir is True
    assert js is True
    assert sb is True
