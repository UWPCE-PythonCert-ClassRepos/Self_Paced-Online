#!/usr/bin/env python
"""Sparse Array Module"""
import operator


class SparseArray:
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, index):
        return self.seq[index]

    def __delitem__(self, index):
        del self.seq[index]

    def __setitem__(self, index, val):
        self.seq[index] = val

