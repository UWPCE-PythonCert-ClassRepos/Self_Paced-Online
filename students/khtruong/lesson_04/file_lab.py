#!/usr/bin/env python

"""This module runs the file lab script.
"""
import os


def printpath():
    """Return the full path for all files in the current directory."""
    [print(os.path.abspath(item)) for item in os.listdir()]


def copyfile(source, dest):
    """Return copy of a file from a source, to a destination.
    (without using shutil, or the OS copy command)"""

# Advanced: make it work for any size file: i.e. don’t read the entire contents
# of the file into memory at once. This should work for any kind of file, so
# you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for
# writing). Note that for binary files, you can’t use readline() – lines don’t
# have any meaning for binary files. Test it with both text and binary files
# (maybe jpeg or something of yourchosing).
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        for line in infile:
            outfile.write(line)

if __name__ == '__main__':
    printpath()
    copyfile('00-README.srt', '00-README_copied.srt')
