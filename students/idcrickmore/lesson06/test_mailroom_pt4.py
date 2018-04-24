from operator import itemgetter
from mailroom_pt4 import report

#test mailroom functions using pytest

donors = {
          "Galileo Galilei": [348, 8377, 123],
          "Giovanni Cassini": [209],
          "Christiaan Huygens": [9135, 39],
          "Edmond Halley": [399, 1100, 357],
          "Edwin Hubble": [1899]
          }
    
def test_report():
    assert report() is '\n-------------------- REPORT --------------------\n\nDonor Name         | Total Given    | Num Gifts| Average Gift\n---------------------------------------------------------------\nChristiaan Huygens   $      9174.00           2  $   4587.00\nGalileo Galilei      $      8848.00           3  $   2949.33\nEdwin Hubble         $      1899.00           1  $   1899.00
\nEdmond Halley        $      1856.00           3  $    618.67\nGiovanni Cassini     $       209.00           1  $    209.00\n'

