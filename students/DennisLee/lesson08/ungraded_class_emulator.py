#!/usr/bin/env python3


# import numpy
# import operator

class SparseArray():

    def __init__(self, seq=None):
        self.val_dict, self.length = {}, 0
        if seq:
            self.append(seq)

    def __str__(self):
        return str(self.__iter__())

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if isinstance(key, slice):
            final_slice = []
            (start, stop, step) = key.indices(self.length)
            for i in range(start, stop, step):
                final_slice.append(self.__getitem__(i))
            return final_slice[:]
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
            elif key in self.val_dict.keys():
                del self.val_dict[key]

    def __delitem__(self, key):
        if isinstance(key, slice):
            (start, stop, step) = key.indices(self.length)
            items_to_delete = [i for i in range(start, stop, step)]
            # Make sure we delete going backward, or else subsequent
            # deletion indices will be incorrect
            if items_to_delete[0] < items_to_delete[-1]:
                direction = -1
            else:
                direction = 1
            for i in items_to_delete[::direction]:
                self.__delitem__(i)
        elif isinstance(key, tuple):
            pass
        else:
            key = self.test_key(key)
            if key in self.val_dict.keys():
                del self.val_dict[key]
            for i in range(key, self.length-1):
                if i in self.val_dict.keys():
                    del self.val_dict[i]
                self.__setitem__(i, self.__getitem__(i+1))
            self.length -= 1
            
    def __iter__(self):
        return [self.__getitem__(x) for x in range(self.length)]

    def __reversed__(self):
        return self.__iter__()[::-1]

    def __contains__(self, item):
        return (item in self.__iter__())

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


    


if __name__ == "__main__":
    array_to_add = [0,0,0,32,56,0,423,0,0,0,0,0,0,46,0,54,66,0]
    sa = SparseArray(array_to_add)
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    print("Array sa reversed is:", reversed(sa))
    sa[2] = 88
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    print("7th member of sa array is:", sa[6])
    print("10th member of sa array is:", sa[9])
    print("Last four members of sa are:", sa[-4:])
    sa.append(0)
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    sa.append(3)
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    sa.append([0,0,35,97,0,0,68,0,0])
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    del sa[4]
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    del sa[15:19]
    print("Array sa now has {0} numbers: {1}".format(len(sa), sa))
    print("Array sa contains 5? ", 5 in sa)
    print("Array sa contains 423? ", 423 in sa)
    print("Array sa contains 0? ", 0 in sa)

    sa2 = SparseArray()
    print("Array sa2 now has {0} numbers: {1}".format(len(sa2), sa2))
    sa2.append([0,0,35,58,0,0])
    print("Array sa2 now has {0} numbers: {1}".format(len(sa2), sa2))
    del sa2[0:]
    print("Array sa2 now has {0} numbers: {1}".format(len(sa2), sa2))
    sa2.append(5)
    print("Array sa2 now has {0} numbers: {1}".format(len(sa2), sa2))
