
class SparseArray(list):


    def __init__(self, sparse_array):
        self.sparse_dict = {}
        self.array_length = 0
        for item in sparse_array:
            self.sparse_dict[self.array_length] = item
            self.array_length += 1


    def __getitem__(self, index):
        """ overrides list get and splice methods """
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.sparse_dict.keys()) if index.stop is None else index.stop
            if index.step is None:
                return [self.sparse_dict[i] for i in range(start, stop)]
            else:
                return [self.sparse_dict[i] for i in range(start, stop, index.step)]
        else:
            return self.sparse_dict[index]

    def __setitem__(self, index, value):
        """ overrides list set method """
        self.sparse_dict[index] = value

    def __len__(self):
        """ overrides list len method """
        return self.array_length
    
    def __delitem__(self, index):
        """ overrides list del method """
        del(self.sparse_dict[index])

        #rebuild dict with new keys
        new_dict = {}
        self.array_length = 0
        for k in sorted(self.sparse_dict.keys()):
            new_dict[self.array_length] = self.sparse_dict[k]
            self.array_length += 1
        self.sparse_dict = new_dict

    def append(self,value):
        """ override list append method """
        self.sparse_dict[self.array_length] = value
        self.array_length += 1


