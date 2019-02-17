"""
Donor classes for mailroom_L9.py
Author: JohnR
Version: .1 (Lesson 09)
Last updated: 2/17/2019
Notes: Guidelines:
        Works with one donor --> Donor class
        Works with multiple donors --> DonorDB
        User input --> Main script
        Complete separation of input and data handling
"""


class Donor(object):
    def __init__(self, first, last, donations=None):
        self.first = first
        self.last = last




