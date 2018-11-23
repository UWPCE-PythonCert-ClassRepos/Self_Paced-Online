class SparseArray:
    def __init__(self, array):
        """"Take in an array and only store non-zero values"""
        self.sparse_array={}
        for i, v in enumerate(array):
            if array[i] > 0:
                self.sparse_array[i] = v

        self._length = len(array)

    def __getitem__(self, index):
        if index > int(self._length):
            raise IndexError('Trying to access an index beyond area')
        elif index in self.sparse_array:
            return self.sparse_array[index]
        else:
            return 0
    def __len__(self):
        """THis will give the arrays virtual length---with zeros"""
        return self._length

    def __setitem__(self, key, value):
        if key <= int(self._length) and value != 0:
            self.sparse_array[key]=value
            return self.sparse_array[key]
        else:
            raise ValueError('Attempting to reassign non-existent element')

    def __delitem__(self, key):
        self.sparse_array.__delitem__(key)
        for i, value in self.sparse_array.items():
            if i > key:
                self.sparse_array.__delitem__(i)
                self.sparse_array[i-1]= value
        self._length-=1





if __name__ == "__main__":

    ex = SparseArray([2, 3, 4, 5, 0, 0, 6, 7, 0, 0, 0])

    print('The 3rd index is: ')
    print(ex[3])

    print('The length is:')
    print(len(ex))
