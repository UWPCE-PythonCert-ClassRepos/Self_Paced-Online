from mailroom import *
import pytest
import os
import copy

initial_donations = {
    "William Gates, III": [3, 5, 7],
    "Mark Zuckerberg": [4.50, 8, 2],
    "Jeff Bezos": [7.77],
    "Paul Allen": [3.6, 4.5],
    "bob": [.01],
    "bill": []
}

donations = copy.deepcopy(initial_donations)

donations = defaultdict(list, donations)


def test_menu():
    pass


def test_menu_handler(capsys):
    flag = False

    def a(input = flag):
        print('Ran func A')

    def b(input = flag):
        print('Ran func B')

    mock_menu = {'A': a, 'B': b}
    menu_handler('A', mock_menu)
    captured = capsys.readouterr()
    assert('Ran func A' in captured.out)
    menu_handler('B', mock_menu)
    captured = capsys.readouterr()
    assert('Ran func B' in captured.out)
    with pytest.raises(KeyError):
        menu_handler(2, mock_menu)


def test_quitbale_function_prompt():
    # input_dict =
    # def mock_input():
    pass
    # monkeypatch.setattr('builtins.input', lambda x: "Mark")
    # requires mocking input
    # - can we do this consecutively for a full functional test?


def test_thank_you():
    # this is really just an instance of print list, I don't need to test both right?
    donor = 'list'
    # we just want to make sure it loops back
    dono = 'bob'
    # should print the next piece?


donors_list = [
    "William Gates, III",
    "Mark Zuckerberg",
    "Jeff Bezos",
    "Paul Allen",
    "bob",
    "bill"
]


def test_list_donors(capsys):
    desc = 'donors'
    list_donors()
    captured = capsys.readouterr()
    assert('These are the donors currently in the database:' in captured.out)


def test_print_list(capsys):
    desc = 'descriptor'
    print_list(donors_list, desc)
    captured = capsys.readouterr()
    assert(desc in captured.out)
    for donor in donors_list:
        assert(donor in captured.out)


def test_donors_in_database():
    assert(donors_in_database(initial_donations) == donors_list)


donor = 'cary'
donation_amounts = [-5, 'cow', 300]
donations_raise = [ValueError, ValueError, False]


def test_new_doation_handler(capsys):
    for idx, donation in enumerate(donation_amounts):
        E = donations_raise[idx]
        if E:
            with pytest.raises(E):
                new_donation_handler(donor, donation)
        else:
            new_donation_handler(donor, donation)
            assert(last_donation(donor) == donation)
            captured = capsys.readouterr()
            assert donor in captured.out
            assert '$'+str(donation) in captured.out


def test_add_donation_to_database():
    for idx, donation in enumerate(donation_amounts):
        if donations_raise[idx]:
            with pytest.raises(ValueError):
                add_donation_to_database(donor, donation)
        else:
            add_donation_to_database(donor, donation)
            assert(last_donation(donor) == donation)


test_donations = {
    5.0935: [donor, '$5.09', 'Thank you'],
    50: [donor, '$50', 'Thank you'],
    5.1: [donor, '$5.10', 'Thank you'],
}


def test_thankyou_string():
    for test_donation, should_contain in test_donations.items():
        thx_str = thankyou_string(donor, test_donation)
        for string in should_contain:
            assert(string in thx_str)


def test_send_thank_you(capsys):
    test_string = 'test_string'
    send_thank_you(donor, 'test_string')
    captured = capsys.readouterr()
    assert(test_string in captured.out)
        # for string in should_contain:
        #    assert(string in captured.out)


donation_report_string = (
    "Donor name                | Total Given |  Num Gifts  |Average Gift \n"
    "____________________________________________________________________\n"
    "William Gates, III         $       15.00            3  $        5.00\n"
    "Mark Zuckerberg            $       14.50            3  $        4.83\n"
    "Paul Allen                 $        8.10            2  $        4.05\n"
    "Jeff Bezos                 $        7.77            1  $        7.77\n"
    "bob                        $        0.01            1  $        0.01\n"
    "bill                       $        0.00            0  $        0.00"
)


def test_create_donation_report():
    donation_report = create_donation_report(donations)
    assert(donation_report_string == donation_report)


def test_print_report(capsys):
    #fix this
    pass


def test_key1():
    assert(key1([1, 2, 3]) == 2)


def test_get_row():
    rows = {
        "William Gates, III": ("William Gates, III", 15, 3, 5),
        "Mark Zuckerberg": ("Mark Zuckerberg", 14.5, 3, 14.5/3),
        "Jeff Bezos": ("Jeff Bezos", 7.77, 1, 7.77),
        "Paul Allen": ("Paul Allen", 8.10, 2, 4.05),
        "bob": ("bob", .01, 1, .01),
        "bill": ("bill", 0, 0, 0)
    }
    for donor in donations:
        row = get_row(donor)
        assert(row == rows[donor])
        print(row)


def test_donations_from():
    for donor in donations:
        assert(donations_from(donor) == donations[donor])


def test_send_letters():
    filename_sufffix = 'test'
    send_letters(filename_sufffix)
    for donor in donations:
        test_name = "{}_{}.txt".format(donor, filename_sufffix)
        if donor == 'bill':
            assert(not(os.path.isfile(test_name)))
        else:
            with open(test_name, 'r') as letter_file:
                letter = letter_file.read()
                las_don = last_donations[donor]
                assert(letter == thankyou_string(donor, las_don))


def test_send_letter(capsys):
    send_letter('bill', 'test1.txt')
    captured = capsys.readouterr()
    assert("No thank you was saved for bill" in captured.out)
    test_name = 'test2.txt'
    donor = 'bob'
    send_letter('bob', test_name)
    with open(test_name, 'r') as letter_file:
        letter = letter_file.read()
        las_don = last_donations[donor]
        print(thankyou_string(donor, las_don))
        print(letter)
        assert(thankyou_string(donor, las_don) in letter)


last_donations = {
    "William Gates, III": 7,
    "Mark Zuckerberg": 2,
    "Jeff Bezos": 7.77,
    "Paul Allen": 4.5,
    "bob": .01,
    "bill": None
}


def test_last_donation():
    for donor in donations:
        assert(last_donation(donor) == last_donations[donor])


