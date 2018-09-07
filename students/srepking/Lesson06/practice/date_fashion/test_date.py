import unittest
from date import date_fashion


class test_date(unittest.TestCase):

    def test_date1(self):
        assert date_fashion(2,2) == 0

    def test_date2(self):
        assert date_fashion(1,9) == 0

    def test_date3(self):
        assert date_fashion(5,5) == 1

    def test_date4(self):
        assert date_fashion(8,5) == 2


    def test_date5(self):
        assert date_fashion(8,1) == 0


if __name__ == '__main__':
    unittest.main()