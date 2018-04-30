import sparse_array as sa


class SparseArrayTest(unittest.TestCase):
    """tests sparse array attributes"""

    def setUp(self):
        self.test = sa.SparseArray()

    def test_sa(self):
        self.assertEqual(self.test(range(5)), [1, 2, 3, 4])
