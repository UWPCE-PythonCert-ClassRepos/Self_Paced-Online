from mailroom_pt4 import report, letters, donor_list
import os

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
    
    
def test_letters():
    assert os.path.isfile('Giovanni Cassini_2018-04-30.txt')
    assert os.path.isfile('Edmond Halley_2018-04-30.txt')
    assert os.path.isfile('Edwin Hubble_2018-04-30.txt')
    assert os.path.isfile('Galileo Galilei_2018-04-30.txt')
    assert os.path.isfile('Christiaan Huygens_2018-04-30.txt')
    

def test_list():
    actual = donor_list()
    expected = ['Galileo Galilei',
                'Giovanni Cassini',
                'Christiaan Huygens',
                'Edmond Halley',
                'Edwin Hubble']
                
    assert expected == actual
