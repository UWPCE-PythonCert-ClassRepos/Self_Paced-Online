from mailroom_pt4 import report

#test mailroom functions using pytest

    
def test_report():
    actual = report()
    expected = """-------------------- REPORT --------------------
Donor Name         | Total Given    | Num Gifts| Average Gift
---------------------------------------------------------------
Christiaan Huygens   $      9174.00           2  $   4587.00
Galileo Galilei      $      8848.00           3  $   2949.33
Edwin Hubble         $      1899.00           1  $   1899.00
Edmond Halley        $      1856.00           3  $    618.67
Giovanni Cassini     $       209.00           1  $    209.00

"""

    assert expected == actual
    