from mailroom import send_thank_you, create_report, send_all
import pytest

# Test the send_thank_you function: basic


def test_1():
    assert send_thank_you("Angelina Jolie", 3.47) == ('Dear Angelina Jolie,'
                                                      ' we wanted to say thank'
                                                      ' you for your generous'
                                                      ' donation of $3.47!')

# Test the send_thank_you function: long name


def test_2():
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


def test_3():
    assert send_thank_you("Angelina Jolie", 3) == ('Dear Angelina Jolie,'
                                                   ' we wanted to say thank'
                                                   ' you for your generous'
                                                   ' donation of $3.00!')

# Test the send_thank_you function: string input error


def test_4():
    with pytest.raises(ValueError):
        assert send_thank_you('Angelina Jolie', 'donation')

# Test the create_report function


def test_5():
    assert create_report() == ('Report has been created.')

# Test the send_all function


def test_6():
    assert send_all() == ('Letters have been sent to all donors.')
