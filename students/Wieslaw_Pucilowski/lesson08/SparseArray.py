from collections import defaultdict

__author__ = "Wieslaw Pucilowski"

# can't drop 0 from the list, since no dict.keys() for zero
# could convert dict to list, drop from list and convert back to dict,
# but dict keys must be reordered after zero dropped, otherwise nothing changed


class SparseArray:
    def __init__(self, seq):
        self._dict = defaultdict(int)
        for x in range(len(seq)):
            if seq[x] != 0:
                self._dict[x] = seq[x]

    def __len__(self):
        return(max(self._dict.keys()) + 1)

    def __setitem__(self, key, val):
        if key not in range(len(self)):
            raise IndexError("Key out of range 0.." + str(len(self) - 1))
        elif val != 0:
            self._dict[key] = val

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = 0 if key.start is None else key.start
            stop = len(self)-1 if key.stop is None else key.stop
            if key.step is None:
                return [self.__getitem__(i) for i in range(start, stop)]
            else:
                return [self.__getitem__(i) for i in range(start, stop, key.step)]
        elif key not in range(len(self)):
            raise IndexError("Key out of range 0.." + str(len(self) - 1))
        elif key in self._dict.keys():
            return self._dict[key]
        else:
            return 0

    def __delitem__(self, key):
        if key not in range(len(self)):
            raise IndexError("Key out of range 0.." + str(len(self) - 1))
        elif key in self._dict.keys():
            del self._dict[key]

    def append(self, val):
        self._dict[len(self)] = val
