#!/usr/bin/env python3
'''A sparse array class should present to the user the same interface as a regular list.

Some ideas of how to do that:

Internally, it can store the values in a dict,
with the index as the keys, so that only the indexes
with non-zero values will be stored.
It should take a sequence of values as an initializer:
sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
you should be able to tell how long it is:
  len(my_array)

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
'''


class SparseArray:

    def __init__(self, sequence):
        self.seq_length = len(sequence)
        self.sparse_dict = {index: item for index,
                            item in enumerate(sequence) if item}

    def __getitem__(self, index):

        if isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.seq_length
            step = index.step if index.step is not None else 1

            return [self.sparse_dict.get(index, 0) for index in range(start, stop, step)]
        elif index >= self.seq_length or index < 0:
            raise IndexError
        else:
            return self.sparse_dict.get(index, 0)

    def __setitem__(self, index, value):
        """ sets the value at the given index of the array"""
        self.sparse_dict[index] = value

    def __len__(self):
        """ Returns the length of the array"""
        return self.seq_length

    def __delitem__(self, index):
        """Delete Item from sparsearray - with test catch"""
        if index >= self.seq_length or index < 0:
            raise IndexError
        else:
            try:
                del self.sparse_dict[index]
            except KeyError:
                pass

        # Rebuild dict after deleting the element
        self.sparse_dict = {(i - 1 if i > index else i): item
                            for i, item in self.sparse_dict.items()}
        # sets the length
        self.seq_length -= 1

    def append(self, value):
        """Add element to sequence/sparse array"""
        self.sparse_dict[self.seq_length] = value
        self.seq_length += 1
