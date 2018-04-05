#!/usr/bin/env python3
"""Sparse Array Module"""


class SparseArray():
    """Sparse Array class"""
    def __init__(self, seq):
        self.num_elems = 0
        self.elements = {}

        self.contains_zero = True if 0 in seq else False
        self.elements = {i: arg for i, arg in enumerate(seq) if arg}
        self.num_elems = len(seq)

    def __contains__(self, item):
        if not item:
            return self.contains_zero
        return bool(item in self.elements.values())

    def __delitem__(self, index):
        if index >= self.num_elems or index < 0:
            raise IndexError
        else:
            try:
                del self.elements[index]
            except KeyError:
                pass

            # Rebuild dict after deleted element
            # NOTE: Can this be done with a dictionary comprehension??
            new_dict = {}
            for i, arg in self.elements.items():
                if i > index:
                    new_dict[i - 1] = arg
                else:
                    new_dict[i] = arg

            self.elements = new_dict
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

            ret_lst = []
            for i in range(strt, stop, step):
                if i in self.elements.keys():
                    ret_lst.append(self.elements[i])
                else:
                    ret_lst.append(0)

            return ret_lst
        else:
            if index >= self.num_elems or index < 0:
                raise IndexError
            elif index in self.elements.keys():
                return self.elements[index]
            return 0

    def __iter__(self):
        for i in range(self.num_elems):
            if i in self.elements.keys():
                yield self.elements[i]
            else:
                yield 0

    def __len__(self):
        return self.num_elems

    def __lt__(self, seq):
        return bool(self.num_elems < len(seq))

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
        elems = []
        for i in range(self.num_elems):
            if i in self.elements.keys():
                elems.append(str(self.elements[i]))
            else:
                elems.append('0')

        return '[' + ', '.join(elems) + ']'

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
