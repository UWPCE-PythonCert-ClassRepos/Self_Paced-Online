import unittest
from sparse_array import SparseArray

class TestSparseArray(unittest.TestCase):

    #def __init__(self):
    #    self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )

    def test_get(self):
        self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
        assert self.sa[4] == 2

    def test_splice(self):
        self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
        assert self.sa[2:5] == (0,0,2)

    def test_set(self):
        self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
        self.sa[6] = 9
        assert self.sa[6] == 9

    def test_append(self):
        self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
        self.sa.append(7)
        assert self.sa[:] == (1,0,0,0,2,0,0,0,5,7) 

    def test_del(self):
        self.sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
        del(self.sa[0])
        assert self.sa[:] == (0,0,0,2,0,9,0,5)        

if __name__ == '__main__':
    unittest.main() 
