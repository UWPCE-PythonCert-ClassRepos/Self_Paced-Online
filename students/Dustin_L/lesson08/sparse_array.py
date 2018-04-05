#!/usr/bin/env python3
"""Sparse Array Module"""


class SparseArray():
    """Sparse Array class"""
    def __init__(self, seq):
        self.num_elems = 0
        self.elements = {}

        self.elements = {i: arg for i, arg in enumerate(seq) if arg}
        self.num_elems = len(seq)

    def __contains__(self, item):
        return bool(item in self.elements.values())

    def __delitem__(self, index):
        if index >= self.num_elems or index < 0:
            raise IndexError
        else:
            try:
                del self.elements[index]
            except ValueError:
                raise IndexError
            except KeyError:
                pass
            else:
                self.num_elems -= 1

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
        for i in range(0, self.num_elems):
            yield self.elements[i]

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
