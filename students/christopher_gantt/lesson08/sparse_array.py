#!/usr/bin/env python3

'''
Sparse Array Exercise
Lesson 8
'''

class NonSparseArray:
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)
   
    #supports indexing the array ie. sa[0]
    def __getitem__(self, i):
        return self.array[i]

    #supports setting array values ie. sa[0]=12
    def __setitem__(self, index, value):
        self.array[index] = value

    #supports deleting array values by index ie. del sa[0]
    def __delitem__(self, index):
        if index > len(self.array)-1:
            raise IndexError ("Index out of list range")
        else:   
            del self.array[index]

    def append(self, value):
        self.array.append(value)


class SparseArray:
    def __init__(self, array):
        self.array = {}
        for num in array:
            if num == 0:
                continue
            else:
                self.array[array.index(num)] = num

    def __repr__(self):
        return repr(self.array)

    def __len__(self):
        return max(self.array)+1

    def __getitem__(self, i):
        display_array = []
        if isinstance(i, slice):
            print(i.start, i.stop)
            for num in range(i.start, i.stop):
                if num in self.array:
                    display_array.append(self.array[num])
                else:
                    display_array.append(0)
            return display_array
        else:
            try:
                return self.array[i]
            except KeyError:
                return 0

    def __setitem__(self, index, value):
        if value == 0:
            del self.array[index]
        else:
            self.array[index] = value

    def __delitem__(self, index):
        if index > max(self.array) + 1:
            raise IndexError ("index exceeds array length")

        try:
            del self.array[index]
        except KeyError:
           print("You've deleted a zero")

        temp_array = {}
        for key, value in self.array.items():
            if key >= index:
                temp_array[key-1] = value
        self.array = temp_array
        del temp_array

    def append(self, value):
        self.array[max(self.array)+1] = value


if __name__ == '__main__':
    #sa = NonSparseArray([1,2,0,0,0,0,3,0,0,4])
    d = SparseArray([1,2,0,0,0,0,3,0,0,4])
