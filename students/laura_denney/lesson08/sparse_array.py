#-------------------------------------------------#
# Title: Sparse Array
# Dev:   LDenney
# Date:  December 9, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 12/09/18, Started Sparse Array Work
#-------------------------------------------------#

class SparseArray(object):

    def __init__(self,sequence):
        self.values = {}
        self.length = len(sequence)
        for index in range(len(sequence)):
            if sequence[index]:
                self.values[index] = sequence[index]

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index not in range(self.length):
            raise IndexError
        elif index in self.values:
            return self.values[index]
        else: return 0


    def __setitem__(self, index, value):
        if index not in range(self.length):
            raise IndexError
        elif value:
            self.values[index] = value

    def __delitem__(self, index):
        if index not in range(self.length):
            raise IndexError
        temp = [0 for i in range(self.length)]
        for key, value in self.values.items():
            temp[key] = value
        del temp[index]
        self.values = {}
        for index in range(len(temp)):
            if temp[index]:
                self.values[index] = temp[index]
        self.length = len(temp)

    def __str__(self):
        temp = [0 for i in range(self.length)]
        for key, value in self.values.items():
            temp[key] = value
        return str(temp)


    def append(self, value):
        if value:
            self.values[self.length] = value
        self.length += 1








