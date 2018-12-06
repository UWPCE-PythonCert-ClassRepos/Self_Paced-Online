"""sparse arrary intializer

takes list like array and makes it more memory efficient
by dealing with sparse data."""


class SparseArray:
    """emulates list but reduces memory usage
    from sparse arrays"""

    def __init__(self, array):
        self.array_length = len(array)
        self.sparse_array = self.create_sparse_array(array)

    def __len__(self):
        """length of expanded array"""
        return self.array_length

    def create_sparse_array(self, expanded_array):
        """shrinks input arrary into sparse array"""
        return {index: value for index, value in enumerate(expanded_array) if value != 0}

    def expand_sparse_array(self):
        """expands current sparse array into full array for output"""
        temp_array = [0] * self.array_length
        for index, value in self.sparse_array.items():
            temp_array[index] = value
        return temp_array

    def __getitem__(self, index):
        """returns value from sparse index"""
        print(type(index))
        if isinstance(index, slice):
            return [self[i] for i in range(index.start, index.stop, index.step)]
        if index >= len(self):
            raise IndexError
        return self.sparse_array.get(index, 0)

    def __setitem__(self, index, value):
        """sets value in list or removes value from sparse array if 0"""
        if value == 0:
            self.sparse_array.pop(index, None)
        else:
            self.sparse_array[index]=value

    def append(self, value):
        """appends to the array the value specified
        if 0, doesn't change the array but increases the length
        if value, increments the length and updates sparse array"""

        if value:
            self.sparse_array[len(self)] = value
        self.array_length += 1