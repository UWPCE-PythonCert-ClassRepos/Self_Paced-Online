'''
Tests for mailroom_oo.py
'''

import os
import mailroom_oo

tester = mailroom_oo.Donor("Test Person", [1, 2, 3])
tester2 = mailroom_oo.Donor("Test2 Person2", [4, 5, 6])
test_donors = mailroom_oo.DonorList([tester, tester2])

def test_name():
    assert(tester.name == "Test Person")

def test_first_donations():
    assert(tester.donations == [1, 2, 3])

def test_donor_totals():
    assert(tester.donor_totals == 6)

def test_add_donations():
    add_tester = mailroom_oo.Donor("Test Person", [1, 2, 3])
    add_tester.add_donation(4)
    assert(add_tester.donations == [1, 2, 3, 4])
    assert(add_tester.donor_totals == 10)

def test_num_donations():
    assert(tester.num_donations == 3)

def test_average_donations():
    assert(tester.average_donations == 2)

def test_list_donor_names():
    assert(test_donors.list_donor_names() == "Test Person\nTest2 Person2")

def test_add_donor():
    tester = mailroom_oo.Donor("Test Person", [1, 2, 3])
    tester2 = mailroom_oo.Donor("Test2 Person2", [4, 5, 6])
    test_donors = mailroom_oo.DonorList([tester, tester2])
    assert(test_donors.list_donor_names() == "Test Person\nTest2 Person2")
    tester3 = mailroom_oo.Donor("Test3 Person3", [7, 8, 9])
    test_donors.add_donor(tester3)
    assert(test_donors.list_donor_names() == "Test Person\nTest2 Person2\nTest3 Person3")
    assert(tester3.num_donations == 3)
    
def test_add_donation():
    test_add = mailroom_oo.DonorList([tester, tester2])
    test_add.add_donation(tester, 4)
    assert(tester.num_donations == 4)

def test_add_donor_and_donation():
    tester = mailroom_oo.Donor("Test Person", [1, 2, 3])
    tester2 = mailroom_oo.Donor("Test2 Person2", [4, 5, 6])
    test_donors = mailroom_oo.DonorList([tester])
    test_donors.add_donor_and_donation(tester2, 7)
    assert(tester2.num_donations == 4)

def test_order_donors():
    # Second person should be tester
    o_d = test_donors.order_donors()
    assert(o_d[1] == [tester])


if __name__ == "__main__":
    test_donors.send_thanks()    




    # while True:
    #     choice = input(
    #     "Please select an option:\n\
    #     1 - Send Thanks\n\
    #     2 - Create Donor Report\n\
    #     3 - Send Letters\n\
    #     4 - Quit\n")
    #     print()
    #     if choice == '1':
    #         send_thanks(donors)
    #     if choice == '2':
    #         create_donor_report(donors)
    #     if choice == '3':
    #         send_letters(donors)
    #     if choice == '4':
    #         donors.quitter()
    