class SparseArray:
# """
# Learning to emulate a built-in class by modeling a sparse array
# """
    storage_dict = {}

    def __init__(self, vals):
        self.vals = vals
        for i, elem in enumerate(self.vals):
            if elem != 0:
                self.storage_dict[i] = elem

    def __len__(self):
        return len(self.vals)

    def len_check(self, key):
        if key > len(self) - 1:
            raise IndexError("Out of range!")

    def __delitem__(self, key):
        # This needs work - what to do with vals
        self.len_check(key)
        self.storage_dict.pop(key)

    def __getitem__(self, key):
        self.len_check(key)
        if key in self.storage_dict:
            return(self.storage_dict[key])
        else:
            return 0

    def __setitem__(self, key, value):
        self.len_check(key)
        if value != 0:
            self.storage_dict[key] = value
        else:
            self.storage_dict.pop(key)

    def append(self, value):
        pass
