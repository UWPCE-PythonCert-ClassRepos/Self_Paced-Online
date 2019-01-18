'''Author: Alex Filson
Updated: 1.18.19
SLicing Lab for Lesson 3
Py210, Online Self-Paced
'''

def exchange_first_last(seq):
    ''' Return sequence with first and last items exchanged'''
    return seq[-1]+seq[1:-1]+seq[0]

def every_other(seq):
    '''Return sequence with every other itme removed'''
    return seq[::2]
