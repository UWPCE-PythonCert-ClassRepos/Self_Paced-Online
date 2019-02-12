# open a terminal window
# pytest lesson9/test_mailroom_oo.py


import hashlib
import os
import mailroom_classes_oo as mc
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
    donation = 10.0
    d = mc.Donor("test_donor", "1")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    exists = ""
    new_donor = d.name
    for k, v in list(dc._esteemed_donors_dict.items()):
        if k == new_donor and v[0] ==  donation:
            exists = "yes"
    assert exists == "yes"


"""
assert whether Donors.print_letters creates files
"""

def test_2():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    donation = 10.0
    d = mc.Donor("test_donor", "2")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    dc.print_letters(tmp_directory)
    if os.path.isfile(tmp_directory + "\\Test_Donor 2_Thank_You_Letter.txt"):
        file_exists = True
    assert file_exists is True


"""
assert whether the tool creates an accurate donor file (using a known hash of the file)
"""
def test_3():
    donation = 10.0
    tmp_directory = "{}/tmp/".format(os.getcwd())
    d = mc.Donor("test_donor", "3")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    dc.print_letters(tmp_directory)
    hash_file = tmp_directory + "\\Test_Donor 3_Thank_You_Letter.txt"
    hash = hashlib.md5()
    with open(hash_file, 'rb') as afile:
        buf = afile.read()
        hash.update(buf)
    print(hash.hexdigest())
    assert hash.hexdigest() == "0897c592be8e4d98c192e0cc8ca0428d"


"""
assert that a new thank you letter is created with a new donor
"""
def test_4(capfd):
    test_string = ""
    donation = 10.0
    d = mc.Donor("test_donor", "4")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    letter = d.donor_letters("new", d.first, donation, 0.0)
    print(letter)
    out, err = capfd.readouterr()
    if "test_donor" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that add_donation creates a new user
"""
def test_5():
    d = mc.Donor("test_donor", "5")
    dc = mc.DonorCollection()
    ls_cnt_before = len(list(dc._esteemed_donors_dict.keys()))
    donation = 10.0
    dc.add_donation(d.name, donation)
    ls_cnt_after = len(list(dc._esteemed_donors_dict.keys()))
    assert ls_cnt_before + 1 == ls_cnt_after


"""
assert that donor_total totals correctly
"""
def test_5():
    donation1 = 10.0
    donation2 = 10.0
    d = mc.Donor("test_donor", "5")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation1)
    dc.add_donation(d.name, donation2)
    new_donor_total = dc.donor_total(d.name)
    assert new_donor_total == 20.0


"""
assert summed_donor_list returns the correct values (donor_sum, donation_cnt, donation_cnt)
"""
def test_6():
    donation1 = 10.0
    donation2 = 10.0
    d = mc.Donor("test_donor", "6")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation1)
    dc.add_donation(d.name, donation2)
    donors_list = dc.sum_donors()
    search = d.name
    for sublist in donors_list:
        if sublist[0] == search:
            donor_sum = sublist[1]
            donation_cnt = sublist[2]
            donor_ave = sublist[3]
            break
    assert donor_sum == 20.0 and donation_cnt == 2 and donor_ave == 10.0



"""
assert the tool creates an acurate report of a donor
"""
def test_7(capfd):
    test_string = ""
    donation1 = 10.0
    donation2 = 10.0
    d = mc.Donor("test_donor", "7")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation1)
    dc.add_donation(d.name, donation2)
    summed_donor_list = dc.sum_donors()
    tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
    print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
        name=dc.esteemed_donors_headers[0],
        total_donation=dc.esteemed_donors_headers[1],
        donation_cnt=dc.esteemed_donors_headers[2],
        ave_donation=dc.esteemed_donors_headers[3]))
    tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
    [print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                    total_donation=row[1],
                                                                                    donation_cnt=row[2],
                                                                                    ave_donation=row[3])
           ) for row in tmp_donor_list]
    out, err = capfd.readouterr()
    if "Test_Donor 7                            20.0                2                             10.0" in out:
        test_string = "success"
    assert test_string == "success"



"""
assert that a thank you letter is created with an existing donor
"""
def test_8(capfd):
    test_string = ""
    donation = 10.0
    d = mc.Donor("test_donor", "8")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    letter = d.donor_letters("existing_donor", d.first, donation, 0.0)
    print(letter)
    out, err = capfd.readouterr()
    if "test_donor" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that a donor name is set correctly
"""

def test_9(capfd):
    donation = 10.0
    d = mc.Donor("test_donor", "9")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    print(d.name)
    out, err = capfd.readouterr()
    if d.name in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that a donation is set correctly
"""

def test_10(capfd):
    test_string = ""
    donation = 10.0
    d = mc.Donor("test_donor", "10")
    dc = mc.DonorCollection()
    dc.add_donation(d.name, donation)
    names_list = list(dc._esteemed_donors_dict.keys())
    values_list = list(dc._esteemed_donors_dict.values())
    assert "Test_Donor 10" in names_list and 10.0 in values_list[0]

def test_11():
    test_string = ""
    donation1 = 10.0
    donation2 = 10.0
    donation3 = 10.0
    donation4 = 10.0
    d1 = mc.Donor("test_donor", "11")
    d2 = mc.Donor("test_donor", "12")
    dc = mc.DonorCollection()
    dc.add_donation(d1.name, donation1)
    dc.add_donation(d1.name, donation2)
    dc.add_donation(d2.name, donation3)
    dc.add_donation(d2.name, donation4)
    cnt = len(dc.distinct_donor_list())
    assert cnt == 2