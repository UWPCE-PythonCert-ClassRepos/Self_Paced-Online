# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:00:24 2018

@author: Laura.Fiorentino
"""


class SparseArray:
    def __init__(self, array):
        self.array = {}
        self.zero_indices = []
        self.orig_len = len(array)
        for item, it in zip(array, range(len(array))):
            if item != 0:
                self.array[it] = item

    def __len__(self):
        return self.orig_len

    def __getitem__(self, index):
        try:
            return self.array[index]
        except KeyError:
            return 0
