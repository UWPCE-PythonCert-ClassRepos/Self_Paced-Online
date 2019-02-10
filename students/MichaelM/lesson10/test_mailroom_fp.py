# open a terminal window
# pytest lesson10/test_mailroom_fp.py


import hashlib
import os
import mailroom_classes_fp as mc
import shutil
import pytest

def clean_directory(dir):
    try:
        shutil.rmtree(dir)
    except:
        pass

"""
assert that a new donor can be added into the donors dictionary with the correct name and donation amount
"""
def test_1():

    exists = ""
    new_donor = "test_donor1".title()
    new_donation = [float(101.0)]
    d = mc.Donors()
    d.donor_name = new_donor
    d.donation_amt = new_donation
    d.esteemed_donors_dict[d.donor_name] = [d.donation_amt]
    for k, v in list(d.esteemed_donors_dict.items()):
        if k == new_donor and v[0] ==  new_donation:
            exists = "yes"
    assert exists == "yes"
    del d.esteemed_donors_dict[d.donor_name]


"""
assert whether Donors.print_letters creates files
"""

def test_2():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    clean_directory(tmp_directory)
    new_donor = "test_donor2".title()
    new_donation = [float(102.0)]
    d = mc.Donors()
    d.donor_name = new_donor
    d.donation_amt = new_donation
    d.esteemed_donors_dict[d.donor_name] = d.donation_amt
    d.print_letters(tmp_directory)
    if os.path.isfile(tmp_directory + "\\Test_Donor2_Thank_You_Letter.txt"):
        assert FileExistsError


"""
assert whether the tool creates an accurate donor file (using a known hash of the file)
"""
def test_3():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    clean_directory(tmp_directory)
    new_donor = "test_donor3".title()
    new_donation = [float(103.0)]
    d = mc.Donors()
    d.donor_name = new_donor
    d.donation_amt = new_donation
    d.esteemed_donors_dict[d.donor_name] = d.donation_amt
    d.print_letters(tmp_directory)
    hash_file = tmp_directory + "\\Test_Donor3_Thank_You_Letter.txt"
    hash = hashlib.md5()
    with open(hash_file, 'rb') as afile:
        buf = afile.read()
        hash.update(buf)
    print(hash.hexdigest())
    assert hash.hexdigest() == "84f2d04d5bab6686066121cf05302b52"


"""
assert that a new thank you letter is created with a new donor
"""
def test_4(capfd):
    test_string = ""
    new_donor = "test_donor4".title()
    new_donation = [float(104.0)]
    letter = mc.Mailroom.donor_letters("new", new_donor, new_donation, 0.0)
    print(letter)
    out, err = capfd.readouterr()
    if new_donor in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that add_donation creates an accurate list after a donor is added
"""
def test_5():
    d = mc.Donor()
    ls_cnt_before = len(list(mc.Mailroom.esteemed_donors_dict.keys()))
    new_donation = 105.0
    new_donor = "test_donor5".title()
    d.add_donation(new_donor, new_donation)
    ls_cnt_after = len(list(mc.Mailroom.esteemed_donors_dict.keys()))
    assert ls_cnt_before + 1 == ls_cnt_after


"""
assert that donor_total totals correctly
"""
def test_5():
    d = mc.Donor()
    new_donation1 = 105.0
    new_donation2 = 105.0
    new_donor = "test_donor5".title()
    d.add_donation(new_donor, new_donation1)
    d.add_donation(new_donor, new_donation2)
    new_donor_total = d.donor_total(new_donor)
    assert new_donor_total == 210.0


"""
assert summed_donor_list returns the correct values (donor_sum, donation_cnt, donation_cnt)
"""
def test_6():
    d = mc.Donor()
    new_donation1 = 106.0
    new_donation2 = 106.0
    new_donor = "test_donor6".title()
    d.add_donation(new_donor, new_donation1)
    d.add_donation(new_donor, new_donation2)
    ds = mc.Donors()
    donors_list = ds.sum_donors()
    search = new_donor
    for sublist in donors_list:
        if sublist[0] == search:
            donor_sum = sublist[1]
            donation_cnt = sublist[2]
            donor_ave = sublist[3]
            break
    assert donor_sum == 212.0 and donation_cnt == 2 and donor_ave == 106.0



"""
assert the tool creates an acurate report of a donor
"""
def test_7(capfd):
    d = mc.Donor()
    new_donation1 = 107.0
    new_donor = "test_donor7".title()
    d.add_donation(new_donor, new_donation1)
    donors = mc.Donors()
    summed_donor_list = donors.sum_donors()
    tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
    print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
        name=mc.Mailroom.esteemed_donors_headers[0],
        total_donation=mc.Mailroom.esteemed_donors_headers[1],
        donation_cnt=mc.Mailroom.esteemed_donors_headers[2],
        ave_donation=mc.Mailroom.esteemed_donors_headers[3]))
    tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
    [print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                    total_donation=row[1],
                                                                                    donation_cnt=row[2],
                                                                                    ave_donation=row[3])
           ) for row in tmp_donor_list]
    out, err = capfd.readouterr()
    if "test_donor7                        214.0             2                             107.0":
        test_string = "success"
    assert test_string == "success"

"""
assert that a thank you letter is created with an existing donor
"""
def test_8(capfd):
    test_string = ""
    new_donor = "test_donor8".title()
    new_donation = [float(104.0)]
    letter = mc.Mailroom.donor_letters("existing_donor", new_donor, new_donation, 0.0)
    print(letter)
    out, err = capfd.readouterr()
    if new_donor in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that a donor name is set correctly
"""

