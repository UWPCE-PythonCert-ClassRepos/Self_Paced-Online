"""
File Name: file_lab.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/17/2018
Python Version: 3.6.4
"""
import pathlib
import os


def print_paths():
    ''' Gets files in directory, prints absolute path'''
    for f in os.listdir():
        print(pathlib.Path(f).absolute())


def copy_file():
    chunk = 256
    
