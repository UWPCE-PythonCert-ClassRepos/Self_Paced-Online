#!/usr/bin/env python3
"""Sparse Array Module"""


class SparseArray():
    """Sparse Array class"""
    def __init__(self, seq):
        self.elements = {}
        self.num_elems = 0

        for i, arg in enumerate(seq):
            self.num_elems += 1
            self.elements[i] = arg

    def __contains__(self, item):
        return bool(item in self.elements.values())

    def __delitem__(self, index):
        if index in self.elements.keys():
            del self.elements[index]
            self.num_elems -= 1

            # Rebuild dict after deleted element
            for i in range(index, self.num_elems):
                self.elements[i] = self.elements[i + 1]
            del self.elements[self.num_elems]
        else:
            raise IndexError

    def __getitem__(self, index):
        try:
            if isinstance(index, slice):
                beg = index.start if index.start is not None else 0
                end = index.stop if index.stop is not None else self.num_elems
                stp = index.step if index.step is not None else 1
                return [self.elements[i] for i in range(beg, end, stp)]
            else:
                return self.elements[index]
        except KeyError:
            raise IndexError

    def __iter__(self):
        for i in range(0, self.num_elems):
            yield self.elements[i]

    def __len__(self):
        return self.num_elems

    def __lt__(self, seq):
        return bool(self.num_elems < len(seq))

    def __setitem__(self, index, value):
        if index < self.num_elems:
            self.elements[index] = value
        else:
            raise IndexError

    def __str__(self):
        return '[' + ', '.join([str(self.elements[i]) for i in range(self.num_elems)]) + ']'

    def __repr__(self):
        return f'SparseArray(*args)'

    def append(self, elem):
        self.elements[self.num_elems] = elem
        self.num_elems += 1


def main():
    """Main function"""
    pass


if __name__ == '__main__':
    main()
