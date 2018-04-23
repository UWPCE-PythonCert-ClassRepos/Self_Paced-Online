"""
Sparse Array Activity
A sparse array class should present to the user the same interface as a regular list.
Internally, it can store the values in a dict, with the index as the keys, so that only the indexes with non-zero values will be stored.

It should take a sequence of values as an initializer:
sa = SparseArray([1,2,0,0,0,0,3,0,0,4])

You should be able to tell how long it is: len(my_array)
This will give its "virtual" length --  with the zeros

It should support getting and setting particular elements via indexing:
sa[5] = 12
sa[3] = 0 # the zero won't get stored!
val = sa[13] # it should get a zero if not set

It should support deleting an element by index:
del sa[4]

It should raise an IndexError if you try to access an index beyond the end.
it should have an append() method.
Can you make it support slicing?
How else can you make it like a list?
In [10]: my_array = SparseArray( (1,0,0,0,2,0,0,0,5) )
In [11]: my_array[4]
Out[11]: 2
In [12]: my_array[2]
Out[12]: 0
"""
from collections import defaultdict


class SparseArray:
    _dict = defaultdict(int)
    def __init__(self, iterable):
        for x in range(len(iterable)):
            if iterable[x] != 0:
                self._dict[x] = iterable[x]
    
    def __len__(self):
        return max(self._dict.keys())+1

    def __getitem__(self, key):
        if isinstance(key, slice):
            cake = []
            for x in range(len(self)):
                if x not in self._dict.keys():
                    cake.append(0)
                else:
                    cake.append(self._dict[x])
            return cake[key]
        if key not in range(len(self)):
            raise IndexError("The given index is out of range")
        elif key not in self._dict.keys():
            return 0
        else:
            return self._dict[key]

    def __setitem__(self, key, val):
        if key not in range(len(self)):
            raise IndexError("The given index is out of range")
        else:
            self._dict[key] = val

    def __delitem__(self, key):
       if key not in range(len(self)):
            raise IndexError("The given index is out of range")
       elif key in self._dict.keys():
           del self._dict[key]

    def __call__(self):
        nice_list = []
        for x in range(len(self)):
            nice_list[x] = self[x]
        return nice_list

    def append(self, val):
        self._dict[len(self)] = val
