#!/usr/bin/env python3
"""Sparse Array Module"""


class SparseArray:
    """Sparse Array class"""
    def __init__(self, seq):
        self.contains_zero = True if 0 in seq else False
        self.elements = {i: arg for i, arg in enumerate(seq) if arg}
        self.num_elems = len(seq)

    def __contains__(self, item):
        if not item:
            return self.contains_zero
        return item in self.elements.values()

    def __delitem__(self, index):
        if index >= self.num_elems or index < 0:
            raise IndexError
        else:
            try:
                del self.elements[index]
            except KeyError:
                pass

            # Rebuild dict after deleted element
            self.elements = {(i - 1 if i > index else i): arg
                             for i, arg in self.elements.items()}
            self.num_elems -= 1

    def __eq__(self, other):
        for i in range(self.num_elems):
            if i in self.elements.keys():
                if self.elements[i] != other[i]:
                    return False
            elif other[i] != 0:
                return False

        return True

    def __getitem__(self, index):
        if isinstance(index, slice):
            strt = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.num_elems
            step = index.step if index.step is not None else 1

            return [self.elements.get(i, 0) for i in range(strt, stop, step)]
        elif index >= self.num_elems or index < 0:
            raise IndexError
        else:
            return self.elements.get(index, 0)

    def __iter__(self):
        for i in range(self.num_elems):
            yield self.elements.get(i, 0)

    def __len__(self):
        return self.num_elems

    def __lt__(self, seq):
        return self.num_elems < len(seq)

    def __setitem__(self, index, value):
        if index >= self.num_elems or index < 0:
            raise IndexError
        elif not value:
            try:
                del self.elements[index]
            except KeyError:
                pass
        else:
            self.elements[index] = value

    def __str__(self):
        elems = [str(self.elements.get(i, 0)) for i in range(self.num_elems)]
        return '[' + ', '.join(elems) + ']'

    def __repr__(self):
        return f'SparseArray(*args)'

    def append(self, elem):
        """Appends elem to end of array"""
        self.elements[self.num_elems] = elem
        self.num_elems += 1
