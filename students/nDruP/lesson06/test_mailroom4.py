from mailroom4 import *
import datetime
import os.path


def test_main_menu():
    assert main_menu("1") == craft_thank_u
    assert main_menu("2") == create_report
    assert main_menu("3") == create_letters
    assert main_menu("4") == sys.exit


def test_check_not_exit():
    assert check_not_exit("Exit") == False
    assert check_not_exit("exit") == False
    assert check_not_exit("Bpb") == True
    assert check_not_exit("") == True


def test_user_input():
    test_str = ["exit", "Bob", "12345", "cwd"]
    assert user_input(test_str[0]) == ""
    assert user_input(test_str[1]) == test_str[1]
    assert user_input(test_str[2]) == test_str[2]
    assert user_input(test_str[3]) == test_str[3]


def test_fstr_keylist():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"1": [2134]}
    assert fstr_keylist(dict1) =="a\nb\nc\n"
    assert fstr_keylist(dict2) == "1\n"


def test_conv_str_money():
    assert conv_str_money("12") == 12.0
    assert conv_str_money("849375.2345") == 849375.23
    assert conv_str_money("bad") == "bad"
    assert conv_str_money(None) == None


def test_add_new_donation():
    add_new_donation("Andrew", 1.1)
    assert "Andrew" in donor_dict.keys()
    assert 1.1 in donor_dict.get("Andrew")
    add_new_donation("Andrew", 123)
    assert 123 in donor_dict.get("Andrew")


def test_thank_u_str():
    assert thank_u_str("Andrew", 13) == (divider + f"Dearest Andrew,\n"
            f"\tThank you for donation(s) of $13.00!\n"
            "We will use your donation(s) to create real living Pokemon.\n"
            "You now have our eternal loyalty. Use it wisely.\n"
            "Sincerely,\n"
            f"We're a Pyramid Scheme & so is Andrew"
            + divider)


def test_report():
    x = "a"


def test_write_letter_to_dir():
    curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
    x = ("Emelio h", [1, 2, 3])
    y = ("Garbanzo o", [4, 5, 6])
    z = ("Preid", [7, 8, 9])
    write_letter_to_dir(x[0], x[1])
    write_letter_to_dir(y[0], y[1])
    write_letter_to_dir(z[0], z[1])
    assert os.path.isfile("Emelio_h_"+curdate+".txt")
    assert os.path.isfile("Garbanzo_o_"+curdate+".txt")
    assert os.path.isfile("Preid_"+curdate+".txt")
    
