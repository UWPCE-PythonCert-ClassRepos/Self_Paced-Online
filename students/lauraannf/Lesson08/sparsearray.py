# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:00:24 2018

@author: Laura.Fiorentino
"""


class SparseArray:
    def __init__(self, array):
        self.array = {}
        self.orig_len = len(array)
        for item, it in zip(array, range(len(array))):
            if item != 0:
                self.array[it] = item

    def __len__(self):
        return self.orig_len

    def __delitem__(self, key):
        temp = self.array.copy()
        if key <= self.orig_len:
            try:
                del self.array[key]
            except KeyError:
                pass
            finally:
                for k in list(self.array.keys()):
                    if k > key:
                        self.array[k-1] = temp[k]
                        del self.array[k]
                self.orig_len = self.orig_len - 1
        else:
            print("out of bounds")

    def __getitem__(self, index):
        if index <= self.orig_len:
            try:
                return self.array[index]
            except KeyError:
                return 0
        else:
            raise IndexError

    def __setitem__(self, index, value):
        self.array[index] = value
        if index > self.orig_len:
            self.orig_len = self.orig_len - 1

    def append(self, value):
        self.array[self.orig_len+1] = value
        self.orig_len = self.orig_len + 1
