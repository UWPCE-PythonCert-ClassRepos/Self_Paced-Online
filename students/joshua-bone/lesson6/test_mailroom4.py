import io
from contextlib import redirect_stdout
from mailroom4 import *

TY_LETTER = ("Dear {full_name},",
             "",
             "\tThank you for your very kind donation{s} of {amounts}.",
             "",
             "\t{it_they} will be put to very good use.",
             "",
             "\t\tSincerely,",
             "\t\t\t-The Team")


def test_display():
    INPUT = ("Line 1", "\tLine 2", "Line 3")
    OUTPUT = ("-" * 80 + "\n" +
              "Line 1\n" +
              "\tLine 2\n" +
              "Line 3\n")

    capture = io.StringIO()
    with redirect_stdout(capture):
        display(INPUT)

    assert capture.getvalue() == OUTPUT


def test_dollar_string():
    assert dollar_string(123.456) == "$123.46"


def test_add_gift():
    donor_list = defaultdict(list)

    add_gift("Test Donor", 123.45, donors=donor_list)
    add_gift("Test Donor", 234.56, donors=donor_list)

    assert donor_list["Test Donor"] == [123.45, 234.56]


def test_report_header():
    ten_char_name = "AAAAABBBBB"

    actual = report_header(donors={ten_char_name: [123.45]}, width=13)

    expected = "Donor Name     |  Total Given |    Num Gifts | Average Gift"
    assert expected == actual


def test_report_body():
    donor_list = {"AAAAABBBBB": [1.0, 2.0, 3.0],
                  "CCCCCDDD": [10.0, 20.0, 30.0]}

    actual = sorted_report_body(width=8, donors=donor_list)

    expected = [
        "CCCCCDDD       |  $60.00 |       3 |  $20.00",
        "AAAAABBBBB     |   $6.00 |       3 |   $2.00"
    ]
    assert expected == actual


def test_display_report():
    donor_list = {"AAAAABBBBB": [1.0, 2.0, 3.0],
                  "CCCCCDDD": [10.0, 20.0, 30.0]}
    OUTPUT = ("-" * 80 + "\n" +
              "Donor Name     |  Total Given |    Num Gifts | Average Gift\n" +
              "-" * 80 + "\n" +
              "CCCCCDDD       |       $60.00 |            3 |       $20.00\n" +
              "AAAAABBBBB     |        $6.00 |            3 |        $2.00\n")

    capture = io.StringIO()
    with redirect_stdout(capture):
        display_report(donors=donor_list, width=13)

    assert capture.getvalue() == OUTPUT


def test_format_amts_one_entry():
    res = format_amts([6.666])

    assert res == "$6.67"


def test_format_amts_multiple_entries():
    res = format_amts([1.111, 4.444, 9.999])

    assert res == "$1.11, $4.44, and $10.00"


def test_format_ty_one_entry():
    name = "TEST NAME"
    amts = [6.666]

    res = format_ty(name, amts, letter=TY_LETTER)
    assert res == ["Dear TEST NAME,",
                   "",
                   "\tThank you for your very kind donation of $6.67.",
                   "",
                   "\tIt will be put to very good use.",
                   "",
                   "\t\tSincerely,",
                   "\t\t\t-The Team"]


def test_format_ty_multiple_entries():
    name = "TEST NAME"
    amts = [1.111, 4.444, 9.999]

    res = format_ty(name, amts, letter=TY_LETTER)
    assert res == ["Dear TEST NAME,",
                   "",
                   ("\tThank you for your very kind donations of " +
                    "$1.11, $4.44, and $10.00."),
                   "",
                   "\tThey will be put to very good use.",
                   "",
                   "\t\tSincerely,",
                   "\t\t\t-The Team"]


def test_display_donors():
    donor_list = {"AAAAABBBBB": [1.0, 2.0, 3.0],
                  "CCCCCDDD": [10.0, 20.0, 30.0]}

    capture = io.StringIO()
    with redirect_stdout(capture):
        display_donors(donors=donor_list)

    expected = "-" * 80 + "\nExisting Donors:\n\nAAAAABBBBB\nCCCCCDDD\n"
    assert capture.getvalue() == expected
