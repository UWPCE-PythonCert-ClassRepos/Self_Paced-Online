import sparse_array as sa
import unittest


class SATest(unittest.TestCase):
    """tests sparse array attributes"""

    def setUp(self):
        self.test = sa.SA((4, 3, 0, 7, 0, 8, 2, 9, 0, 4))

    def test_sa(self):
        print('self.test.seq is', self.test.seq)
        print('self.test.seq_d is', self.test.seq_d)
        print('self.test.make_arr() makes', self.test.make_arr())
        self.assertEqual(self.test.make_arr(), [4, 3, 7, 8, 2, 9, 4])

    def test_sa_len(self):
        self.assertEqual(self.test.get_seq_len(), 10)

    def test_sa_index(self):
        self.assertEqual(self.test.__getitem__(self.test.seq, 3), 7)
