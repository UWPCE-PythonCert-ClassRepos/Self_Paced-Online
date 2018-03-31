
class SparseArray(list):

    #_max_index = 0
    #_sparse_dict = {}

    #@property
    #def max_index(self):
    #    return _max_index

    def __init__(self, sparse_array):
        #self.sparse_dict = _sparse_dict
        #self.max_index = _max_index
        self.sparse_dict = {}
        self.max_index = 0
        for item in sparse_array:
            if item > 0:
                self.sparse_dict[self.max_index] = item
            self.max_index += 1


    def __getitem__(self, index):
 
        if isinstance(index, slice):
            return [self.sparse_dict[i] for i in range(index.start, index.stop, index.step)]
        return self.sparse_dict[index]

    def __setitem__(self, index, value):
        self.sparse_dict[index] = value

    def __len__(self):
        return self.max_index
    
    def __delitem__(self, index):
        del(self.sparse_dict[index])

    def append(self,value):
        self.sparse_dict[self.max_index] = value
        self.max_index += 1


