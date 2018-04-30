import sparse_array as sa
import unittest


class SATest(unittest.TestCase):
    """tests sparse array attributes"""

    def setUp(self):
        self.test = sa.SA((4, 3, 0, 7, 0, 8, 2, 9, 0))

    def test_sa(self):
        self.assertEqual(self.test.make_array(), str([4, 3, 7, 8, 2, 9]))
