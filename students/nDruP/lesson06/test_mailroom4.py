from mailroom4 import *


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
