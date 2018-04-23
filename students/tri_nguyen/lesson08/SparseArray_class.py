class SparseArray:
    def __init__(self, array):
        self.array = array
        self.non_zeros = {idx: item for idx, item in enumerate(self.array) if item != 0}

    def __len__(self):
        return len(self.array)

    def __getitem__(self, idx):
        try:
            return self.array[idx]
        except IndexError:
            print(idx, 'is out of range.')
        except TypeError:
            print(idx, 'is not integers or slices.')

    def __setitem__(self, idx, value):
        try:
            self.array[idx] = value
        except IndexError as err:
            print(err)
        except TypeError as err:
            print(err)

    def append(self, value):
        if isinstance(value, int):
            self.array.append(value)
            self.non_zeros = {idx: item for idx, item in enumerate(self.array) if item != 0}

    def __delitem__(self, idx):
        try:
            del self.array[idx]
        except TypeError as err:
            print(err)


if __name__ == '__main__':
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
    print('there are', len(sa), 'items')
    print('\nindexing:',sa[6], '\n')
    print(sa.array, '\n')
    print('slicing:', sa[1:9])
    print(sa[34])