def test_9(capfd):
    d = mc.Donor()
    new_donor = "test_donor9".title()
    d.donor_name = new_donor
    print(d.donor_name)
    out, err = capfd.readouterr()
    if new_donor in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that a donation is set correctly
"""

def test_10(capfd):
    test_string = ""
    d = mc.Donor()
    new_donation = [float(110.0)]
    d.donation_amt = new_donation
    print(*d.donation_amt)
    out, err = capfd.readouterr()
    if "110.0" in out:
        test_string = "success"
    assert test_string == "success"


# ---- NEW TESTING ADDED FOR LESSON10 ----
"""
assert that a temporary directory is set correctly
"""

def test_11(capfd):
    d = mc.Donors()
    tmp_directory = "{}/tmp/".format(os.getcwd())
    d.tmp_directory = tmp_directory
    print(d.tmp_directory)
    out, err = capfd.readouterr()
    if tmp_directory in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that challenge correctly splits a list based on a minimum amt (over a minimum prior contribution)
challenge(self, factor, donor, max_donation=0, min_donation=0)
"""

def test_12():
    d = mc.Donor()
    new_donor = "test_donor12".title()
    d.add_donation(new_donor, 50.0)
    d.add_donation(new_donor, 75.0)
    d.add_donation(new_donor, 100.0)
    d.add_donation(new_donor, 125.0)
    d.add_donation(new_donor, 150.0)
    d.donations_summmed = sum(d.challenge(2, new_donor, 0, 100))
    assert d.donations_summmed == 750.0


"""
assert that challenge correctly splits a list based on a maximum amt (under a maximum prior contribution)
"""

def test_13():
    d = mc.Donor()
    new_donor = "test_donor13".title()
    d.add_donation(new_donor, 50.0)
    d.add_donation(new_donor, 75.0)
    d.add_donation(new_donor, 100.0)
    d.add_donation(new_donor, 125.0)
    d.add_donation(new_donor, 150.0)
    d.donations_summmed = sum(d.challenge(2, new_donor, 100, 0))
    assert d.donations_summmed == 450.0


"""
assert challenge factors sums correctly based on a maximum amt (under a maximum prior contribution)
"""

def test_14():
    d = mc.Donor()
    new_donor = "test_donor14".title()
    d.add_donation(new_donor, 50.0)
    d.add_donation(new_donor, 75.0)
    d.add_donation(new_donor, 100.0)
    d.add_donation(new_donor, 125.0)
    d.add_donation(new_donor, 150.0)
    factor_of_1 = sum(d.challenge(1, new_donor, 100, 0)) #225.0
    factor_of_2 = sum(d.challenge(2, new_donor, 100, 0)) # 450.0
    factor_of_3 = sum(d.challenge(3, new_donor, 100, 0)) #675.0
    factor_of_4 = sum(d.challenge(4, new_donor, 100, 0)) #900.0
    assert factor_of_1 == 225.0 and factor_of_2 == 450.0 and factor_of_3 == 675.0 and factor_of_4 == 900.0


"""
assert that the correct donor is chosen and factored
"""

def test_15():
    d = mc.Donor()
    new_donor = "test_donor15".title()
    d.usr_name = new_donor
    d.add_donation(new_donor, 50.0)
    d.add_donation(new_donor, 75.0)
    d.add_donation(new_donor, 100.0)
    d.add_donation(new_donor, 125.0)
    d.add_donation(new_donor, 150.0)
    d.donations_summmed = sum(d.challenge(2, new_donor, 100, 0))
    assert d.donor_name == new_donor

''''''



