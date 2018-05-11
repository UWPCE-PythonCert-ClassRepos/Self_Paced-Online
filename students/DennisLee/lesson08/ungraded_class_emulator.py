#!/usr/bin/env python3


class SparseArray():

    val_dict, length = {}, 0

    def __init__(self, seq):
        self.append(seq)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if isinstance(key, slice):
            final_slice = []
            (start, stop, step) = key.indices(self.length)
            for i in range(start, stop, step):
                final_slice.append(self.__getitem__(i))
            return final_slice
        elif isinstance(key, tuple):
            pass
        else:
            key = self.test_key(key)
            if key in self.val_dict.keys():
                return self.val_dict[key]
            else:
                return 0

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            (start, stop, step) = key.indices(self.length)
            for i, j in zip(range(start, stop, step), value):
                self.__setitem__(i, j)
        elif isinstance(key, tuple):
            pass
        else:
            key = self.test_key(key)
            if value:
                self.val_dict[key] = value
            else:
                del self.val_dict[key]

    def __delitem__(self, key):
        if isinstance(key, slice):
            (start, stop, step) = key.indices(self.length)
            if start < stop:  # Make sure we delete going backward
                start, stop, step = stop - 1, start - 1, -step
            for i in range(start, stop, step):
                self.__delitem__(i)
        elif isinstance(key, tuple):
            pass
        else:
            key = self.test_key(key)
            if key == self.length - 1:
                del self.val_dict[key]
            else:
                for i in range(key, self.length-1):
                    if key in self.val_dict.keys():
                        del self.val_dict[i]
                        self.__setitem__(i, self.val_dict[i+1])
            self.length -= 1
            
    def __iter__(self):
        return [self.__getitem__(x) for x in range(self.length)]

    def __reversed__(self):
        return self.__iter__()[::-1]

    def __contains__(self, item):
        return (item in self.val_dict.values())

    def append(self, val):
        if isinstance(val, list):
            for i in val:
                self.append(i)
        elif isinstance(val, tuple):
            pass
        else:
            if val:
                self.val_dict[self.length] = val
            self.length += 1

    def test_key(self, key):
        if key not in range(-self.length, self.length):
            raise IndexError(f"Index {key} out of range - array is only "
                    f"{self.length} items long.")
        if key < 0:
            key += self.length
        return key
