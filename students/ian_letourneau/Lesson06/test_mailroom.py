from mailroom import send_thank_you, create_report, send_all
import pytest, os

# Test the send_thank_you function: basic


def test_send_thank_you_valid_input():
    assert send_thank_you("Angelina Jolie", 3.47) == ('Dear Angelina Jolie,'
                                                      ' we wanted to say thank'
                                                      ' you for your generous'
                                                      ' donation of $3.47!')

# Test the send_thank_you function: long name


def test_send_thank_you_long_input():
    assert send_thank_you("The Great Leader of the"
                          " Azerothian people", 3.47) == ('Dear The Great'
                                                          ' Leader of the'
                                                          ' Azerothian people'
                                                          ', we wanted to'
                                                          ' say thank you for'
                                                          ' your generous'
                                                          ' donation of'
                                                          ' $3.47!')

# Test the send_thank_you function: integer input


def test_send_thank_you_int_input():
    assert send_thank_you("Angelina Jolie", 3) == ('Dear Angelina Jolie,'
                                                   ' we wanted to say thank'
                                                   ' you for your generous'
                                                   ' donation of $3.00!')


# Test the create_report function


def test_create_report_sorted():
    assert create_report() == ['LeBron James,6609558.50,4,1652389.62',
                              'Bill Gates,4040233.25,3,1346744.42',
                              'Jimmy Kimmel,1002495.96,5,200499.19',
                              'Angelina Jolie,6.47,2,3.24',
                      'The Great Leader of the Azerothian people,3.47,1,3.47']

# Test the send_all function


def test_send_all_outputs():
    files = send_all()
    # directory = "C:\\Users\\letoui\\Documents\\PythonCert\\Self_Paced-Online\\students\\ian_letourneau\\Lesson06"
    for file in files:
        assert os.path.isfile(file) == True
