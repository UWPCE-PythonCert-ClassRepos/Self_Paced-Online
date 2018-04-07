#!/usr/bin/env python3
"""Unit Tests for Sparse Array"""

import unittest
import random
import sparse_array as sa


class TestSparseArray(unittest.TestCase):
    """Test class containing all unit tests for Sparse Array"""
    test_seq = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4]
    test_seq2 = [1, 2, 3, 4, 5]
    test_seq_str = str(test_seq)
    test_seq_first_zero_index = 2
    test_seq_first_nonzero_index = 0

    def setUp(self):
        self.array = sa.SparseArray(self.test_seq)

    def tearDown(self):
        pass

    def test_contains(self):
        self.assertTrue(1 in self.array)
        self.assertTrue(0 in self.array)

    def test_delete_outside_index(self):
        with self.assertRaises(IndexError):
            del self.array[self.array.num_elems + 1]
        with self.assertRaises(IndexError):
            del self.array[-1]

    def test_delete_zero(self):
        del self.array[self.test_seq_first_zero_index]
        self.assertTrue(self.array == [1, 2, 0, 0, 0, 3, 0, 0, 4],
                        msg=self.array)

    def test_delete_nonzero(self):
        del self.array[self.test_seq_first_nonzero_index]
        self.assertTrue(self.array == [2, 0, 0, 0, 0, 3, 0, 0, 4],
                        msg=self.array)

    def test_equality(self):
        self.assertTrue(self.array == self.test_seq)

    def test_get_item_outside_index(self):
        with self.assertRaises(IndexError):
            _ = self.array[self.array.num_elems + 1]
        with self.assertRaises(IndexError):
            _ = self.array[-1]

    def test_get_item(self):
        for i, val in enumerate(self.test_seq):
            self.assertTrue(val == self.array[i])

    def test_get_slice(self):
        for i in range(len(self.test_seq)):
            for j in range(len(self.test_seq)):
                self.assertTrue(self.test_seq[i:j] == self.array[i:j])

    def test_iter(self):
        for i, val in enumerate(self.array):
            self.assertTrue(self.test_seq[i] == val)

    def test_len(self):
        self.assertTrue(len(self.test_seq) == len(self.array))

    def test_less_than(self):
        self.assertFalse(self.array < self.test_seq)

    def test_set_item_outside_index(self):
        with self.assertRaises(IndexError):
            self.array[self.array.num_elems + 1] = 4
        with self.assertRaises(IndexError):
            self.array[-1] = 4

    def test_set_item_to_zero(self):
        test_zero_list = [0 for _ in range(len(self.test_seq))]
        for i in range(len(self.test_seq)):
            self.array[i] = 0
            self.assertTrue(self.array[i] == 0)

        self.assertTrue(self.array == test_zero_list)

    def test_set_item_to_nonzero(self):
        test_list = [i + 1 for i in range(len(self.test_seq))]
        for i in range(len(self.test_seq)):
            self.array[i] = i + 1
            self.assertTrue(self.array[i] == i + 1)

        self.assertTrue(self.array == test_list)

    def test_str(self):
        self.assertTrue(str(self.array) == self.test_seq_str)

    def test_repr(self):
        self.assertTrue(repr(self.array) == 'SparseArray(*args)')

    def test_append_random(self):
        random_list = random.sample(range(100), 50)
        self.array = sa.SparseArray([])

        for i, val in enumerate(random_list):
            self.array.append(val)
            self.assertTrue(self.array[i] == random_list[i],
                            msg=(self.array, self.test_seq))

        self.assertTrue(self.array == random_list)

    def test_append_zeros(self):
        test_append_list = self.test_seq[:]
        for _ in range(50):
            self.array.append(0)
            test_append_list.append(0)

        self.assertTrue(self.array == test_append_list)


if __name__ == '__main__':
    unittest.main()
