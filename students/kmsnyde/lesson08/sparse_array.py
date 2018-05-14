# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:31:10 2018

@author: Karl M. Snyder
"""

class SparseArray(object):
    def __init__(self, *array):
        self.array = [obj for obj in array]
        
    def __getitem__(self, key):
        try:
            return self.array[key]
        except IndexError:
            print('Index provided is out of range.')
    
    def __setitem__(self, key, value):
        try:
            self.array[key] = value
        except IndexError:
            print("Index provided is out of range.")
    
    def __len__(self):
        return len(self.array)
    
    def append(self, new_obj):
        self.array.append(new_obj)
    
    def __delitem__(self, key):
        try:
            del self.array[key]
        except IndexError:
            print('Index provided is out of range.')
        
    def __repr__(self):
        return repr([obj for obj in self.array if obj != 0])