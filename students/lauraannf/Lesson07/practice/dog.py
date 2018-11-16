# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:24:53 2018

@author: Laura.Fiorentino
"""


class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting")

    def rollover(self):
        print(self.name.title() + "rolled over")
