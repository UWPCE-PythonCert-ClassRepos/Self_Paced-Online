from mailroom_pt4 import report

#test mailroom functions using pytest


def test_report():
    actual = report()
    expected = (
        "-------------------- REPORT --------------------\n"
        "Donor Name         | Total Given    | Num Gifts| Average Gift\n"
        "---------------------------------------------------------------\n"
        "Christiaan Huygens   $      9174.00           2  $   4587.00\n"
        "Galileo Galilei      $      8848.00           3  $   2949.33\n"
        "Edwin Hubble         $      1899.00           1  $   1899.00\n"
        "Edmond Halley        $      1856.00           3  $    618.67\n"
        "Giovanni Cassini     $       209.00           1  $    209.00\n")

        
    assert expected == actual
    