#!/usr/bin/python


class SparseArray():
    _varray = {}

    def __init__(self, sequence):
        if type(sequence) == list:
            self.create_dict(sequence)
        else:
            raise TypeError("Input must be a list")
        self._length = len(sequence)

    def __getitem__(self, item_number):
        if item_number >= self._length:
            raise IndexError("item index out of bounds")
        elif item_number in self._varray:
            return(self._varray[item_number])
        else:
            return 0

    def __setitem__(self, item_number, data):
        self.append(data, item_number)

    def __len__(self):
        return self._length

    def __delitem__(self, key):
        if key in self._varray:
            del self._varray[key]

        if key < self._length:
            for i in range(key, self._length):
                if i in self._varray:
                    self.append(self._varray[i], i - 1)
                    del self._varray[i]
            self._length -= 1

    def create_dict(self, sequence):
        for i, elem in enumerate(sequence):
            if elem != 0:
                self._varray[i] = elem

    def append(self, data, item_number=None):

        if item_number is None:
            if data:
                self._varray[self._length] = data
            self._length += 1

        elif item_number in self._varray:
            if data:
                self._varray[item_number] = data
            else:
                self._varray.pop(item_number)

        elif item_number == self._length:
            self.append(data)

        elif item_number < self._length:
            if data:
                self._varray[item_number] = data

        else:
            raise IndexError("item index out of bounds")


