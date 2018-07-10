#!/usr/bin/env python3

"""
Lesson1, Task 1: Explore Errors
Lorenzo Trisolini
"""


def NameError():
    print(hello)

def SintaxError():
    print( 2 / 2 ))

def typeerror():
    a= 'Hello'
    a=a + ' World'
    a=a +5
    print(a)
    
def attributeerror():
    a = {"a":1}
    a.prepend (2)