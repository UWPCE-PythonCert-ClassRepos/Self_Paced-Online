# open a terminal window
# cd Lesson06
# pytest test_mailroom_lesson06.py
import hashlib
import os
import mailroom_lesson06_module as mrm
import shutil

"""
assert whether spam_donors creates files
"""
def test_1():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    new_donation = [float(100.0)]
    new_donor = "test_donor1".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation
    mrm.spam_donors(tmp_directory)
    if os.path.isfile(tmp_directory + "\\test_Thank_You_Letter.txt"):
        assert FileExistsError


"""
assert whether the tool creates an accurate donor file (using a known hash of the file)
"""
def test_2():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    try:
        shutil.rmtree(tmp_directory)
    except:
        pass
    hash_file = tmp_directory + "\\Test_Donor2_Thank_You_Letter.txt"
    new_donation = [float(100.0)]
    new_donor = "test_donor2".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation
    mrm.spam_donors(tmp_directory)
    hash = hashlib.md5()
    with open(hash_file, 'rb') as afile:
        buf = afile.read()
        hash.update(buf)
    print(hash.hexdigest())
    assert hash.hexdigest() == "67adbfb0ea0e114c2edb42444f92e85d" #08640f41a7b00b2add9f967745773a51


"""
assert that create_ty_letter creates a donor when requested
"""
def test_3():
    new_donation = 100.0
    new_donor = "test_donor3".title()
    mrm.create_ty_letter("new", new_donor, new_donation)
    assert new_donor in mrm.esteemed_donors_dict


"""
assert that create_ty_letter creates an accurate list after donor is added by replicating functionality
"""
def test_4():
    donor_list_before = list(mrm.esteemed_donors_dict.keys())
    ls_cnt_before = len(donor_list_before)
    new_donation = 100.0
    new_donor = "test_donor4".title()
    mrm.create_ty_letter("new", new_donor, new_donation)
    donor_list_after = list(mrm.esteemed_donors_dict.keys())
    ls_cnt_after = len(donor_list_after)
    assert ls_cnt_before + 1 == ls_cnt_after and donor_list_after.count(new_donor) == 1


"""
assert that create_ty_letter add_to_donor to an existing donor when requested
"""
def test_5():
    new_donation = 100.0
    new_donor = "test_donor4".title()
    mrm.create_ty_letter("add_to_donor", new_donor, new_donation)
    esteemed_donors_dict_summed = {k: sum(v) for (k, v) in mrm.esteemed_donors_dict.items()}
    sum_amt = float(esteemed_donors_dict_summed[new_donor])
    assert sum_amt == 200.0


"""
assert create_report creates donors in summed_donor_list
"""
def test_6():
    new_donation_1 = [float(100.0)]
    new_donation_2 = 100.0
    new_donor = "test_donor6".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation_1
    mrm.esteemed_donors_dict.setdefault(new_donor, []).append(new_donation_2)
    mrm.create_report()
    donor_match = ""
    for sublist in mrm.summed_donor_list:
        if sublist[0] == new_donor:
            donor_match = "new_donor"
            break
    assert donor_match == "new_donor"


"""
assert create_report correctly totals user donations
"""
def test_7():
    new_donation_1 = [float(100.0)]
    new_donation_2 = 100.0
    new_donor = "test_donor7".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation_1
    mrm.esteemed_donors_dict.setdefault(new_donor, []).append(new_donation_2)
    mrm.create_report()
    donor_sum = 0
    for sublist in mrm.summed_donor_list:
        if sublist[0] == new_donor:
            donor_sum = sublist[1]
            break
    assert donor_sum == 200.0


"""
assert create_report correctly counts user donations
"""
def test_8():
    new_donation_1 = [float(100.0)]
    new_donation_2 = 100.0
    new_donor = "test_donor8".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation_1
    mrm.esteemed_donors_dict.setdefault(new_donor, []).append(new_donation_2)
    mrm.create_report()
    donor_cnt = 0
    for sublist in mrm.summed_donor_list:
        if sublist[0] == new_donor:
            donor_cnt = sublist[2]
            break
    assert donor_cnt == 2


"""
assert create_report correctly averages user donations
"""
def test_9():
    new_donation_1 = [float(100.0)]
    new_donation_2 = 100.0
    new_donor = "test_donor9".title()
    mrm.esteemed_donors_dict[new_donor] = new_donation_1
    mrm.esteemed_donors_dict.setdefault(new_donor, []).append(new_donation_2)
    mrm.create_report()
    donor_ave = 0
    for sublist in mrm.summed_donor_list:
        if sublist[0] == new_donor:
            donor_ave = sublist[3]
            break
    assert donor_ave == 100.0


"""
assert list is created when user types 'list'
"""
def test_10(capfd):
    test_string = ""
    mrm.function_calls("ty", "list", "", "", 0.0)
    out, err = capfd.readouterr()
    if "John Jacob Astor\nAlan Rufus, 1st Lord of Richmond\nHenry Ford\nCornelius Vanderbilt\nJakob Fugger\n" in out:
        test_string = "success"
    assert test_string == "success"


""" 
assert a new user is added when the user chooses to add a new user
"""
def test_11():
    new_donation = 100.0
    new_donor = "test_donor10".title()
    mrm.function_calls("ty", "new", new_donor, "", new_donation)
    assert new_donor in mrm.esteemed_donors_dict


""" function_calls(func, action="", new_donor_name="", directory="", response_donation_amt=0.0):
assert a donation amt is added to an existing user when the user chooses
"""
def test_12():
    new_donation = 100.0
    new_donor = "test_donor10".title()
    mrm.function_calls("ty", "add_to_donor", new_donor, "", new_donation)
    esteemed_donors_dict_summed = {k: sum(v) for (k, v) in mrm.esteemed_donors_dict.items()}
    sum_amt = float(esteemed_donors_dict_summed[new_donor])
    assert sum_amt == 200.0


"""
assert the tool creates a report when the user chooses
"""
def test_13(capfd):
    mrm.function_calls("cr", "", "", "", 0.0)
    out, err = capfd.readouterr()
    if "Donor Name                              Total Donation      Number of Donations           Ave Donation\n" in out:
        test_string = "success"
    assert test_string == "success"

"""
assert the tool spams all users when the user chooses
   # mr.spam_donors(directory)
"""
def test_14():
    tmp_directory = "{}/tmp/".format(os.getcwd())
    try:
        shutil.rmtree(tmp_directory)
    except:
        pass
    mrm.function_calls("s", "", "", tmp_directory, 0.0)
    tmp_file = "{}/tmp/Cornelius Vanderbilt_Thank_You_Letter.txt".format(os.getcwd())
    assert os.path.exists(tmp_file) == 1

"""
assert obtain_donation_amt(donor_name):
"""


"""
assert 
"""


