from mailroom_part4 import *


def test_1():
    assert is_name_list('not_list') is False


def test_2():
    assert is_name_list('list') is True


def test_3():
    assert is_name_list('') is False


def test_4():
    assert is_name_existing({'donor_name': 'David Sedaris'}) is True


def test_5():
    assert is_name_existing({'donor_name': 'daVid sedaRiS'}) is True


def test_6():
    assert is_name_existing({'donor_name': 'Amy Sedaris'}) is False


def test_7():
    d = {'donor_name': 'David Sedaris', 'donation': 123.0}
    add_donation_to_existing(d)
    assert ddb['David Sedaris'] == [23000, 1200, 2000, 123.0]


def test_8():
    d = {'donor_name': 'New Donor', 'donation': 456.0}
    add_donation_to_new(d)
    assert ddb['New Donor'] == [456.0]


def test_9():
    d = {'donor_name': 'New Donor', 'donation': 456.0}
    letter = ('Dear New Donor,'
              '\n\n\tThank you for your generous gift of $456.00.'
              '\n\tYour contribution will keep 23 Fleebs floobing for an entire year.'
              '\n\tWe truly could not do this important work without you.'
              '\n\nSincerely,'
              '\nFleeb Freedom Now')

    assert create_letter(d) == letter


def test_10():
    assert generate_table_row('Test Name', [1, 23, 0]) == [('Test Name', '$24', '3', '$8.0')]


def test_11():
    dbd = {'Test Name 1': [1, 2, 3],
           'Test Name 2': [0],
           'Test Name 3': []}
    output = [("Donor Name", "Total Given", "Num Gifts", "Average Gift"),
              ('Test Name 1', '$6', '3', '$2.0'),
              ('Test Name 2', '$0', '1', '$0.0'),
              ('Test Name 3', '$0', '0', '$0')]
    assert create_report_table(dbd) == output


def test_12():
    tbl = [('this', 'that', 'the other'), (1, 2, 123456789), ('the longest string', 'srt', 's')]
    assert max_column_width(tbl) == [18, 4, 9]


def test_13():
    assert add_column_spaces([1, 2, 3], spaces=2) == [3, 4, 5]


def test_14():
    assert create_report_formstring([1, 2, 3]) == '{:1}{:2}{:3}'


def test_15():
    write_letters({'New Donor': [1, 2, 456]})

    letter = ('Dear New Donor,'
              '\n\n\tThank you for your generous gift of $456.00.'
              '\n\tYour contribution will keep 23 Fleebs floobing for an entire year.'
              '\n\tWe truly could not do this important work without you.'
              '\n\nSincerely,'
              '\nFleeb Freedom Now')

    with open('New_Donor.txt', 'r') as f:
        assert f.read() == letter
