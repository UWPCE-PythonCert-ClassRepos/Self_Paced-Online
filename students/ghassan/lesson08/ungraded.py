class SparseArray:

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def sa(self):
        _data_dict = {}
        for item in range(len(self.data)):
            _data_dict[self.data[item]] = item
        return [x for x in _data_dict]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        try:
            return self.sa[index]
        except IndexError:
            raise
